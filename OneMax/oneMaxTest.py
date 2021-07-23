import unittest
import datetime
from OneMax import genetic

class OneMaxTests(unittest.TestCase):
    def test(self , length = 100):
        geneset = [ 0 , 1 ]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate , startTime)

        def fnGetFitness(genes):
            return getFitness(genes)

        optimalFitness = length
        best = genetic.get_best(fnGetFitness , length , optimalFitness , geneset , fnDisplay)

        self.assertEqual(best.Fitness , optimalFitness)


def getFitness(genes):
    return genes.count(1)


def display(candidate , startTime):
    timeD = datetime.datetime.now() - startTime
    print("{0}...{1}\t{2:3.2f}\t{3}".format(
            ''.join(map(str, candidate.Genes[:15])),
            ''.join(map(str, candidate.Genes[-15:])),
            candidate.Fitness,
            str(timeD)))


if __name__ == "__main__":
    unittest.main()
