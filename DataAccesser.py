data = []
file = open("./PriceData", "r")
line = file.readline()

TEXT_STARTING_POINT = 1515628800  # UNIX Time Stamp for first stock market data in "PriceData"
startUNIXTime = 1527638400   # The data we are considering to train
endUNIXTime = 100000000000000

while not "#" in line:
    data.append(line)
    line = file.readline()

b = [float(a) for a in data]
data = [b[index] for index in range(0, len(data), 1)]
print("Data: " + str(len(data)))