#!/usr/bin/env python

import time

#from example_2021 import Example2021
#from example_2021.strategy import BaseStrategy

from qualification_2021 import Qualification2021
from qualification_2021 import BaseStrategy, FirstStreetStrategy, OneSecondStrategy, TenSecondsStrategy, MostUsedStreetStrategy, UsedStreetsStrategy, StreetRelationStrategy, ShortStreetRelationStrategy, StreetCarLengthRelationStrategy, StreetRelationReversedStrategy, StreetCarLengthRelationReversedStrategy

CHALLENGE=Qualification2021
STRATEGY=StreetCarLengthRelationReversedStrategy
INPUT_FILES= ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']

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