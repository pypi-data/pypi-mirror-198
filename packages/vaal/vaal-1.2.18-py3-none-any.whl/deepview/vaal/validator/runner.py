from time import monotonic_ns as clock_now
import deepview.vaal as vaal
from PIL import Image
import numpy as np


class Runner:
    def __init__(
            self,
            model: str,
            norm: str,
            engine: str,
            threshold: float,
            iou: float,
            output_names: str,
            label_offset: int,
            max_detections: int,
            model_info: str,
            warmup: int,
            max_label: int
    ):
        self.model = model
        self.norm = norm
        self.engine = engine
        self.threshold = threshold
        self.iou = iou
        self.output_names = output_names
        self.label_offset = label_offset
        self.max_detections = max_detections
        self.model_info = model_info
        self.ctx = None
        self.warmup = warmup
        self.max_label = max_label
        self.init_runner()

        self.box_timings = []
        self.inference_timings = []
        self.loading_input_timings = []

    def clamp(self, value, min, max):
        return min if value < min else max if value > max else value

    def init_runner(self):
        self.ctx = vaal.Context(self.engine)

        if self.model_info is not None:
            self.ctx['model_info'] = self.model_info

        if self.max_detections is not None:
            self.ctx['max_detection'] = self.max_detections

        self.ctx['score_threshold'] = self.clamp(self.threshold, 0.0, 1.0)
        self.ctx['iou_threshold'] = self.clamp(self.iou, 0.0, 1.0)

        self.ctx['label_offset'] = self.label_offset

        if self.norm is not None:
            if self.norm == 'raw':
                self.ctx['normalization'] = vaal.ImageProc.RAW.value
            elif self.norm == 'signed':
                self.ctx['normalization'] = vaal.ImageProc.SIGNED_NORM.value
            elif self.norm == 'unsigned':
                self.ctx['normalization'] = vaal.ImageProc.UNSIGNED_NORM.value
            elif self.norm == 'whitening':
                self.ctx['normalization'] = vaal.ImageProc.WHITENING.value
            elif self.norm == 'imagenet':
                self.ctx['normalization'] = vaal.ImageProc.IMAGENET.value
            else:
                print('unsupported normalization method: %s' % self.norm)
                exit(1)

        self.ctx.load_model(self.model)

        if self.warmup > 0:
            from timeit import timeit
            t = timeit(self.ctx.run_model, number=self.warmup)
            print('model warmup took %f seconds (%f ms avg)' %
                  (t, t * 1000 / self.warmup))

        if self.max_label is None:
            self.max_label = 16

    def __call__(self, image_path):
        """
        Computes
        """
        W, H = Image.open(image_path).size
        start = clock_now()

        self.ctx.load_image(image_path)
        load_ns = clock_now() - start
        self.loading_input_timings.append(load_ns)

        start = clock_now()
        self.ctx.run_model()
        infer_ns = clock_now() - start
        self.inference_timings.append(infer_ns)

        start = clock_now()
        bxs = self.ctx.boxes()
        boxes_ns = clock_now() - start
        self.box_timings.append(boxes_ns)

        outputs = []
        for j, box in enumerate(bxs):
            outputs.append([box.xmin * W, box.ymin * H, box.xmax * W, box.ymax * H, box.score, box.label])
        return np.array(outputs)

    def summary(self):
        return {
            'min_inference_time': np.min(self.inference_timings),
            'max_inference_time': np.max(self.inference_timings),
            'min_input_time': np.min(self.loading_input_timings),
            'max_input_time': np.max(self.loading_input_timings),
            'min_decoding_time': np.min(self.box_timings),
            'max_decoding_time': np.max(self.box_timings),
            'avg_decoding': np.mean(self.box_timings),
            'avg_input': np.mean(self.loading_input_timings),
            'avg_inference': np.mean(self.inference_timings),
        }
