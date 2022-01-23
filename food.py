from special import Special

class Food(Special):
    def __init__(self, specials, size):
        Special.__init__(self, specials, (202, 0, 42), size)