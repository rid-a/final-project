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
