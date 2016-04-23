import unittest
from ShufflerBase import ShufflerBase
import random

class ShufflerBase_Test(unittest.TestCase):
    def setUp(self):
        self.testSize = 10
        self.testShuffler = ShufflerBase(self.testSize)

    def test_differenceFromOrigin(self):
        for i in range(self.testSize):
            self.assertEqual(self.testShuffler.differenceFromOrigin(i), 0)

        self.testShuffler.setDeck([0,1,4,3,2])
        self.assertEqual(self.testShuffler.differenceFromOrigin(2), 2)
        self.assertEqual(self.testShuffler.differenceFromOrigin(4), -2)
        self.testShuffler.setDeck([4,1,2,3,0])
        self.assertEqual(self.testShuffler.differenceFromOrigin(0), 4)
        self.assertEqual(self.testShuffler.differenceFromOrigin(4), -4)

    def test_totalDifferenceFromOrigin(self):
        self.assertEqual(self.testShuffler.totalDifferenceFromOrigin(), 0)
        self.testShuffler.shuffleOnce()
        self.assertEqual(self.testShuffler.totalDifferenceFromOrigin(), 0)

    def test_absoluteTotalDifferenceFromOrigin(self):
        self.assertEqual(self.testShuffler.absoluteTotalDifferenceFromOrigin(), 0)
        self.testShuffler.setDeck([4,1,2,3,0])
        self.assertEqual(self.testShuffler.absoluteTotalDifferenceFromOrigin(), 8)
        self.testShuffler.setDeck([0,1,2,4,3])
        self.assertEqual(self.testShuffler.absoluteTotalDifferenceFromOrigin(), 2)

    def test_differenceBetweenIndices(self):
        self.assertEqual(self.testShuffler.differenceBetweenIndices(0,3), 0)
        self.assertEqual(self.testShuffler.differenceBetweenIndices(1,4), 0)
        self.testShuffler.setDeck([4,1,2,3,0])
        self.assertEqual(self.testShuffler.differenceBetweenIndices(0,4), 0)
        self.testShuffler.setDeck([0,1,4,2,3])
        self.assertEqual(self.testShuffler.differenceBetweenIndices(2,4), -1)
        self.assertEqual(self.testShuffler.differenceBetweenIndices(2,3), 1)

    def test_absoluteTotalDifferenceBetweenIndices(self):
        self.assertEqual(self.testShuffler.absoluteTotalDifferenceBetweenIndices(), 0)
        self.testShuffler.setDeck([0,4,2,3,1])
        self.assertEqual(self.testShuffler.absoluteTotalDifferenceBetweenIndices(), 20)


if __name__ == '__main__':
    unittest.main()

