
import Segmentize
import DataAccesser
import DataPointsCollection
import Optimize
TEXT_STARTING_POINT = 1515628800  # UNIX Time Stamp for first stock market data in "PriceData"
trainStartTime = 1527638400  # The data we are considering to train
trainEndTime = 100000000000000

trainingPrices = DataAccesser.generate_price("PriceData", trainStartTime, trainEndTime, TEXT_STARTING_POINT)
trainingSegments = Segmentize.get_segments(trainingPrices)
trainingPoints = DataPointsCollection.generateDataPoints(trainStartTime, trainEndTime)
theta = Optimize.findBestTheta(trainingPoints, trainingSegments)





