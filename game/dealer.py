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
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.points = 0
        self.total_score = 300
        

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            #self.get_inputs()
            self.do_updates()
            self.do_outputs()

    #def get_inputs(self):
        """Ask the user if they want to continue playing.

        Args:
            self (Dealer): An instance of Dealer.
        """



    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        card.draw()
        self.points = card.points
        self.total_score += self.points
     
        


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 
        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        next_card = self.card.value

        print(f'Next card was: {next_card}')
        print(f'Your score is: {self.total_score}')
        while True:
                looping = input('Play again? [y/n]: ').lower()
                if looping == 'y':
                    self.is_playing = True
                    print('Next game it is!')
                    break
                elif looping == 'n':
                    self.is_playing = False
                    print('Thanks for playing Hilo')
                    break
                else:
                    print('Invalid input, try again!')
        print('')  
        pass
