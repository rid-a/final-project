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