#!/usr/bin/env python

import time

from example_2021 import Example2021
from example_2021.strategy import BaseStrategy

CHALLENGE=Example2021
STRATEGY=BaseStrategy
INPUT_FILES= ['a_example', 'b_little_bit_of_everything.in', 'c_many_ingredients.in', 'd_many_pizzas.in', 'e_many_teams.in']

if __name__ == '__main__':

    maxFilenameLength = max(map(len, INPUT_FILES)) + 1

    overallStartTime = time.time()

    for inputFile in INPUT_FILES:
        challengeStartTime = time.time()
        filename = '/'.join([CHALLENGE.__str__(), 'input', inputFile])

        challenge = CHALLENGE(STRATEGY, filename)
        challenge.run()

        print("{}: {} seconds".format(inputFile.ljust(maxFilenameLength), time.time() - challengeStartTime))

    print("{}: {} seconds".format('Overall'.ljust(maxFilenameLength), time.time() - overallStartTime))