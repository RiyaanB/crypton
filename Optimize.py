import numpy as np
from DataAccesser import PriceData
from DataPoints import *
from Segmentize import get_segments

pd = PriceData()
segments = get_segments(pd)
gradients = np.transpose(np.matrix([segment.grad for segment in segments]))

points = [TwitterNegative(7, "Positive tweets", 1)]

m = np.zeros((len(segments), datatypes+1))

for point in points:
    for i in range(0, len(segments)):
        m[i][point.type] += point.time_penalty(segments[i])

for i in range(0, len(segments)):
    for j in range(0, datatypes):
        m[i][j] = subclassList[j](m[i][j])

alpha = 1
theta = np.zeros((datatypes+1, 1))


def J():
    i = H() - gradients
    return np.transpose(i) * i


def H():
    return np.matmul(m, theta)

