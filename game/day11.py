
class Lizard:
    def __init__(self, slimey, rough, tounge, eyes):
        self.slimey=slimey
        self.tounge=tounge
        self.rough=rough
        self.eyes=eyes
        pass
    def crawl(legs,slow, moves, climb, distance):
        legs.slow=slow
        legs.moves=moves
        legs.climb=climb
        legs.distance=distance
        pass

p1=Lizard
slimey=print("i am slimey")
rough=print("i am rough")
tounge=print('i have a touge')
eyes=print('i have eyes')
slow=print('i am slow')
moves=print('i am slow')
climb=print('i can climb')
distance=print('i move distance')

class Iguana(Lizard):
    def __init__(self,slimey,regeneration):
        super().__init__(slimey)
        self,regeneration=regeneration
    def swim(self):
        print('paddle paddle...')
    pass
