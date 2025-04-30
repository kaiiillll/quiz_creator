import tkinter as tk
from tkinter import messagebox
import random
from collections import defaultdict

class WheelOfFortuneQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Wheel of Fortune Quiz Game")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f8ff")
        
        # Player data
        self.player = {
            "name": "",
            "gender": "",
            "age": 0,
            "section": "",
            "year": ""
        }
        
        # Game data
        self.all_questions = defaultdict(list)
        self.current_questions = []
        self.current_question = None
        self.score = 0
        self.attempts = 3
        self.current_level = "Easy"
        self.questions_answered_in_level = 0
        
        # Load questions at start
        self.load_questions()
        
        # Start with registration screen
        self.show_registration_screen()
    
    def load_questions(self):
        """Load questions from the created_questions.txt file and categorize by difficulty"""
        try:
            with open("created_questions.txt", "r") as file:
                content = file.read().split("\n\n")
                
            for block in content:
                if not block.strip():
                    continue
                    
                question_data = {}
                lines = block.split("\n")
                for line in lines:
                    if ":" in line:
                        key, value = line.split(":", 1)
                        question_data[key.strip().lower()] = value.strip()
                
                if len(question_data) >= 7:  # Ensure all required fields exist
                    difficulty = question_data.get("difficulty", "Easy").capitalize()
                    self.all_questions[difficulty].append(question_data)
                    
            if not self.all_questions:
                messagebox.showerror("Error", "No questions found in the database!")
                self.root.destroy()
                
        except FileNotFoundError:
            messagebox.showerror("Error", "Question database not found! Please create questions first.")
            self.root.destroy()
    
    def prepare_level_questions(self):
        """Prepare questions for the current difficulty level"""
        self.current_questions = self.all_questions.get(self.current_level, [])
        random.shuffle(self.current_questions)
        self.questions_answered_in_level = 0
    
    def advance_level(self):
        """Move to the next difficulty level"""
        levels = ["Easy", "Medium", "Hard"]
        current_index = levels.index(self.current_level)
        
        if current_index < len(levels) - 1:
            self.current_level = levels[current_index + 1]
            self.prepare_level_questions()
            messagebox.showinfo("Level Up!", f"Advancing to {self.current_level} questions!")
            return True
        else:
            messagebox.showinfo("Congratulations!", "You've completed all difficulty levels!")
            self.show_game_over_screen()
            return False
    
    def show_registration_screen(self):
        """Show player registration form"""
        self.clear_screen()
        
        tk.Label(self.root, text="Player Registration", font=("Arial", 20, "bold"), bg="#f0f8ff").pack(pady=20)
        
        # Registration form
        form_frame = tk.Frame(self.root, bg="#f0f8ff")
        form_frame.pack(pady=10)
        
        # Name
        tk.Label(form_frame, text="Full Name:", bg="#f0f8ff").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Gender
        tk.Label(form_frame, text="Gender:", bg="#f0f8ff").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.gender_var = tk.StringVar(value="Male")
        tk.Radiobutton(form_frame, text="Male", variable=self.gender_var, value="Male", bg="#f0f8ff").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        tk.Radiobutton(form_frame, text="Female", variable=self.gender_var, value="Female", bg="#f0f8ff").grid(row=1, column=1, padx=5, pady=5, sticky="e")
        
        # Age
        tk.Label(form_frame, text="Age:", bg="#f0f8ff").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.age_entry = tk.Entry(form_frame, width=30)
        self.age_entry.grid(row=2, column=1, padx=5, pady=5)
        
        # Section
        tk.Label(form_frame, text="Section:", bg="#f0f8ff").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.section_entry = tk.Entry(form_frame, width=30)
        self.section_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Year
        tk.Label(form_frame, text="Year Level:", bg="#f0f8ff").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.year_var = tk.StringVar()
        years = ["1st Year", "2nd Year", "3rd Year", "4th Year"]
        tk.OptionMenu(form_frame, self.year_var, *years).grid(row=4, column=1, padx=5, pady=5, sticky="w")
        
        # Register button
        tk.Button(self.root, text="Start Game", command=self.register_player, bg="#4CAF50", fg="white", 
                 font=("Arial", 12, "bold")).pack(pady=20)
    
    def register_player(self):
        """Register player and start game"""
        self.player["name"] = self.name_entry.get().strip()
        self.player["gender"] = self.gender_var.get()
        
        try:
            self.player["age"] = int(self.age_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age!")
            return
            
        self.player["section"] = self.section_entry.get().strip()
        self.player["year"] = self.year_var.get()
        
        if not all(self.player.values()):
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        # Start with Easy questions
        self.current_level = "Easy"
        self.prepare_level_questions()
        self.show_game_screen()
    
    def show_game_screen(self):
        """Show the main game screen"""
        self.clear_screen()
        
        # Header with player info
        header_frame = tk.Frame(self.root, bg="#f0f8ff")
        header_frame.pack(fill="x", pady=10)
        
        tk.Label(header_frame, 
                text=f"Player: {self.player['name']} ({self.player['gender']}, {self.player['age']}) | "
                     f"{self.player['year']} - {self.player['section']} | "
                     f"Score: {self.score} | Attempts left: {self.attempts}",
                bg="#f0f8ff", font=("Arial", 10)).pack()
        
        # Level indicator
        level_frame = tk.Frame(self.root, bg="#f0f8ff")
        level_frame.pack(pady=5)
        
        levels = ["Easy", "Medium", "Hard"]
        for i, level in enumerate(levels):
            color = "#4CAF50" if level == self.current_level else ("#cccccc" if levels.index(level) < levels.index(self.current_level) else "#ffffff")
            tk.Label(level_frame, text=level[0], bg=color, fg="black", 
                    font=("Arial", 14, "bold"), width=3, relief="ridge").grid(row=0, column=i, padx=5)
        
        # Game title
        tk.Label(self.root, text="Wheel of Fortune Quiz", font=("Arial", 24, "bold"), bg="#f0f8ff").pack(pady=10)
        tk.Label(self.root, text=f"Current Level: {self.current_level}", font=("Arial", 16), bg="#f0f8ff").pack()
        
        # Spin wheel button
        tk.Button(self.root, text="SPIN THE WHEEL!", command=self.spin_wheel, 
                 bg="#FF5722", fg="white", font=("Arial", 16, "bold")).pack(pady=30)
        
        # Question display area (initially empty)
        self.question_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.question_frame.pack(pady=20)
        
        # Answer area (initially empty)
        self.answer_frame = tk.Frame(self.root, bg="#f0f8ff")
        self.answer_frame.pack(pady=10)
    
    def spin_wheel(self):
        """Select a random question from current level and display it"""
        if self.attempts <= 0:
            messagebox.showinfo("Game Over", "You've used all your attempts!")
            self.show_game_over_screen()
            return
            
        if not self.current_questions and self.questions_answered_in_level >= 3:
            if not self.advance_level():
                return
        
        # Clear previous question
        for widget in self.question_frame.winfo_children():
            widget.destroy()
        for widget in self.answer_frame.winfo_children():
            widget.destroy()
            
        # Select random question from current level
        if not self.current_questions or self.questions_answered_in_level >= 3:
            self.prepare_level_questions()
            
        self.current_question = self.current_questions.pop(0)
        
        # Display question
        tk.Label(self.question_frame, 
                text=f"Subject: {self.current_question.get('subject', 'N/A')} | "
                     f"Difficulty: {self.current_question.get('difficulty', 'N/A')}",
                bg="#f0f8ff", font=("Arial", 12, "bold")).pack()
        
        tk.Label(self.question_frame, 
                text=self.current_question.get("question", "No question found"),
                bg="#f0f8ff", font=("Arial", 14), wraplength=700).pack(pady=10)
        
        # Display options
        options_frame = tk.Frame(self.question_frame, bg="#f0f8ff")
        options_frame.pack(pady=10)
        
        for opt in ['a', 'b', 'c', 'd']:
            tk.Label(options_frame, 
                    text=f"{opt}) {self.current_question.get(opt, 'N/A')}",
                    bg="#f0f8ff", font=("Arial", 12)).pack(anchor="w")
        
        # Answer input
        tk.Label(self.answer_frame, text="Your answer (a-d):", bg="#f0f8ff").pack()
        self.answer_entry = tk.Entry(self.answer_frame, width=5, font=("Arial", 14))
        self.answer_entry.pack()
        
        # Submit button
        tk.Button(self.answer_frame, text="Submit Answer", command=self.check_answer,
                 bg="#2196F3", fg="white").pack(pady=10)
    
    def check_answer(self):
        """Check if the player's answer is correct"""
        if not self.current_question:
            return
            
        player_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.current_question.get("correct", "").lower()
        
        if player_answer not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Please enter a valid answer (a, b, c, or d)")
            return
            
        self.questions_answered_in_level += 1
        
        if player_answer == correct_answer:
            # Calculate points based on difficulty
            points = {"Easy": 5, "Medium": 10, "Hard": 15}.get(self.current_level, 5)
            self.score += points
            messagebox.showinfo("Correct!", f"Congratulations! You got it right!\n+{points} points")
        else:
            self.attempts -= 1
            messagebox.showinfo("Incorrect", 
                              f"Sorry, the correct answer was {correct_answer.upper()}.\n"
                              f"You have {self.attempts} attempts remaining.")
        
        # Update game screen
        self.show_game_screen()
    
    def show_game_over_screen(self):
        """Show final score and options"""
        self.clear_screen()
        
        tk.Label(self.root, text="Game Over", font=("Arial", 24, "bold"), bg="#f0f8ff").pack(pady=40)
        tk.Label(self.root, text=f"Final Score: {self.score}", font=("Arial", 18), bg="#f0f8ff").pack(pady=20)
        
        # Level progress
        levels_frame = tk.Frame(self.root, bg="#f0f8ff")
        levels_frame.pack(pady=10)
        
        levels = ["Easy", "Medium", "Hard"]
        for i, level in enumerate(levels):
            color = "#4CAF50" if levels.index(level) < levels.index(self.current_level) else "#cccccc"
            tk.Label(levels_frame, text=level[0], bg=color, fg="black", 
                    font=("Arial", 14, "bold"), width=3, relief="ridge").grid(row=0, column=i, padx=5)
        
        # Player info
        tk.Label(self.root, 
                text=f"Player: {self.player['name']} ({self.player['gender']}, {self.player['age']})\n"
                     f"{self.player['year']} - {self.player['section']}",
                bg="#f0f8ff", font=("Arial", 12)).pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#f0f8ff")
        button_frame.pack(pady=30)
        
        tk.Button(button_frame, text="Play Again", command=self.reset_game, 
                 bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Exit", command=self.root.destroy,
                 bg="#F44336", fg="white").grid(row=0, column=1, padx=10)
    
    def reset_game(self):
        """Reset the game to start over"""
        self.score = 0
        self.attempts = 3
        self.current_level = "Easy"
        self.questions_answered_in_level = 0
        self.prepare_level_questions()
        self.show_registration_screen()
    
    def clear_screen(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = WheelOfFortuneQuiz(root)
    root.mainloop()