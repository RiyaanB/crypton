import matplotlib.pyplot as plt
from DataAccesser import *
import Segmentize
from DataPointsCollection import POINTS

plt.plot(list(range(0, len(data))), data, 'r-')

segments = Segmentize.get_segments()

x = [segment.startTime for segment in segments]
x.append(len(data)-1)
y = [data[a] for a in x]

plt.plot(x, y, 'b-')

plt.scatter([x.timestamp for x in POINTS], [7000]*len(POINTS))

plt.show()
