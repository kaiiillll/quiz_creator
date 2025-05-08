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
def register_player(self):
        """Register player information"""
        self.player["name"] = self.name_entry.get().strip()
        self.player["gender"] = self.gender_var.get()
        
        try:
            self.player["age"] = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return
        
        self.player["section"] = self.section_entry.get().strip()
        self.player["year"] = self.year_entry.get().strip()
        
        if not self.player["name"]:
            messagebox.showerror("Error", "Please enter your name")
            return
        
        self.show_main_menu()
        
def show_main_menu(self):
        """Show the main menu screen"""
        self.clear_screen()
        
        # Title
        tk.Label(self.root, text="BRAIN ROULETTE", font=("Impact", 36, "bold"), bg="#000000", fg="#FF0000").pack(pady=30)
        
        # Player info
        tk.Label(self.root, text=f"Player: {self.player['name']}", font=("Arial", 14), bg="#000000", fg="#FFFFFF").pack()
        tk.Label(self.root, text=f"Level: {self.current_level}", font=("Arial", 14), bg="#000000", fg="#FFFFFF").pack()
        tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 14), bg="#000000", fg="#FFFFFF").pack(pady=10)
        
        # Menu buttons
        button_frame = tk.Frame(self.root, bg="#000000")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Spin Wheel", command=self.spin_wheel, 
                 bg="#FF5733", fg="white", font=("Arial", 14, "bold"),
                 width=15, relief="raised", bd=5).grid(row=0, column=0, padx=10, pady=10)
        
        tk.Button(button_frame, text="Instructions", command=self.show_instructions, 
                 bg="#33FF57", fg="black", font=("Arial", 14, "bold"),
                 width=15, relief="raised", bd=5).grid(row=0, column=1, padx=10, pady=10)
        
        tk.Button(button_frame, text="View Profile", command=self.show_profile, 
                 bg="#3357FF", fg="white", font=("Arial", 14, "bold"),
                 width=15, relief="raised", bd=5).grid(row=1, column=0, padx=10, pady=10)
        
        tk.Button(button_frame, text="Exit Game", command=self.exit_game, 
                 bg="#FF33F5", fg="white", font=("Arial", 14, "bold"),
                 width=15, relief="raised", bd=5).grid(row=1, column=1, padx=10, pady=10)
        
# wheel animations and buttons 
def spin_wheel(self):
        """Show the wheel spinning animation and select a category"""
        self.clear_screen()
        
        # Title
        tk.Label(self.root, text="Spin the Wheel!", font=("Arial", 24, "bold"), bg="#000000", fg="#FFFFFF").pack(pady=20)
        
        # Wheel canvas
        self.wheel_canvas = tk.Canvas(self.root, width=500, height=500, bg="#000000", highlightthickness=0)
        self.wheel_canvas.pack()
        
        # Draw initial wheel
        self.draw_wheel()
        
        # Spin button
        tk.Button(self.root, text="SPIN!", command=self.start_wheel_spin, 
                 bg="#FF0000", fg="white", font=("Arial", 16, "bold"),
                 relief="raised", bd=5).pack(pady=20)
def draw_wheel(self, angle=0):
        """Draw the wheel at the specified angle"""
        self.wheel_canvas.delete("all")
        
        center_x, center_y = 250, 250
        radius = 200
        
        # Draw wheel segments
        for i in range(len(self.wheel_categories)):
            start_angle = angle + (i * 360/len(self.wheel_categories))
            end_angle = angle + ((i+1) * 360/len(self.wheel_categories))
            
            # Draw segment
            self.wheel_canvas.create_arc(
                center_x-radius, center_y-radius, 
                center_x+radius, center_y+radius,
                start=start_angle, extent=end_angle-start_angle,
                fill=self.wheel_colors[i], outline="white"
            )
# position of the text
            mid_angle = (start_angle + end_angle) / 2
            text_radius = radius * 0.7
            text_x = center_x + text_radius * 0.7 * math.cos(math.radians(mid_angle))
            text_y = center_y + text_radius * 0.7 * math.sin(math.radians(mid_angle))
            
            self.wheel_canvas.create_text(
                text_x, text_y,
                text=self.wheel_categories[i],
                font=("Arial", 12, "bold"),
                fill="black"
            )
 # position of pointer and center of wheel
        self.wheel_canvas.create_oval(
            center_x-20, center_y-20,
            center_x+20, center_y+20,
            fill="#000000", outline="white"
        )
        
        
        self.wheel_canvas.create_polygon(
            center_x+radius+10, center_y-10,
            center_x+radius+10, center_y+10,
            center_x+radius+30, center_y,
            fill="#FFFFFF"
        )
        
 # wheel speed and animations       
def start_wheel_spin(self):
        """Start the wheel spinning animation"""
        if not self.wheel_spinning:
            self.wheel_spinning = True
            self.spin_wheel_animation()
    
def spin_wheel_animation(self, speed=30, deceleration=0.98):
        """Animate the wheel spinning"""
        if speed > 0.5:
            self.wheel_angle = (self.wheel_angle + speed) % 360
            self.draw_wheel(self.wheel_angle)
            self.root.after(30, lambda: self.spin_wheel_animation(speed * deceleration, deceleration))
        else:
            self.wheel_spinning = False
            self.select_category()
            
