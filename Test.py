import Segmentize
import DataAccesser
import PointCollection
import Optimize
import numpy as np

TEXT_STARTING_POINT = 1515628800  # UNIX Time Stamp for first stock market data in "PriceData"
trainStartTime = 1527811200  # The data we are considering to train
trainEndTime = 1528441200

Points = PointCollection.generateDataPoints(trainStartTime)

trainingPrices = DataAccesser.generate_price("PriceData", trainStartTime, trainEndTime, TEXT_STARTING_POINT)
trainingSegments = Segmentize.get_segments(trainingPrices)
theta = Optimize.findBestTheta(Points, trainingSegments)

testStartTime = trainEndTime
testEndTime = 100000000000

testingPrices = DataAccesser.generate_price("PriceData", testStartTime, testEndTime, TEXT_STARTING_POINT)
testSegments = Segmentize.get_segments(testingPrices)

m = Optimize.generateWeightageMatrix(Points, testSegments)
gradients = np.transpose(np.matrix([segment.grad for segment in testSegments]))
print("Predicted Gradients of BTC price")
print(np.matmul(m, theta))
print("\n Actual Gradient")
print(gradients)