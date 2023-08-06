from deepview.vaal.validator.dataset import Dataset
from deepview.vaal.validator.drawer import Drawer
from deepview.vaal.validator.utils import *
from PIL import Image
from os.path import basename, join


class Evaluator:
    def __init__(
            self,
            dataset: str,
            gt_format: str,
            dt_format: str,
            normalized: bool,
            extension: str,
            visualize: str,
            debug: str
    ):
        """
        Class constructor

        :param model: RTM model ready to run on VisionPack
        :param dataset: Absolute path to the dataset
        :param gt_format: dataset format (See Dataset constructor for additional info)
        :param dt_format: output format
        :param normalized: weather the gt is normalized or not
        :param extension: dataset extension for images
        """
        self.dataset = Dataset(
            path=dataset,
            gt_format=gt_format,
            normalized=normalized,
            extension=extension
        )
        self.dt_format = dt_format
        if not (self.dt_format in ['xyxy', 'xywh']):
            print(
                "\t Unsupported dataset format was provided: [{}]\n"
                "\t Only either of 'xyxy' or 'xywh' is accepted".format(
                    dt_format
                )
            )
            exit(0)
        self.runner = None
        self.label_map = None
        self.drawer = None
        self.visualize = visualize
        self.debug = debug
        self.sync_dict = {
            "motorbike": 'motorcycle',
            'aeroplane': 'airplane',
            'sofa': 'couch',
            'pottedplant': 'potted plant',
            'diningtable': 'dining table',
            'tvmonitor': 'tv'
        }

    def enable_vaal_interface(self, runner):
        """
        Sets the VAAL context into the Evaluator class
        :param runner: VAAL.Context interface
        """
        self.runner = runner

    def match_predictions(self, predictions):
        n_pred = predictions.copy()
        for i in range(n_pred.shape[0]):
            cls_id = n_pred[i][-1]
            n_pred[i][-1] = self.label_map[cls_id]
        return n_pred

    def build_mapper(self, new_labels):
        if new_labels is None:
            return
        self.label_map = dict()
        gt_labels = self.dataset.labels

        for i, label in enumerate(new_labels):
            if label in gt_labels:
                new_id = gt_labels.index(label)
                self.label_map[float(i)] = float(new_id)
            else:
                alias_name = self.sync_dict.get(label, None)
                if alias_name is None:
                    print('\t - [WARNING] ``{}`` label does not exist on label file'.format(
                        label
                    ))
                else:
                    if alias_name in gt_labels:
                        new_id = gt_labels.index(alias_name)
                        self.label_map[float(i)] = float(new_id)

    def __call__(self, new_labels=None, append_background=False):
        """
        Computes evaluation metrics
        """
        if new_labels is None and \
                (self.runner.ctx.labels is None or len(self.runner.ctx.labels) == 0):
            print(
                "\t - [ERROR] Labels where not found in model neither provided "
                "in --labels parameter. Aborting validation")
            exit(1)

        prediction_labels = self.runner.ctx.labels
        self.build_mapper(new_labels=prediction_labels)

        if self.visualize:
            print("\t - [INFO]: Saving visualizations to: %s" % self.visualize)
            self.drawer = Drawer(
                alpha=0.5,
                classes=prediction_labels
            )

        nc = 80
        iouv = np.linspace(0.5, 0.95, 10)  # iou vector for mAP@0.5:0.95
        niou = iouv.shape[0]
        dt, p, r, f1, mp, mr, map50, map = [0.0, 0.0, 0.0], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        stats, ap, ap_class = [], [], []

        num_samples = len(self.dataset.dataset)
        for index in range(num_samples):
            print("\t - [INFO]: Computing Metrics for instance: %i of %i [%2.f %s]" % (
                index + 1,
                num_samples,
                100 * ((index + 1) / float(num_samples)),
                '%'
            ), end='\r')
            instance = self.dataset.dataset[index]
            annotations = self.dataset.load_instance(instance)

            if len(annotations) == 0:
                continue

            labelsn = []
            tcls = []

            image_path = annotations['image']
            boxes = annotations['boxes']
            labels = annotations['labels']

            for i, box in enumerate(boxes):
                x1, y1, x2, y2 = box
                gt_label_id = labels[i]
                tcls.append(gt_label_id)
                labelsn.append([gt_label_id, x1, y1, x2, y2])

            predn = self.runner(image_path=image_path)
            predn = self.match_predictions(
                predictions=predn
            )

            labelsn = np.array(labelsn).astype(np.float32)
            predn = np.array(predn).astype(np.float32)
            pred = predn.copy()

            nl = len(labelsn)
            tcls = labelsn[:, 0].tolist() if nl else []  # target class
            if len(pred) == 0:
                if nl:
                    stats.append((np.zeros(shape=(0, niou), dtype=np.bool_), [], [], tcls))
                continue

            if nl:
                tbox = labelsn[:, 1:5]
                labelsn = np.concatenate((labelsn[:, 0:1], tbox), 1)  # native-space labels
                correct = process_batch_np(predn, labelsn, iouv)
            else:
                correct = np.zeros(shape=(pred.shape[0], niou), dtype=np.bool_)
            stats.append((correct, pred[:, 4], pred[:, 5], tcls))

            if self.debug:
                np.save(join(self.debug, 'gt_{}'.format(index)), labelsn)
                np.save(join(self.debug, 'dt_{}'.format(index)), pred)

            if self.drawer:
                original_image = Image.open(image_path).convert('RGB').copy()
                n_image = self.drawer.draw_evaluation_pass(
                    image=original_image,
                    gt_boxes=labelsn,
                    dt_boxes=pred,
                    iou_threshold=0.5
                )
                n_path = join(self.visualize, basename(image_path))

                n_image.save(
                    n_path
                )

            if len(pred) == 0:
                stats.append((np.zeros(shape=(0, niou), dtype=np.bool), np.array([]), np.array([]), tcls))
            else:
                correct = process_batch_np(pred, labelsn, iouv)
                stats.append((correct, pred[:, 4], pred[:, 5], tcls))

        stats = [np.concatenate(x, 0) for x in zip(*stats)]  # to numpy

        tp, fp, p, r, f1, ap, ap_class = ap_per_class(*stats)
        ap50, ap75, ap = ap[:, 0], ap[:, 5], ap.mean(1)  # AP@0.5, AP@0.5:0.95
        mp, mr, map50, map75, map = p.mean(), r.mean(), ap50.mean(), ap75.mean(), ap.mean()

        return {
                   "mAP@0.5": map50,
                   "mAP@0.75": map75,
                   "mAP@0.5:0.95": map,
                   "Recall@0.5:0.95": mr
               }, self.runner.summary()
