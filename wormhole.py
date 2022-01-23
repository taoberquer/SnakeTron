from special import Special

class Wormhole:
    def __init__(self, specials, size):
        self.first = Special(specials, (0, 0, 150), size)
        self.sec = Special(specials, (0, 0, 150), size)
