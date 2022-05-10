import random
from game.card import Card
"""
    Update the code and the comments as you change the code for your game.  You will be graded on following the
    Rules listed and your program meets all of the Requirements found on 
    https://byui-cse.github.io/cse210-course-competency/abstraction/materials/hilo-specification.html
"""



class Dealer:
    """A person who directs the game. 
    The responsibility of a Dealer is to control the sequence of play and draw cards.
    Attributes:
        is_playing (boolean): Whether or not the game is being played.
    """

    def __init__(self):
        self.number_card = range(1, 13)
        self.card = random.choice(self.number_card)
        self.points = 0
        self.total_score = 300
        self.choice = Card()
        self.selection = False

    def start_game(self):
        
        while self.choice.play_again and self.total_score > 0:
            print('Welcome to Hilo game!')
            self.do_outputs()
            self.do_updates()
            self.get_points()
            self.do_outputs()

            while True:
                looping = input('Play again? [y/n]: ').lower()
                if looping == 'y':
                    self.choice.play_again = True
                    print('Next game it is!')
                    break
                elif looping == 'n':
                    self.choice.play_again = False
                    break
                else:
                    print('Invalid input, try again!')
            print('')  
        pass

  

    def get_points(self):

        if self.selection == self.choice.guess:
            self.total_score += 100
        else:
            self.total_score -= 75
      
    def do_updates(self):

        
        self.points = self.card
        print(f'The card is: {self.points}')
        
        
        self.choice.get_input()
        self.card = random.choice(self.number_card)
        print(f'The Next card: {self.card}')
        if self.card > self.points:
            self.selection = True
        else:
            self.selection = False


    def do_outputs(self): 
        print(f'Your score is: {self.total_score}')
        pass
