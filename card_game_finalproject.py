import random
from argparse import ArgumentParser
import sys
import re

def deck(filePath):
    deck_list = []
    with open(filePath, "r", encoding = "utf-8") as file:
        # INSERT regex w/capturing groups for the number/letter + the name
        # or maybe not here since we're not doing dict anymore
        deck_list = []
        for line in file:
            deck_list.append(line.strip())
    return deck_list


class Player:
    def __init__(self, name):
        self.name = name
        self.home = list()
        self.card_value = ""
        self.card_suit = ""

    def choose_card(self, table):
        """Represents the player choosing a card from the outer circle
        Args:
            table (Table): represents the current state of the table/game
        Side Effects:
            Updates the card_value and card_suit attributes with the card that was pulled.
            Prints table.
            Prints message to user about what card they pulled.
        Returns:
            random_card (str): the card the user pulled
        """
        random_card = random.choice(table.outer_cards) # ex. "3 spades"
        
        regex = r"(?P<value>\d+|[A-Z])\s(?P<suit>[a-z]+)"
        match = re.search (regex, random_card)

        self.card_value = match.group("value")
        self.card_suit = match.group("suit")
        
        print(table) # prints current state of the table as defined in Table class (so they know what's in the middle & maybe num of turns?)
        print (f"{self.name}, you pulled a {self.card_value} of {self.card_suit}!")
        return random_card

class Table:
    """Represents the current state of the game, AKA what's on the table
    
    Attributes:
        pulled_cards (list of str): cards that were already pulled
        placed_cards (list of str): cards that were added to the middle
        outer_cards (list of str): cards remaining in the outer circle
        middle_cards (list of str):
        homes (dict of str: int):
    """

class Game:
    """A game of Injera be Wet"""
    
def main(cardsList, playersList):
    """Set up and play a game of Injera be Wet"""
    
    
def parse_args(argList):
    """Parse command-line arguments"""

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    # call the main function w/all required arguments, but with 'args.' preceding it
    # basically ur calling the main function with the command line arguments