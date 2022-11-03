

# import libraries and modules
from random import randint
from xml.dom.expatbuilder import parseString
# main class is game
# characteristics
# pass
class BigGame:
    def __init__(self,points,characters,NPC,level,speed):
        self.points=points
        self.characters=characters
        self.NPC=NPC
        self.level=level
        self.speed=speed
    def score(value,multipliers,good,bad):
        value.good=good
        value.bad=bad
        value.multipliers=multipliers
        pass
# subclass is RPS
# characteristics for RPS
# pass
class RPS(BigGame):
    pass