from typing import List, Any


def iou_metric(input_feats_1: List[Any], input_feats_2: List[Any]) -> float:
    if not(isinstance(input_feats_1, list)):
        set_1 = set([input_feats_1])
    else:
        set_1 = set(input_feats_1)

    if not(isinstance(input_feats_2, list)):
        set_2 = set([input_feats_2])
    else:
        set_2 = set(input_feats_2)

    metric = len(set_1.intersection(set_2)) / len(set_1.union(set_2))

    return metric

def intersection_metric(input_feats_1: List[Any], input_feats_2: List[Any]) -> float:
    if not(isinstance(input_feats_1, list)):
        set_1 = set([input_feats_1])
    else:
        set_1 = set(input_feats_1)

    if not(isinstance(input_feats_2, list)):
        set_2 = set([input_feats_2])
    else:
        set_2 = set(input_feats_2)

    metric = len(set_1.intersection(set_2))

    return metric