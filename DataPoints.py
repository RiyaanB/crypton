import numpy


class DataPoint:
    def __init__(self, timestamp, description, typ):
        self.timestamp = timestamp
        self.description = description
        self.type = typ

    def time_penalty(self, segment):
        return 0 if self.timestamp > segment.endTime \
            else numpy.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq


class TwitterPositive(DataPoint):
    pass


class TwitterNegative(DataPoint):
    pass


subclassList = {0:TwitterPositive.weightage,
                1:TwitterNegative.weightage}

datatypes = 2