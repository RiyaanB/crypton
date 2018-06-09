data = []
file = open("./PriceData", "r")
line = file.readline()

while not "#" in line:
    data.append(line)
    line = file.readline()

b = [float(a) for a in data]
data = [b[index] for index in range(0, len(data), 1)]
print("Data: " + str(len(data)))
