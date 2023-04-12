class Player:
    """Both computer and human players
    Attributes: 
        name(str) - name of player
        home(int) - num of points player has
    """
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
    
