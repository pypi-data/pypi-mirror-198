from os.path import join, exists, splitext
from typing import Tuple
from PIL import Image
import numpy as np
import warnings
import glob


class Dataset:
    def __init__(
            self,
            path: str,
            gt_format: str,
            normalized: bool,
            extension: str,
    ):
        """
        Class constructor

        :param path: Absolute path to dataset folder
        :param gt_format: it could be either of thew following: yolo, xyxy or xywh
            yolo: is in x_center,y_center, box_width, box_height
            xyxy: integer values representing 4 corners of the bounting box (top_left_x, top_left_y), (bottom_right_x, bottom_right_y)
        :param normalized: Weather data is normalized by the image dimension or not
        :param extension: image extension. it should be either of the following "*.jpg", "*.png", "*.jpeg".
        For a different extension the program will rise an extension
        """
        self.dataset_path = path
        self.gt_format = gt_format.lower()
        self.normalized = normalized
        self.extension = extension
        label_file = join(path, 'labels.txt')

        if not exists(label_file):
            print("\t [ERROR] label file was not found in: {}".format(
                label_file
            ))
            exit(1)

        with open(label_file) as fp:
            self.labels = [line.rstrip().lower() for line in fp.readlines()]

        if not (self.gt_format in ['yolo', 'xyxy', 'xywh']):
            print(
                "\t Unsupported dataset format was provided: [{}]\n"
                "\t Only either of these 'yolo', 'xyxy', 'xywh' is accepted".format(
                    gt_format
                )
            )
            exit(0)

        self.transformer = None
        if self.gt_format == 'yolo':
            self.transformer = self.yolo2xyxy
        elif self.gt_format == 'xywh':
            self.transformer = self.xywh2xyxy
        else:
            self.transformer = None

        if not (extension in ["*.jpg", "*.png", "*.jpeg"]):
            print(
                "\t Unsupported extension was provided. [{} is not a valid extension]\n"
                "\t Only \"*.jpg\", \"*.png\", \"*.jpeg\" are supported".format(
                    self.extension)
            )
            exit(0)

        self.dataset = self.read_dataset()

    def read_dataset(self) -> list:
        """
        This function loads all the filenames from the path.
        Annotations must have the same name as the image, only changing the extension by .txt
        :return: list of Tuples (image_)
        """

        images = glob.glob(
            join(self.dataset_path, self.extension)
        )

        if len(images) == 0:
            print(
                "\t You provided an empty dataset. Please the absolute path pointed by ``path`` variable in the "
                "constructor is a valid dataset structure"
            )
            exit(0)

        dataset = list()

        num_samples = len(images)
        for index in range(num_samples):
            print("\t - [INFO]: Reading annotation: %i of %i [%2.f %s]" % (
                index + 1,
                num_samples,
                100 * ((index+1)/float(num_samples)),
                '%'
            ), end='\r')
            image_path = images[index]
            annotation_path = splitext(image_path)[0] + '.txt'

            if exists(image_path) and exists(annotation_path):
                dataset.append(
                    (image_path, annotation_path)
                )

        if len(dataset) == 0:
            print(
                "\t Invalid dataset was provided at: {}".format(
                    self.dataset_path
                )
            )
            exit(0)

        return dataset

    def yolo2xyxy(self, annotations):
        w_c = annotations[..., 2:3]
        h_c = annotations[..., 3:4]

        annotations[..., 0:1] = annotations[..., 0:1] - w_c / 2
        annotations[..., 1:2] = annotations[..., 1:2] - h_c / 2
        annotations[..., 2:3] = annotations[..., 0:1] + w_c
        annotations[..., 3:4] = annotations[..., 1:2] + h_c

        return annotations

    def xywh2xyxy(self, annotations):
        annotations[..., 2:3] = annotations[..., 2:3] + annotations[..., 0:1]
        annotations[..., 3:4] = annotations[..., 3:4] + annotations[..., 1:2]
        return annotations

    def load_instance(
            self,
            data: Tuple
    ) -> dict:
        """
        This function loads a single instance from dataset.
        Basically it load annotations and return image_path and annotations in a Tuple format

        :param data: (image_path, annotation_path)

        :return: Tuple(str, ndarray) or None in case the annotation is empty or file does not exist
        """
        image_path, annotation_path = data
        W, H = Image.open(image_path).size

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            annotation = np.genfromtxt(annotation_path)
        if len(annotation):
            annotation = annotation.reshape(-1, 5)
        else:
            return {}

        boxes = self.transformer(annotation[:, 1:5]) if self.transformer else annotation[:, 1:5]
        boxes[..., 0] *= W
        boxes[..., 1] *= H
        boxes[..., 2] *= W
        boxes[..., 3] *= H
        return {
            'image': image_path,
            'boxes': boxes,
            'labels': annotation[:, 0:1].flatten().astype(np.int32),
        }
