class MostUsedStreetStrategy:

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
            bestStreet = None
            for street in intersections[i]:
                if street.name in streetUsage and (not bestStreet or streetUsage[street.name] > streetUsage[bestStreet]):
                    bestStreet = street.name

            if bestStreet:
                intersectionSchedule[i] = [(bestStreet, 1)]

        return intersectionSchedule