class UsedStreetsStrategy:

    def run(self, inputFile):
        streetUsage = {}
        for car in inputFile.cars:
            for street in car.streets:
                if street not in streetUsage:
                    streetUsage[street] = 0
                streetUsage[street] += 1

        intersections = {}

        for i in range(inputFile.streetCount):
            streetEnd = inputFile.streets[i].end
            if streetEnd not in intersections.keys():
                intersections[streetEnd] = []

            intersections[streetEnd].append(inputFile.streets[i])

        intersectionSchedule = {}

        for i in range(inputFile.intersectionCount):
            for street in intersections[i]:
                if street.name in streetUsage:
                    if i not in intersectionSchedule:
                        intersectionSchedule[i] = []
                    intersectionSchedule[i].append((street.name, 1))

        return intersectionSchedule