import numpy as np
from scipy.spatial import distance


def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
    cosine_sim = float(1 - distance.cosine(vec1, vec2))
    return cosine_sim
