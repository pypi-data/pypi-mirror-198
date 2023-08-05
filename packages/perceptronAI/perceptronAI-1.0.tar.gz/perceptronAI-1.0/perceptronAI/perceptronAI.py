import numpy as np
import random
from tqdm import tqdm

def Creation(x, y, z, bar=None):
    w = np.array([random.uniform(-1, 1) for _ in range(len(x[0]))])
    for _ in (tqdm(range(z), bar_format='{percentage:3.0f}% |{bar:100}|') if bar else range(z)):
        output = []
        for j in range(len(x)):
            output.append(1 / (1 + np.exp(-np.sum(x[j] * w))))
            w = w + np.array([[y[j][0] - output[j]][0] * output[j] * (1 - output[j]) * x[j][k] for k in range(len(x[j]))])
    return w.tolist()

def Generation(x, y):
    return 1 / (1 + np.exp(-np.dot(y, x)))
