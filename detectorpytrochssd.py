import sys
sys.path.append('/home/radek/PycharmProjects/VocImageLabeler/pytorchssd')
from pytorchssd.vision.ssd.mobilenetv1_ssd import create_mobilenetv1_ssd, create_mobilenetv1_ssd_predictor

class DetectorPytrochSSD:
    path_to_model = ""
    path_to_label = ""
    detector = None
    predictor = None
    confidence = 90

    def __init__(self, custom_model, custom_labels, confidence):
        self.confidence = confidence
        self.path_to_model = custom_model
        self.path_to_label = custom_labels
        class_names = [name.strip() for name in open(self.path_to_label).readlines()]
        self.detector = create_mobilenetv1_ssd(len(class_names), is_test=True)
        self.detector.load(self.path_to_model)
        self.predictor = create_mobilenetv1_ssd_predictor(self.detector, candidate_size=200)



    def run(self, image):
        boxes, labels, probs = self.predictor.predict(image, 10, self.confidence/100)
        points_dict = dict()
        for i in range(boxes.size(0)):
            box = boxes[i, :]
            label = str(labels[i].numpy())
            if label not in points_dict:
                points_dict[label] = []
            points_dict[label].append([label, int(box[0]), int(box[1]), int(box[2]), int(box[3])])

        return points_dict
