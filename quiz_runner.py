import tkinter as tk
import math
from tkinter import messagebox
import random
import time
from collections import defaultdict
import json  # Added for reading the questions file

class BrainRouletteGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Brain Roulette Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#000000")
        
        # information from the user
        self.player = {
            "name": "",
            "gender": "",
            "age": 0,
            "section": "",
            "year": ""
        }
        
        # Data of the game
        self.all_questions = defaultdict(list)
        self.current_questions = []
        self.current_question = None
        self.score = 0
        self.attempts = 3
        self.current_level = "Easy"
        self.questions_answered_in_level = 0
        
        # Wheel animation variables
        self.wheel_categories = ["Math", "Science", "History", "English", "General"]
        self.wheel_colors = ["#FF5733", "#33FF57", "#3357FF", "#F3FF33", "#FF33F5"]
        self.wheel_spinning = False
        self.wheel_angle = 0
        
        # Show colorful intro animation
        self.show_intro_animation()
    
    def show_intro_animation(self):
        """Show animated intro text"""
        self.animated_chars = []
        self.intro_canvas = tk.Canvas(self.root, width=800, height=400, bg="#000000", highlightthickness=0)
        self.intro_canvas.pack(pady=50)
        
        intro_part1 = "WELCOME TO THE"
        intro_part2 = "BRAIN ROULETTE"
        
        colors = ["#FF0000", "#FF7000", "#FFFF00", "#00FF00", 
                  "#0000FF", "#4B0082", "#9400D3", "#FF1493",
                  "#00FFFF", "#7CFC00", "#FFD700", "#FF4500"]
        
        # Animate "WELCOME TO THE"
        x_pos = 100
        y_pos = 180
        for i, char in enumerate(intro_part1):
            if char == " ":
                x_pos += 15
                continue
            color = colors[i % len(colors)]
            char_id = self.intro_canvas.create_text(
                x_pos, y_pos, text=char,
                font=("Impact", 28, "bold"),
                fill=color,
                state=tk.HIDDEN
            )
            self.animated_chars.append((char_id, x_pos, y_pos, color))
            x_pos += 30
        
        # Animate "BRAIN ROULETTE"
        x_pos = 100
        y_pos = 250
        for i, char in enumerate(intro_part2):
            if char == " ":
                x_pos += 30
                continue
            color = colors[(i + len(intro_part1)) % len(colors)]
            char_id = self.intro_canvas.create_text(
                x_pos, y_pos, text=char,
                font=("Impact", 36, "bold"),
                fill=color,
                state=tk.HIDDEN
            )
            self.animated_chars.append((char_id, x_pos, y_pos, color))
            x_pos += 40

        self.current_char_index = 0
        self.animate_next_char()

    def animate_next_char(self):
        """Animate the next character in the intro"""
        if self.current_char_index < len(self.animated_chars):
            char_id, x, y, color = self.animated_chars[self.current_char_index]
            
            # Make character visible
            self.intro_canvas.itemconfig(char_id, state=tk.NORMAL)
            
            # Bounce effect
            for i in range(5):
                self.intro_canvas.move(char_id, 0, -5)
                self.root.update()
                time.sleep(0.03)
            for i in range(5):
                self.intro_canvas.move(char_id, 0, 5)
                self.root.update()
                time.sleep(0.03)
            
            self.current_char_index += 1
            self.root.after(50, self.animate_next_char)
        else:
            # Animation complete, show continue button
            self.root.after(1000, self.show_continue_button)
    
    def show_continue_button(self):
        """Show continue button after intro"""
        tk.Button(self.root, text="Continue to Game", 
                 command=self.load_game_content,
                 bg="#FF0000", fg="white",
                 font=("Arial", 14, "bold"),
                 relief="raised", bd=5).pack(pady=30)
    
    def load_game_content(self):
        """Load game content after intro"""
        self.load_questions()
        self.show_registration_screen()
    
    def clear_screen(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def load_questions(self):
        """Load questions from created_questions.txt file"""
        try:
            with open("created_questions.txt", "r") as file:
                questions_data = json.load(file)
                
                for level in ["Easy", "Medium", "Hard"]:
                    if level in questions_data:
                        self.all_questions[level] = questions_data[level]
                    else:
                        messagebox.showwarning("Warning", f"No {level} questions found in the file")
                        
                # If no questions were loaded at all
                if not self.all_questions:
                    messagebox.showerror("Error", "No questions found in the file. Using default questions.")
                    self.load_default_questions()
                    
        except FileNotFoundError:
            messagebox.showerror("Error", "created_questions.txt file not found. Using default questions.")
            self.load_default_questions()
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid format in created_questions.txt. Using default questions.")
            self.load_default_questions()
    
    def load_default_questions(self):
        """Load default questions if the file is not available"""
        # readily available questions if the file is empty
        # Easy questions
        self.all_questions["Easy"].extend([
            {"category": "Math", "question": "What is 2 + 2?", "answer": "4"},
            {"category": "Science", "question": "What is the chemical symbol for water?", "answer": "H2O"},
            {"category": "History", "question": "Who was the first president of the United States?", "answer": "George Washington"},
            {"category": "English", "question": "What is the past tense of 'run'?", "answer": "ran"},
            {"category": "General", "question": "How many colors are in a rainbow?", "answer": "7"}
        ])
        
        # Medium questions
        self.all_questions["Medium"].extend([
            {"category": "Math", "question": "What is 15 × 6?", "answer": "90"},
            {"category": "Science", "question": "What planet is known as the Red Planet?", "answer": "Mars"},
            {"category": "History", "question": "In what year did World War II end?", "answer": "1945"},
            {"category": "English", "question": "What literary device compares two things using 'like' or 'as'?", "answer": "Simile"},
            {"category": "General", "question": "What is the capital of France?", "answer": "Paris"}
        ])
        
        # Hard questions
        self.all_questions["Hard"].extend([
            {"category": "Math", "question": "What is the square root of 144?", "answer": "12"},
            {"category": "Science", "question": "What is the atomic number of gold?", "answer": "79"},
            {"category": "History", "question": "Who wrote the Declaration of Independence?", "answer": "Thomas Jefferson"},
            {"category": "English", "question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
            {"category": "General", "question": "What is the largest ocean on Earth?", "answer": "Pacific"}
        ])
        
    def show_registration_screen(self):
        """Show player registration form"""
        self.clear_screen()
        
        # Title
        tk.Label(self.root, text="Player Registration", font=("Arial", 24, "bold"), bg="#000000", fg="#FFFFFF").pack(pady=20)
        
        # Registration frame
        reg_frame = tk.Frame(self.root, bg="#000000")
        reg_frame.pack(pady=20)
        
        # Name
        tk.Label(reg_frame, text="Full Name:", font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(reg_frame, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Gender
        tk.Label(reg_frame, text="Gender:", font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(reg_frame, text="Male", variable=self.gender_var, value="Male", bg="#000000", fg="#FFFFFF", selectcolor="#000000").grid(row=1, column=1, padx=10, pady=5, sticky="w")
        tk.Radiobutton(reg_frame, text="Female", variable=self.gender_var, value="Female", bg="#000000", fg="#FFFFFF", selectcolor="#000000").grid(row=1, column=1, padx=10, pady=5, sticky="e")
        
        # Age
        tk.Label(reg_frame, text="Age:", font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.age_entry = tk.Entry(reg_frame, font=("Arial", 12))
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Section
        tk.Label(reg_frame, text="Section:", font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.section_entry = tk.Entry(reg_frame, font=("Arial", 12))
        self.section_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Year
        tk.Label(reg_frame, text="Year:", font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.year_entry = tk.Entry(reg_frame, font=("Arial", 12))
        self.year_entry.grid(row=4, column=1, padx=10, pady=5)
        
        # Submit button
        tk.Button(self.root, text="Start Game", command=self.register_player, 
                 bg="#4CAF50", fg="white", font=("Arial", 14, "bold"),
                 relief="raised", bd=5).pack(pady=20)