import random
from argparse import ArgumentParser
import sys
import re

def deck(filePath):
    deck_list = []
    with open(filePath, "r", encoding = "utf-8") as file:
        deck_list = []
        for line in file: 
            deck_list.append(line.strip())
    return deck_list

class Card:
    def __init__(self, card):
        self.card_str = card
        
    def card_value_suit(self):
        regex = r"(?P<value>\d+[A-Z])\s(?P<suit>[a-z]+)"
        match = re.search(regex, self.card_str)
        value, suit = match.group ("value"), match.group("suit")
        return value, suit
    
    def card_name(self):
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
        return f"{self.card_str}"

class Player:
    def __init__(self, name):
        self.name = name

    def choose_card(self, table):
        random_card = random.choice(table.outer_cards)
        return random_card

class Table:
    def __init__(self, card_deck, pulled_cards, middle_cards, homes):
        self.outer_cards = [x for x in card_deck if x not in pulled_cards if x not in middle_cards]
        self.middle_cards = middle_cards.copy() # a list of str
        self.homes = homes.copy()
    
    def __str__(self):
        """returns an informal repsresentation of the board """
        return(f"Middle Cards: {self.middle_cards} Homes: {self.homes}")
    
class Game:
    """A game of Injera Bewatt"""
    def __init__(self, players, deckList = deck ("card_deck.txt")):
        self.players = players
        self.homes = {p.name: 0 for p in players}
        self.middle_cards = random.sample(deckList, 4)
        self.pulled_cards = list()
    
    def table(self):
        """Return the table aka an instance of the table class, using this class' attributes as arguments"""
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