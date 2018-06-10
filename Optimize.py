import numpy as np
from DataPoints import *
from DataPointsCollection import POINTS
from Segmentize import get_segments


def generateWeightageMatrix(points, segments):
    m = np.zeros((len(segments), datatypes + 1))
    for point in points:
        for i in range(0, len(segments)):
            m[i][point.type] += point.time_penalty(segments[i])

    for i in range(0, len(segments)):
        for j in range(0, datatypes):
            m[i][j] = subclassList[j].weightage(m[i][j])
        m[i][datatypes] = 1
    return m


def findBestTheta(points, segs):
    """ Uses vectorized gradient descent to find the best value of the over determined matrix"""
    gradients = np.transpose(np.matrix([segment.grad for segment in segs]))
    alpha = 0.0001
    theta = np.zeros((datatypes + 1, 1))
    m = generateWeightageMatrix(points, segs)
    delta = (1 / len(segs)) * np.matmul(np.transpose(m), (np.matmul(m, theta) - gradients))
    while np.sum(np.matmul(delta, np.transpose(delta))) > 0.001:
        theta = theta - alpha * delta
        delta = (1 / len(segs)) * np.matmul(np.transpose(m), (np.matmul(m, theta) - gradients))

    return theta

if __name__ == "__main__":
    print(findBestTheta(get_segments(), POINTS))
