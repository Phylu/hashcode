class StreetRelationStrategy:

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
            intersectionStreets = {} # Street Name : Number of Cars
            intersectionCarCount = 0

            for street in intersections[i]:
                if street.name in streetUsage:
                    intersectionStreets[street.name] = streetUsage[street.name]
                    intersectionCarCount += streetUsage[street.name]

            for streetName in intersectionStreets:
                percentage = streetUsage[streetName]*1.0 / intersectionCarCount

                if i not in intersectionSchedule:
                    intersectionSchedule[i] = []

                intersectionSchedule[i].append([streetName, max(int(percentage * 10), 1)])

        return intersectionSchedule