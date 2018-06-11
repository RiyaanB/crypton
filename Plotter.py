import matplotlib.pyplot as plt

import PointCollection
from DataAccesser import *
import Segmentize

TEXT_STARTING_POINT = 1515628800  # UNIX Time Stamp for first stock market data in "PriceData"
trainStartTime = 1527811200  # The data we are considering to train
trainEndTime = 10000000000000 #1528441200

data = generate_price("PriceData", trainStartTime, trainEndTime, TEXT_STARTING_POINT)

"""Just a utility module to plot and visualize the segments"""


plt.plot(list(range(0, len(data))), data, 'r-')

segments = Segmentize.get_segments(data)

x = [segment.startTime for segment in segments]
x.append(len(data)-1)
y = [data[a] for a in x]

plt.plot(x, y, 'b-')

Points = PointCollection.generateDataPoints(trainStartTime)

#for point in Points:
#    plt.plot(point.timestamp, 7600, 'bx' if point.pos else 'rx')
#
plt.show()
