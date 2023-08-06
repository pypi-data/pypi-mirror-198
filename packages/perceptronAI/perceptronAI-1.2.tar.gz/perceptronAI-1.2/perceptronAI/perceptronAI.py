from numpy import array, exp, dot, sum
from random import uniform
from tqdm import tqdm


class Perceptron:
    def __init__(self):
        self.w = None

    def creation(self, x, y, i, bar=True):
        self.w = array([uniform(-1, 1) for _ in range(len(x[0]))])
        for _ in (tqdm(range(i), bar_format='{percentage:3.0f}% |{bar:100}|') if bar else range(i)):
            output = []
            for j in range(len(x)):
                output.append(1 / (1 + exp(-sum(x[j] * self.w))))
                self.w = self.w + array([[y[j][0] - output[j]][0] * output[j] * (1 - output[j]) * x[j][k] for k in range(len(x[j]))])
        self.w = list(self.w)
        return self.w

    def generation(self, y):
        return 1 / (1 + exp(-dot(y, array(self.w))))
