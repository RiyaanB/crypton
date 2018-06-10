import datetime
from DataPoints import *


def CollectDataPoints(startTime, endTime):
    file = open("./tweeter_details", "r")

    p = ""
    while "*" not in p:
        p += file.readline()

    p = p.split("#")
    p = [element.split("\n") for element in p]
    for lst in p:
        lst.pop(0)
        lst.pop(-1)

    for lst in p:
        for i in range(0, len(lst)):
            lst[i] = (float(lst[i]) - startTime) / 3600

    file.close()
    file2 = open("./tweepyData", "r")
    p2 = ""
    while "*" not in p2:
        p2 += file2.readline()
    p2 = p2.split("#")
    p2 = [element.split("\n") for element in p2]
    for lst in p2:
        lst.pop(0)
        lst.pop(-1)

    for lst in p:

    for i in range(0, 4):
        for ele in p2[i]:
            if float(ele) - 5.5 * 3600 > startTime:
                p[i].append(float(ele) - 5.5 * 3600)
    print(p)
    t1 = [subclassList[0](point, "Tweet") for point in p[0]]
    t2 = [subclassList[1](point, "Tweet") for point in p[1]]
    t3 = [subclassList[2](point, "Tweet") for point in p[2]]
    t4 = [subclassList[3](point, "Tweet") for point in p[3]]

    # p contains points for each subclass of DataPoint

    file = open("./Articles", "r")
    text = ""
    while "*" not in text:
        text += file.readline()

    text = text[0:len(text) - 1]
    text = text.split("\n")
    text = text[0:len(text) - 1]
    for t in range(0, len(text)):
        text[t] = text[t].split(" ")
        text[t] = subclassList[int(text[t][0])]((datetime.datetime(2018, 6 if "J" in text[t][2] else 5,
                                                                   int(text[t][2][1:]), int(text[t][1]) // 100, 0,
                                                                   0).timestamp() - startTime) // 3600,
                                                "I affect BTC prices")

    POINTS = text + t1 + t2 + t3 + t4
    POINTS.sort(key=lambda point: point.timestamp)
    file.close()
    return POINTS

