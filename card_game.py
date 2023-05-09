import random
from argparse import ArgumentParser
import sys
import re

def deck(filePath):
    """ Creates a list of cards from text file (Alisha, deck Function: with statement)
    Args: 
        filePath(str): path to text file containing card names 
    Returns: 
        deck_list(list): list of cards
    """
    deck_list = []
    with open(filePath, "r", encoding = "utf-8") as file:
        deck_list = []
        for line in file: 
            deck_list.append(line.strip())
    return deck_list

class Card:
    '''
    This card game class represents a playing card
   
    Attributes:
     - card_str (str): the string that represents a card
    '''
    def __init__(self, card):
        '''
        initializes a Card Object(Lima)
       
        Args:
         - card (str): a string that represents a card
        '''
        self.card_str = card
        
    def card_value_suit(self):
        '''Uses regex to group values and suits(Yasmin, regex, sequence 
        unpacking).
        
        Returns:
            value(str): card number
            suit(str): card suit
        '''
    
        regex = r"(?P<value>\d+|[A-Z])\s(?P<suit>[a-z]+)"
        match = re.search(regex, self.card_str)
        value, suit = match.group("value"), match.group("suit")
        return value, suit
    
    def card_name(self):
        '''Specifies card name based on value (Yasmin, sequence unpacking).
        Returns:
            name(str): name of the card
        '''
        if self.card_value_suit()[0] == "J":
            name = f"Jack of {self.card_value_suit()[1]}"
        elif self.card_value_suit()[0] == "Q":
            name = f"Queen of {self.card_value_suit()[1]}"
        elif self.card_value_suit()[0] == "K":
            name = f"King of {self.card_value_suit()[1]}"
        elif self.card_value_suit()[0] == "A":
            name = f"Ace of {self.card_value_suit()[1]}"
        else:
            name = f"{self.card_value_suit()[0]} of {self.card_value_suit()[1]}"
        return name
    
    def __str__(self):
        '''
        Returns the string representation of the card 
        (Lima, informal representation using magic method)
       
        Returns:
         - str: the string that represents a card

        '''
        return f"{self.card_str}"

class Player:
    def __init__(self, name):
        self.name = name

    def choose_card(self, table):
        random_card = random.choice(table.outer_cards)
        return random_card

class Table:
    def __init__(self, card_deck, pulled_cards, middle_cards, homes):
        """Set attributes. (Rida, list comprehension)
        Args:
            card_deck (list of str): list of cards
            pulled_cards (list of str): list of cards that were pulled
            middle_cards (list of str): list of cards in the middle
            homes (dict of str: int): players' names and their scores
        """
        self.outer_cards = [x for x in card_deck if x not in pulled_cards if x not in middle_cards]
        self.middle_cards = middle_cards.copy()
        self.homes = homes.copy()
    
    def __str__(self):
        """returns an informal repsresentation of the board (Hanan, informal representation) """
        return(f"Middle Cards: {self.middle_cards} Homes: {self.homes}")
    
class Game:
    """A game of Injera Bewatt """
    def __init__(self, players, deckList = deck ("card_deck.txt")):
        """ Set attributes (Alisha, Game class __init__: optional parameter)
        Args: 
            players(list of Player): list of players 
            deckList(list of str): list of cards
        Side effects:
            sets attributes 
        """
        self.players = players
        self.homes = {p.name: 0 for p in players}
        self.middle_cards = random.sample(deckList, 4)
        self.pulled_cards = list()
    
    def table(self):
        """Return an instance of Table using this class' attributes 
        as arguments (Rida, composition of two custom classes)
        """
        return Table(deck("card_deck.txt"), self.pulled_cards, self.middle_cards, self.homes)
    
    def game_over(self, table):
        if table.outer_cards:
            return False
        else:
            return True
    
    def turn(self, player):
        """"A player's turn.
        Args:
            player (Player): a player
        """
        table = self.table()
        
        while self.game_over(table) == False:
            card = Card(player.choose_card(table))
            self.pulled_cards.append(card.card_str)
            
            print(table)
            print (f"{player.name}, you pulled a {card.card_name()}!")
            
            see_match = input("Do you see a match? Yes/No. ")
            if see_match.lower() == 'yes':
                possible_match = Card(input("What card is the match? " + 
                    "(Format like this: '3 diamonds' or 'A spades')" + 
                    "choose wisely, you only get one chance. ").strip())
                
                if card.card_value_suit()[0] == possible_match.card_value_suit()[0] and possible_match.card_str in table.middle_cards:
                    print ("Match successful! Both cards will be added to your home.\n")
                    self.homes[player.name] += 2
                    self.middle_cards.remove(possible_match.card_str)
                    return
                
                else:
                    print("Match unsuccessful. Your card will be added to the middle.\n")
                    self.middle_cards.append(card.card_str)
                    return
                
            elif see_match.lower() == "no":
                print("Your turn is over, your card will be added to the middle.\n")
                self.middle_cards.append(card.card_str)
                return 
    
    def play_game(self):
        """Plays the game while the game is not over
        Side effects: 
            prints who the winner is and the outcome of the game when it's over (Hanan, key function: lambda)
        """
        table = self.table()
        
        loop = -1
        while self.game_over(table) == False:
            loop += 1
            player = self.players[loop % len(self.players)]
            self.turn(player)
        
        print(f"Game Over! {table}")   
        winner = max(table.homes, key=lambda name: table.homes[name])         
        print(f"The winner is {winner}!")
    
def main(playersList):
    """Set up and play a game of Injera be Wet"""
    players = [Player(name) for name in playersList]
    game = Game(players)
    game.play_game()
    
def parse_args(argList):
    '''
    Parses the command-line arguments(Lima, ArgumentParser)
   
    Args:
     - arglist (list of str): arguments from the command line.
   
    Returns:
     - namespace: the parsed arguments, as a namespace.
    '''
    parser = ArgumentParser()
    parser.add_argument('names', nargs="*", help = 'player names')
    return parser.parse_args(argList)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.names)