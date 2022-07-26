from collections import namedtuple
import argparse
import cv2
import jetson.inference
import jetson.utils
import logging
import numpy as np
import sys

logger = logging.getLogger('root')


class DetectorJetson:
    path_to_model = ""
    path_to_label = ""
    detector = None
    width = 0
    height = 0

    def __init__(self, width, height, custom_model, custom_labels):
        self.width = width
        self.height = height
        argv = ['--model=' + custom_model, '--labels=' + custom_labels,
                '--input-blob=input_0', '--output-cvg=scores', '--output-bbox=boxes']
        parser = argparse.ArgumentParser(
            description="Locate objects in a live camera stream using an object detection DNN.",
            formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                                                  jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

        parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
        parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
        parser.add_argument("--network", type=str, default="ssd-mobilenet-v1",
                            help="pre-trained model to load (see below for options)")
        parser.add_argument("--overlay", type=str, default="box,labels,conf",
                            help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
        parser.add_argument("--model", type=str, default=custom_model, help="minimum detection threshold to use")
        parser.add_argument("--labels", type=str, default=custom_labels, help="minimum detection threshold to use")
        parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

        try:
            opt = parser.parse_known_args()[0]
            self.detector = jetson.inference.detectNet(opt.network, argv, opt.threshold)
        except:
            e = sys.exc_info()[0]
            logger.error("Can't init Jetson model with error:" + e)
            raise
        else:
            logger.error("Jetson model init OK!")

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def detect(self, image):
        detections = self.detector.Detect(image)
        arr = jetson.utils.cudaToNumpy(image, self.width, self.height)
        arr1 = cv2.cvtColor(arr.astype(np.uint8), cv2.COLOR_RGBA2BGR)
        return arr1, detections

    def run(self, image):
        _, detections = self.detect(image)
        Points = namedtuple('Points', ['classid', 'x1', 'y1', 'x2', 'y2'])
        points_dict = dict()
        for detect in detections:
            if detect.ClassID not in points_dict:
                points_dict[detect.ClassID] = []
            points_dict[detect.ClassID].append(Points(detect.ClassID, detect.Left, detect.Top, detect.Right, detect.Bottom))

        return points_dict
