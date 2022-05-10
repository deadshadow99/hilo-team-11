class Card:
    """The dealer draws a card that contains a random number between 1 and 13. 
    
    He keeps track of the player points, assigns 100 points if the player guessed right, or substracts 75 points if the player guessed wrong.
    
    Attributes:
        .    
    """

    def __init__(self):

      self.guess = True
      self.play_again = True


    def get_input(self):
        
        while True:
            answer = input("Higher or lower? [h/l]: ").lower()

            if answer == 'h':
                self.guess = True
                break
            elif answer == 'l':
                self.guess = False
                break
            else:
                print("Invalid input, try again.")
