import matplotlib.pyplot as plt
from DataAccesser import PriceData
import Segmentize

pd = PriceData()

plt.plot(list(range(0,len(pd.data))), pd.data, 'b-')

segments = Segmentize.get_segments(pd)

x = [segment.startTime for segment in segments]
x.append(len(pd.data)-1)
y = [pd.price(a) for a in x]

plt.plot(x, y, 'r-')

plt.show()
