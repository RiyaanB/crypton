import numpy as np
from DataPoints import *
from Segmentize import get_segments

segments = get_segments()
gradients = np.transpose(np.matrix([segment.grad for segment in segments]))

points = [TwitterNegative(7, "Positive tweets", 1)]

m = np.zeros((len(segments), datatypes+1))

for point in points:
    for i in range(0, len(segments)):
        m[i][point.type] += point.time_penalty(segments[i])

for i in range(0, len(segments)):
    for j in range(0, datatypes):
        m[i][j] = subclassList[j](m[i][j])
    m[i][datatypes] = 1


def J():
    i = H() - gradients
    return np.transpose(i) * i


def H():
    return np.matmul(m, theta)

alpha = 0.1
theta = np.zeros((datatypes+1, 1))

delta = (1/len(segments))*np.matmul(np.transpose(m), (H()-gradients))
while np.sum(np.matmul(delta, np.transpose(delta))) > 0.001:
    print(np.sum(np.matmul(delta, np.transpose(delta))))
    theta = theta - alpha*delta
    delta = (1 / len(segments)) * np.matmul(np.transpose(m), (H() - gradients))

print(theta)
