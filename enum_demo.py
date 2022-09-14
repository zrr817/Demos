'''
This is a demo script to showcase how to use enums
This will generate a random royal of any suit
'''

# Imports
import random

from enum import Enum

class Cards(Enum):
    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4
    
    @classmethod
    def suit(cls):
        return cls(random.randint(1,4))
    
class Values(Enum):
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14
    
    @classmethod
    def generate_value(cls):
        return cls(random.randint(11,14))
    
if __name__ == '__main__':
    print(Values.generate_value(), 'of', Cards.suit())
