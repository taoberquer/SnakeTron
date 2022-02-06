from special import Special


class Food(Special):
    def __init__(self, specials, size, random=True):
        Special.__init__(self, specials, (202, 0, 42), size, random)
