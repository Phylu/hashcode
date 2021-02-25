class BaseStrategy:

    def run(self, inputFile):
        pizzaIterator = 0
        pizzas = []
        teamCounter = 0

        for i in range(inputFile.teamsByNumber(4)):
            if inputFile.numberOfPizzas - 4 < pizzaIterator:
                break
            pizzas.append([4, pizzaIterator, pizzaIterator + 1, pizzaIterator + 2, pizzaIterator + 3])
            pizzaIterator = pizzaIterator + 4
            teamCounter += 1

        for i in range(inputFile.teamsByNumber(3)):
            if inputFile.numberOfPizzas - 3 < pizzaIterator:
                break
            pizzas.append([3, pizzaIterator, pizzaIterator + 1, pizzaIterator + 2])
            pizzaIterator = pizzaIterator + 3
            teamCounter += 1

        for i in range(inputFile.teamsByNumber(2)):
            if inputFile.numberOfPizzas - 2 < pizzaIterator:
                break
            pizzas.append([2, pizzaIterator, pizzaIterator + 1])
            pizzaIterator = pizzaIterator + 2
            teamCounter += 1

        return teamCounter, pizzas