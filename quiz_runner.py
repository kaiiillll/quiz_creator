# list all the import needed for the game
import tkinter as tk
from tkinter import messagebox
import random
import time
from collections import defaultdict

# the class for brain roulette and design
class BrainRouletteGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Roulette Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#000000")
        
# needed info from the user to know the person
        self.player = {
            "name": "",
            "gender": "",
            "age": 0,
            "section": "",
            "year": ""
        }

# game data to disrupt the user if 3 more attempts
        self.all_questions = defaultdict(list)
        self.current_questions = []
        self.current_question = None
        self.score = 0
        self.attempts = 3
        self.current_level = "Easy"
        self.questions_answered_in_level = 0

