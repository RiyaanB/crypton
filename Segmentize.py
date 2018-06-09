from DataAccesser import *


class Segment:
    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.grad = (data[endTime] - data[startTime])/(endTime - startTime)

    def __str__(self):
        return "(" + str(self.startTime) + ":" + str(self.endTime) + ")"


def get_segments():
    segments = []
    startTime = 0
    limit = len(data)
    while startTime < limit-1:
        endTime = startTime + 1
        bestIndex = endTime
        error = 0
        while endTime < limit:
            grad = (data[endTime] - data[startTime]) / (endTime - startTime)
            for i in range(startTime+1, endTime):
                predicted_val = (grad * (i-startTime)) + data[startTime]
                error += (data[i] - predicted_val)**2

            if error/(endTime-startTime+1) < 20000:
                bestIndex = endTime
            else:
                break

            endTime += 1
        segments.append(Segment(startTime, bestIndex))
        startTime = bestIndex
    print("Segments: " + str(len(segments)))
    return segments
