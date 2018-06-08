class PriceData:
    def __init__(self):
        self.data = []
        self.file = open("./PriceData", "r")
        line = self.file.readline()
        while not "#" in line:
            self.data.append(line)
            line = self.file.readline()

    def price(self, hour):
        return self.data[hour]
