import detectorjetson
import detectorpytrochssd


def factory(type, paths_tuple):
    if type == 1:
        return detectorjetson.DetectorJetson(paths_tuple.path_to_model, paths_tuple.path_to_images_label)
    else:
        return detectorpytrochssd.DetectorPytrochSSD(paths_tuple.path_to_model, paths_tuple.path_to_images_label)
