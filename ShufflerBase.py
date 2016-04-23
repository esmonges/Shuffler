import random

class ShufflerBase (object):
    """Base class for shuffler objects. Subclasses must implement
    the ShuffleOnce method"""

    def __init__(self, deckSize):
        self.deckSize = deckSize
        self.deck = range(deckSize)

    # shuffleOnce
    # Does one iteration of the shuffling action. In the base class,
    # this is just the standard random.shuffle function.
    def shuffleOnce(self):
        random.shuffle(self.deck)

    # differenceFromOrigin
    # Given an index i, calculates the difference of the
    # number at that index from its origin. Assumes that
    # the number itself is the original index.
    def differenceFromOrigin(self, i):
        return self.deck[i] - i

    # totalDifferenceFromOrigin
    # Determines the sum of the differences of the numbers
    # and their origins.
    # This turns out to always be 0. Guess I could have proven
    # that before writing this, but oh well!
    def totalDifferenceFromOrigin(self):
        totalDifference = 0
        for i in range(self.deckSize):
            totalDifference += self.differenceFromOrigin(i)
        return totalDifference

    # absoluteTotalDifferenceFromOrigin
    # Determines the sum of the absolute differences of the
    # numbers in the deck and their origins
    def absoluteTotalDifferenceFromOrigin(self):
        totalDifference = 0
        for i in range(self.deckSize):
            totalDifference += abs(self.differenceFromOrigin(i))
        return totalDifference

    # setDeck
    # For testing purposes. Given an array of numbers (the deck),
    # sets the deck and deckSize for the object to be the new deck.
    def setDeck(self, newDeck):
        self.deck = newDeck
        self.deckSize = len(newDeck)

    # differenceBetweenIndices
    # Figures out how far the elements at i and j have
    # moved relative to each other's original positions.
    # This boils down to taking the difference between the
    # original positions and the differnece between the new
    # positions, and taking the difference between those absolute values
    def differenceBetweenIndices(self, i, j):
        originalDifference = self.deck[i] - self.deck[j]
        newDifference = i - j
        return abs(originalDifference) - abs(newDifference)

    # absoluteTotalDifferenceBetweenIndices
    # Determines the net difference between elements relative
    # to each other. Achieved by summing the differenceBetweenIndices
    # for each element compared to each other element
    def absoluteTotalDifferenceBetweenIndices(self):
        totalDifference = 0
        for i in range(self.deckSize):
            for j in range(self.deckSize):
                # Note that differenceBetweenIndices(i,j) is always 0
                # for i == j
                totalDifference += abs(self.differenceBetweenIndices(i,j))
        return totalDifference

    def differences(self):
        return {
            'totalOriginDifference': self.absoluteTotalDifferenceFromOrigin(),
            'totalIndexDifference': self.absoluteTotalDifferenceBetweenIndices()
        }

