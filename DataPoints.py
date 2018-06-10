import numpy
import math
"""A DataPoint is anything that has the power to fluctuate price of Bitcoin. 
These include tweets, articles, reddit posts etc..
Each DataPoint should be classified into its subclasses such that all things inside each 
class have similar attributes and have the potential to cause a change in price of BTC 
of the same magnitude and direction
Each class can also choose to define the weightage of the sources as a function of time """


class DataPoint:
    def __init__(self, timestamp, description):
        self.timestamp = timestamp
        self.description = description
        self.type = -1
        self.pos = False

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq

    def __str__(self):
        return str(self.timestamp) + " " + str(self.__class__)


class TwitterHighPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 0
        self.pos = True

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq**0.5

class TwitterLowPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 1
        self.pos = True

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq ** 0.5

class TwitterHighNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 2
        self.pos = False

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq ** 0.5

class TwitterLowNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 3
        self.pos = False

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/4)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq ** 0.5

class DominantPositive(DataPoint): #9 days
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 4
        self.pos = True

    def time_penalty(self, segment):
        if self.timestamp > segment.endTime:
            return 0
        elif segment.startTime <= self.timestamp <= segment.endTime:
            return 1
        else:
            return math.exp(-(((segment.startTime - self.timestamp)/2)**2))


class DominantNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 5
        self.pos = False


class GovernmentPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 6
        self.pos = True


class GovernmentNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 7
        self.pos = False


class WeakPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 8
        self.pos = True


class WeakNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 9
        self.pos = False


class OtherPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 10
        self.pos = True


class OtherNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 11
        self.pos = False


subclassList = {0: TwitterHighPositive,
                1: TwitterLowPositive,
                2: TwitterHighNegative,
                3: TwitterLowNegative,
                4: DominantPositive,
                5: DominantNegative,
                6: GovernmentPositive,
                7: GovernmentNegative,
                8: WeakPositive,
                9: WeakNegative,
                10: OtherPositive,
                11: OtherNegative}
datatypes = 12
