import numpy
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

    def time_penalty(self, segment):
        return 0 if self.timestamp > segment.endTime \
            else numpy.exp(-(((segment.startTime - self.timestamp)/8)**2))

    @staticmethod
    def weightage(wfreq):
        return wfreq

    def __str__(self):
        return str(self.timestamp) + " " + self.description


class TwitterHighPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 0


class TwitterLowPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 1


class TwitterHighNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 2


class TwitterLowNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 3


class DominantPositive(DataPoint): #9 days
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 4


class DominantNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 5


class SubstantialPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 6


class SubstantialNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 7


class WeakPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 8


class WeakNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 9


class OtherPositive(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 10


class OtherNegative(DataPoint):
    def __init__(self, timestamp, description):
        super().__init__(timestamp, description)
        self.type = 11


subclassList = {0: TwitterHighPositive,
                1: TwitterLowPositive,
                2: TwitterHighNegative,
                3: TwitterLowNegative,
                4: DominantPositive,
                5: DominantNegative,
                6: SubstantialPositive,
                7: SubstantialNegative,
                8: WeakPositive,
                9: WeakNegative,
                10: OtherPositive,
                11: OtherNegative}
datatypes = 12
