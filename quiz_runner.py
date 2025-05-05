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
        
# displayed text, size, and their color
        intro_text = "W E L C O M E   T O   T H E   B R A I N   R O U L E T T E"
        colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", 
                 "#0000FF", "#4B0082", "#9400D3", "#FF1493",
                 "#00FFFF", "#7CFC00", "#FFD700", "#FF4500"]
        
# animation per letter with colors
        self.animated_chars = []
        x_pos = 100
        y_pos = 200
        
        for kyle, charot in enumerate(intro_text):
            if charot == " ":
                x_pos += 15  
                continue
                
            color = colors[kyle % len(colors)]
            char_id = self.intro_canvas.create_text(
                x_pos, y_pos, text=charot, 
                font=("Impact", 28, "bold"), 
                fill=color,
                state=tk.HIDDEN
            )
            self.animated_chars.append((char_id, x_pos, y_pos, color))
            x_pos += 30
            
 # Implementation of the animation program
        self.current_char_index = 0
        self.animate_next_char()
    
    def animate_next_char(self):
        """Animate the next character in the intro"""
        if self.current_char_index < len(self.animated_chars):
            char_id, x, y, color = self.animated_chars[self.current_char_index]
            
 # to make the intro visible to the app
            self.intro_canvas.itemconfig(char_id, state=tk.NORMAL)
            
            # Bounce effect
            for kyle in range(5):
                self.intro_canvas.move(char_id, 0, -5)
                self.root.update()
                time.sleep(0.03)
            for kyle in range(5):
                self.intro_canvas.move(char_id, 0, 5)
                self.root.update()
                time.sleep(0.03)
            
            self.current_char_index += 1
            self.root.after(50, self.animate_next_char)
        else:
            # completed animation and continue button
            self.root.after(1000, self.show_continue_button)
    
            