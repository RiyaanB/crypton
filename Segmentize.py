import Constants
from DataAccesser import PriceData
pd = PriceData()


class Segment:

    def __init__(self, startTime, endTime):
        self.startTime = startTime
        self.endTime = endTime
        self.grad = (pd.price(endTime) - pd.price(startTime))/(endTime - startTime)

    def __str__(self):
        return "(" + str(self.startTime) + ":" + str(self.endTime) + ")"


def get_segments(pd):
    segments = []
    startTime = 0
    limit = len(pd.data)
    while startTime < limit-1:
        endTime = startTime + 1
        bestIndx = endTime
        error = 0
        while endTime < limit:
            grad = (pd.price(endTime) - pd.price(startTime)) / (endTime - startTime)
            for i in range(startTime+1,endTime):
                predicted_val = (grad * (i-startTime)) + pd.price(startTime)
                error += (pd.price(i) - predicted_val)**2

            if error/(endTime-startTime+1) < Constants.N:
                bestIndx = endTime

            endTime += 1
        segments.append(Segment(startTime, bestIndx))
        startTime = bestIndx
    return segments

