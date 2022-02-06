from special import Special


class Wall(Special):
    def __init__(self, specials, size, random=True, x=0, y=0):
        Special.__init__(self, specials, (173, 134, 0), size, random, x, y)
