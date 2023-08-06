from deepview.vaal.validator.utils import tf_iou
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import random


class Drawer:
    def __init__(self, classes, alpha=0.3):
        self.classes = classes
        self.colors = []
        self.alpha = alpha
        for j in range(len(classes)):
            rc = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.colors.append(rc)

    def draw_with_pillow(
            self,
            image,
            bboxes,
            is_gt=True
    ):
        if is_gt:
            t_image = Image.new('RGB', image.size)
            img1 = ImageDraw.Draw(t_image)

            for label, x1, y1, x2, y2 in bboxes:
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                color = self.colors[int(label)]
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    fill=color
                )
            return Image.blend(image, t_image, alpha=self.alpha)

        else:
            img1 = ImageDraw.Draw(image)
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            for x1, y1, x2, y2, score, label in bboxes:
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                color = self.colors[int(label)]
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=1
                )

                img1.rectangle(
                    ((x1, y1 - 15), (x2, y1)),
                    fill=color,
                    width=3
                )
                draw.text(
                    (x1 + 10, y1 - 12),
                    "%s: %.2f" % (self.classes[int(label)], score),
                    font=font,
                    align="left",
                    fill=(255, 255, 255)
                )

            return image

    def draw_evaluation_pass(
            self,
            image,
            gt_boxes,
            dt_boxes,
            iou_threshold=0.5
    ):
        img1 = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        gt_visited = []

        for x1, y1, x2, y2, score, label in dt_boxes:

            box = np.array([[x1, y1, x2, y2]])
            ious = tf_iou(gt_boxes[..., 1:5], box).flatten()
            max_iou_idx = np.argmax(ious)
            max_iou = ious[max_iou_idx]
            dt_label = int(label)
            gt_label = int(gt_boxes[max_iou_idx][0])

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            if max_iou_idx in gt_visited or max_iou < iou_threshold:
                # duplicated prediction.
                # This node was already visited
                color = (255, 0, 0)
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=1
                )
                img1.rectangle(
                    ((x1, y1 - 15), (x2, y1)),
                    fill=color,
                    width=1
                )
                img1.text(
                    (x1 + 10, y1 - 12),
                    "%s: %.2f" % (self.classes[dt_label], score),
                    font=font,
                    align="left",
                    fill=(255, 255, 255)
                )
                continue

            if max_iou >= iou_threshold and gt_label == dt_label:
                # TP
                color = (0, 255, 0)
                gt_visited.append(max_iou_idx)
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=1
                )
                img1.rectangle(
                    ((x1, y1 - 15), (x2, y1)),
                    fill=color,
                    width=1
                )
                img1.text(
                    (x1 + 10, y1 - 12),
                    "%s: %.2f" % (self.classes[dt_label], score),
                    font=font,
                    align="left",
                    fill=(255, 255, 255)
                )
                continue

            if max_iou >= iou_threshold and gt_label != dt_label:
                # met iou test but fails class test
                color = (255, 0, 0)
                gt_visited.append(max_iou_idx)
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=1
                )
                img1.rectangle(
                    ((x1, y1 - 15), (x2, y1)),
                    fill=color,
                    width=1
                )
                img1.text(
                    (x1 + 10, y1 - 12),
                    "%s: %.2f" % (self.classes[dt_label], score),
                    font=font,
                    align="left",
                    fill=(255, 255, 255)
                )
                continue

        if len(gt_visited) < len(gt_boxes):
            for i, (label, x1, y1, x2, y2) in enumerate(gt_boxes):
                if i in gt_visited:
                    continue
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                gt_label = int(label)
                color = (0, 0, 255)
                img1.rectangle(
                    ((x1, y1), (x2, y2)),
                    outline=color,
                    width=1
                )
                img1.rectangle(
                    ((x1, y1 - 15), (x2, y1)),
                    fill=color,
                    width=1
                )
                img1.text(
                    (x1 + 10, y1 - 12),
                    "%s" % self.classes[gt_label],
                    font=font,
                    align="left",
                    fill=(255, 255, 255)
                )
        t_image = Image.new('RGB', image.size)
        img2 = ImageDraw.Draw(t_image)

        for label, x1, y1, x2, y2 in gt_boxes:
            color = (0, 255, 0)
            img2.rectangle(
                ((x1, y1), (x2, y2)),
                fill=color
            )
        return Image.blend(image, t_image, alpha=self.alpha)
