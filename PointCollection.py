import datetime

from DataPoints import *


def generateDataPoints(startTime):
    points = []
    i = 0
    file = open("./tweepyData", "r")
    line = file.readline()
    while "*" not in line:
        if "#" in line:
            i += 1
        else:
            points.append(subclassList[i]((float(line)-startTime)//3600, "I am a Tweet about BTC"))
        line = file.readline()

    file = open("./Articles", "r")
    line = file.readline()
    while "*" not in line:
        info = line.split(" ")
        timestamp = datetime.datetime(2018, 6 if "J" in info[2] else 5, int(info[2][1:]), int(info[1])//100).timestamp()
        points.append(subclassList[int(info[0])]((timestamp-startTime)//3600, "I am an Article that affects BTC prices"))
        line = file.readline()
    return points