# selected categories
def select_category(self):
        """Determine which category was selected"""
        segment_angle = 360 / len(self.wheel_categories)
        normalized_angle = 360 - (self.wheel_angle % 360)
        selected_index = int(normalized_angle / segment_angle) % len(self.wheel_categories)
        selected_category = self.wheel_categories[selected_index]
        
        # Show selected category
        self.wheel_canvas.create_text(
            250, 450,
            text=f"Selected: {selected_category}",
            font=("Arial", 16, "bold"),
            fill="#FFFFFF"
        )
        
        # Continue to question after delay
        self.root.after(2000, lambda: self.prepare_question(selected_category))

# preparing questions and category    
def prepare_question(self, category):
        """Prepare a question from the selected category"""
        # Filter questions by category and level
        available_questions = [
            q for q in self.all_questions[self.current_level] 
            if q["category"] == category
        ]
        
        if not available_questions:
            messagebox.showinfo("No Questions", f"No {category} questions available for {self.current_level} level.")
            self.show_main_menu()
            return

 # Select a random question
        self.current_question = random.choice(available_questions)
        self.show_question()
    
def show_question(self):
        """Display the current question"""
        self.clear_screen()
        
# Display category and level
        tk.Label(self.root, text=f"Category: {self.current_question['category']}", 
                font=("Arial", 14), bg="#000000", fg="#FFFFFF").pack(pady=5)
        tk.Label(self.root, text=f"Level: {self.current_level}", 
                font=("Arial", 14), bg="#000000", fg="#FFFFFF").pack(pady=5)
        
# Display score and attempts
        info_frame = tk.Frame(self.root, bg="#000000")
        info_frame.pack(pady=10)
        
        tk.Label(info_frame, text=f"Score: {self.score}", 
                font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=0, column=0, padx=20)
        tk.Label(info_frame, text=f"Attempts left: {self.attempts}", 
                font=("Arial", 12), bg="#000000", fg="#FFFFFF").grid(row=0, column=1, padx=20)
        
# Qustion display and answer 
 
        tk.Label(self.root, text=self.current_question["question"], 
                font=("Arial", 16, "bold"), bg="#000000", fg="#FFFFFF", wraplength=700).pack(pady=30)
        
        # Answer entry
        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)
        self.answer_entry.focus_set()
        
        # Submit button
        tk.Button(self.root, text="Submit Answer", command=self.check_answer, 
                bg="#4CAF50", fg="white", font=("Arial", 14, "bold")).pack(pady=20)
        
        # Bind Enter key to submit
        self.root.bind("<Return>", lambda event: self.check_answer())
        
# functions for checking the answer
def check_answer(self):
        """Check if the player's answer is correct"""
        player_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_question["answer"].strip().lower()
        
        if player_answer == correct_answer:
            # Correct answer
            self.score += 10
            self.questions_answered_in_level += 1
            messagebox.showinfo("Correct!", "Your answer is correct! +10 points")
            
            # Check if player should level up
            if self.questions_answered_in_level >= 5 and self.current_level != "Hard":
                self.level_up()
            else:
                self.show_main_menu()
        else:
            # Incorrect answer
            self.attempts -= 1
            if self.attempts > 0:
                messagebox.showerror("Incorrect", f"Wrong answer! You have {self.attempts} attempts left.")
                self.answer_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Game Over", "You've used all your attempts!")
                self.reset_game()
                
# level and reset functions
def level_up(self):
        """Move player to next difficulty level"""
        if self.current_level == "Easy":
            self.current_level = "Medium"
        elif self.current_level == "Medium":
            self.current_level = "Hard"
        
        self.questions_answered_in_level = 0
        self.attempts = 3  # Reset attempts
        
        messagebox.showinfo("Level Up!", f"Congratulations! You've reached {self.current_level} level!")
        self.show_main_menu()
    
def reset_game(self):
        """Reset the game to initial state"""
        self.score = 0
        self.attempts = 3
        self.current_level = "Easy"
        self.questions_answered_in_level = 0
        self.show_main_menu()
        
# instructions for the useer
def show_instructions(self):
        """Show game instructions"""
        self.clear_screen()
        
        tk.Label(self.root, text="Game Instructions", font=("Arial", 24, "bold"), bg="#000000", fg="#FFFFFF").pack(pady=20)
        
        instructions = [
            "1. Spin the wheel to select a question category.",
            "2. Answer the question correctly to earn 10 points.",
            "3. You have 3 attempts to answer correctly.",
            "4. Answer 5 questions correctly in a level to advance.",
            "5. The game has three levels: Easy, Medium, and Hard.",
            "6. Try to get the highest score possible!"
        ]
        
        for instruction in instructions:
            tk.Label(self.root, text=instruction, font=("Arial", 12), bg="#000000", fg="#FFFFFF").pack(pady=5)
        
        tk.Button(self.root, text="Back to Menu", command=self.show_main_menu, 
                 bg="#FF0000", fg="white", font=("Arial", 14, "bold")).pack(pady=20)
    