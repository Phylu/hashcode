class TenSecondsStrategy:

    def run(self, inputFile):
        intersections = {}

        for i in range(inputFile.streetCount):
            streetEnd = inputFile.streets[i].end
            if streetEnd not in intersections.keys():
                intersections[streetEnd] = []

            intersections[streetEnd].append(inputFile.streets[i])

        intersectionSchedule = {}
        for i in range(inputFile.intersectionCount):
            intersectionSchedule[i] = []
            for j in range(len(intersections[i])):
                intersectionSchedule[i].append((intersections[i][j].name, 10))

        return intersectionSchedule