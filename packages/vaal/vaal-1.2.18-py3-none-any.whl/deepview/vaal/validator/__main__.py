from os.path import exists
from os import makedirs
from argparse import ArgumentParser
from deepview.vaal.validator.utils import clamp
from deepview.vaal.validator.evaluator import Evaluator
from deepview.vaal.validator.runner import Runner

if __name__ == '__main__':

    opts = ArgumentParser(description='VisionPack Detection with Python')
    opts.add_argument('-v', '--version', action='store_true',
                      help='display version information')
    opts.add_argument('-e', '--engine', type=str, default='npu',
                      help='compute engine for inference (cpu, gpu, npu)')
    opts.add_argument('-d', '--dataset', type=str, default=None,
                      help='absolute path to the dataset folder')
    opts.add_argument('-t', '--threshold', type=float, default=0.5,
                      help='detection threshold before a box is accepted')
    opts.add_argument('-u', '--iou', type=float, default=0.5,
                      help='intersect over union during nms to merge boxes')
    opts.add_argument('-i', '--model_info', type=str,
                      help='model information describes the type of model')
    opts.add_argument('-o', '--output_names', type=str,
                      help='model output names in correct order for decoding')
    opts.add_argument('-l', '--label_offset', type=int, default=0,
                      help='label offset when matching index to label name')
    opts.add_argument('-n', '--norm', type=str,
                      help='input normalization method for the model')
    opts.add_argument('-m', '--max_detection', type=int,
                      help='maximum number of detections to return')
    opts.add_argument('-w', '--warmup', type=int, default=0,
                      help='warmup iterations before processing images')
    opts.add_argument('--visualize', type=str, default=None,
                      help='path to store visualizations')
    opts.add_argument('--debug', type=str, default=None,
                      help='path to store debug data')
    opts.add_argument('model', metavar='model.rtm', type=str,
                      help='deepview-rt model (rtm) to load')
    args = opts.parse_args()

    if args.dataset is not None:
        dataset_path = args.dataset
    else:
        print("\t [ERROR] Validation script does not found a valid route at: {}".format(
            args.dataset
        ))
        exit(1)

    dataset_format = "yolo"
    predictions_format = "xyxy"
    extension_match_re = "*.jpg"
    model_path = args.model

    norm = None
    if args.norm is not None:
        norm = args.norm

    model_info = None
    if args.model_info is not None:
        model_info = args.model_info

    max_detections = 50
    if args.max_detection is not None:
        max_detections = args.max_detection

    engine = 'cpu'
    if args.engine is not None:
        engine = args.engine

    debug = args.debug
    if args.debug:
        if not exists(args.debug):
            makedirs(args.debug)

    label_offset = args.label_offset
    threshold = clamp(args.threshold, 0.0, 1.0)
    iou = clamp(args.iou, 0.0, 1.0)
    output_names = None

    warmup = args.warmup
    max_label = 16

    evaluator = Evaluator(
        dataset=dataset_path,
        gt_format=dataset_format,
        dt_format=predictions_format,
        normalized=True,
        extension=extension_match_re,
        visualize=args.visualize,
        debug=debug
    )
    if args.visualize:
        try:
            if not exists(args.visualize):
                makedirs(args.visualize)
        except Exception as e:
            print("\t - [ERROR] {}".format(
                str(e)
            ))
            exit(1)

    runner = Runner(
        model=model_path,
        norm=norm,
        engine=engine,
        threshold=threshold,
        iou=iou,
        output_names=output_names,
        label_offset=label_offset,
        max_detections=max_detections,
        model_info=model_info,
        warmup=warmup,
        max_label=max_label
    )

    evaluator.enable_vaal_interface(runner=runner)

    metrics, timings = evaluator(
        new_labels=None,
        append_background=False
    )
    print("\n"
          "===========================================================\n"
          "                  VAAL Evaluation Summary\n"
          "===========================================================")

    print("                      Metric  |  Value")
    print("-----------------------------------------------------------")
    for key, value in metrics.items():
        print("              %-15s |  %.2f" % (key, value * 100))

    print("-----------------------------------------------------------\n"
          "              Timings Report (milliseconds)\n"
          "-----------------------------------------------------------")
    print("      load image | avg: %5.2f min: %5.2f max: %5.2f" %
          (timings['avg_input'] * 1e-6,
           timings['min_input_time'] * 1e-6,
           timings['max_input_time'] * 1e-6))

    print("      inference  | avg: %5.2f min: %5.2f max: %5.2f" %
          (timings['avg_inference'] * 1e-6,
           timings['min_inference_time'] * 1e-6,
           timings['max_inference_time'] * 1e-6))

    print("      box decode | avg: %5.2f min: %5.2f max: %5.2f" %
          (timings['avg_decoding'] * 1e-6,
           timings['min_decoding_time'] * 1e-6,
           timings['max_decoding_time'] * 1e-6))
