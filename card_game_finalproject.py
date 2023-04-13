import random
class Player:
    """Both computer and human players
    Attributes: 
        name(str) - name of player
        home(int) - num of points player has
        score(int)- the score of the player
    """
    def __init__(self, name):
        self.name = name
        self.home = []
        self.score = 0
        
    def choose_card(filepath):
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                my_card = random.choice(line.strip())
                return my_card
            
    def update_home(self, points):
        '''
        Updates the score of the player by adding he given points
        
        Args:
         - points(int): The number of points that should be added to
           the score borad
        '''
        score += points
    
        
class HumanPlayer(Player):
    """human player playing game

    Args:
        Player (class): inherits everything the player class has
    """
class ComputerPlayer(Player):
    """computer player playing game

    Args:
        Player (class): inherits everything the player class has
    """

class Table():
    """Information on what's on the table 
    Attributes: 
        remaining_cards(list of str)- cards still left upside down on table
        middle- cards facing up 

    """
class Game():
    """ Staging game play 
    Attributes: 
        players(list)- list of player instances 
        home(int)- score of each player

    """
def main(): 
    """Initializing the game 
    """
    
