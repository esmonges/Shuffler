from ShufflerBase import ShufflerBase
import random

class CutShuffler (ShufflerBase):
    def __init__(self, deckSize, centerTolerance):
        super(CutShuffler, self).__init__(deckSize)
        self.centerTolerance = centerTolerance

    # shuffleOnce
    # Does one iteration of the shuffling action. For a cut shuffler,
    # this is cutting the deck in half at a random index near the center
    # within some tolerance (i.e. +/- 5), and then sawpping the halfs.
    def shuffleOnce(self):
        center = self.deckSize // 2
        adjustment = random.randrange(-self.centerTolerance, self.centerTolerance)
        center += adjustment
        firsthalf = self.deck[:center]
        secondhalf = self.deck[center:]
        self.deck = secondhalf + firsthalf