class FirstStreetStrategy:

    def run(self, inputFile):
        intersections = {}

        for i in range(inputFile.streetCount):
            streetEnd = inputFile.streets[i].end
            if streetEnd not in intersections.keys():
                intersections[streetEnd] = []

            intersections[streetEnd].append(inputFile.streets[i])

        intersectionSchedule = {}
        for i in range(inputFile.intersectionCount):
            intersectionSchedule[i] = [(intersections[i][0].name, 1)]

        return intersectionSchedule