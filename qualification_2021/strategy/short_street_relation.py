class ShortStreetRelationStrategy:

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
            intersectionStreets = {} # Street Name : Length
            intersectionStreetsLength = 0

            for street in intersections[i]:
                if street.name in streetUsage:
                    intersectionStreets[street.name] = street.time
                    intersectionStreetsLength += street.time


            intersectionStreetsPercentage = {}
            for streetName in intersectionStreets:
                percentage = 1 / (street.time*1.0 / intersectionStreetsLength)
                intersectionStreetsPercentage[streetName] = percentage

                if i not in intersectionSchedule:
                    intersectionSchedule[i] = []

                intersectionSchedule[i].append([streetName, max(int(percentage), 1)])
            
            # print(intersectionStreetsPercentage)

        return intersectionSchedule