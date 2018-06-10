

def generate_price(filepath, startTime, endTime, textStartingPoint):
    """Generates a list of hourly prices of BTC"""
    retVal = []
    file = open("./"+filepath, "r")
    line = file.readline()
    currentTime = textStartingPoint
    while not "#" in line:
        if startTime <= currentTime <= endTime:
            retVal.append(line)
        line = file.readline()
        currentTime += 3600

    b = [float(a) for a in retVal]
    retVal = [b[index] for index in range(0, len(retVal), 1)]
    #print("Data: " + str(len(data)))
    file.close()
    return retVal

