import random

class Card:
    """The dealer draws a card that contains a random number between 1 and 13. 
    
    He keeps track of the player points, assigns 100 points if the player guessed right, or substracts 75 points if the player guessed wrong.
    
    Attributes:
        .    
    """

def __init__(self):
    """Constructs a new instance of Card
    
    Args:
        self (Card): an instance of Card
    """

    self.value = 0
    self.points = 0
    self.previous_value = 0
    self.guess = ''
    


    
def draw(self):
    """Generates a random value between 1 and 13 and calculates points based on player's guess.txt
    Args:
        self (Card): An instance of Card
    
    """

    self.previous_value = random.randint(1, 13)
    print(f'The card is {self.previous_value}')
    guess = input('Higher or lower [h/l]')
    self.value = random.randint(1, 13)
    if self.value > self.previous_value and guess == 'h':
        self.points = 100
    elif self.value < self.previous_value and guess == 'l':
        self.points = 100
    elif self.value > self.previous_value and guess == 'l':
        self.points = -75
    elif self.value < self.previous_value and guess == 'h':
        self.points = -75
    else:
        self.points = 0
