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

# animation for wheels "very cute"
        self.wheel_categories = ["Math", "Science", "History", "English", "General"]
        self.wheel_colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F5"]
        self.wheel_spinning = False
        self.wheel_angle = 0
        
# intro animation of the wheels
        self.show_intro_animation()
    
    def show_intro_animation(self):
        """Show colorful 'BRAIN ROULETTE' intro animation"""
        self.clear_screen()

# sizes for wheel animation
        self.intro_canvas = tk.Canvas(self.root, width=800, height=400, bg="#000000", highlightthickness=0)
        self.intro_canvas.pack(pady=50)