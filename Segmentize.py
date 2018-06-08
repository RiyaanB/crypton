from DataAccesser import PriceData
pd = PriceData()


class Segment:
    pass


def get_segments(pd):
    segments = []
    startTime = 0
    endTime = 1
    limit = len(pd.data)
    error = 0
    best = 10
    N = 1.2
    while endTime < limit:
        error = 0
        for i in range(startTime, limit):
            predicted_price = ((pd.price(endTime)-pd.price(startTime))/(endTime-startTime)) * (i-startTime) + pd.price(startTime)
            error += (pd.price(i) - (predicted_price))**2
        error
        endTime += 1