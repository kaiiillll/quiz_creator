import tkinter as tk
from tkinter import messagebox

# use def function 
def collect_questions():
    def save_questions():
        question = question_entry.get("1.0", tk.END.strip()
        subject = subject_var.get()
        difficulty = difficulty_var.get()
        options = {
            "a": option_a.get(),
            "b": option_b.get(),
            "c": option_c.get(),
            "d": option_d.get()
        }
        correct = correct_answer.get().lower()
        
        if not all([question, subject, difficulty, options["a"], options["b"], options["c"],options["d"]):
            messagebox.showerror("Error", "Please fill all field!")
            return
            
        if correct not in ["a", "b", "c", "d"]:
            messagebox.showerror("Error", "Correct answer must be a, b, c, or d!!")
            return
            
        with open("created_questions.txt", "a") as file:
            file.write(f"Subject: {subject}\n")
            file.write(f"Difficulty: {difficulty}\n")
            file.write(f"Question: {question}\n")
            file.write(f"a) {options['a']}\n")
            file.write(f"b) {options['b']}\n")
            file.write(f"c) {options['c']}\n")
            file.write(f"d) {options['d']}\n")
            file.write(f"Correct: {correct}\n\n")
            
        messagebox.showinfo("Saved", "Question saved succesfully!")
        clear_fields()
        
    def preview():
        preview text = f"Subject: {subject_var.get()}\n
        
            
    print("Quiz Creator")
    print("Enter your desired questions, subject, difficulty, and the answers. Type 'EXIT' to stop the program.\n")
            
            print("\nAvailable subjects: Math, Science, History, Literature, General Knowlege, Social Sciences")
            subject = (input("Enter the subject for this question: ")).title()
            
            while True: 
                difficulty = input("Enter difficulty level (Easy, Medium, Hard): ").title()
                if difficulty in ['Easy', 'Medium', 'Hard']:
                    break
                print("That is Invalid! Please choose from the three given stages.")
                
            print("\nEnter the four possible answers: ")
            # assigned choices and possible answers to questions
            a = input("a) ")
            b = input("b) ")
            c = input("c) ")
            d = input("d) ")
            
            # the correct will be saved also to the file 
            correct = input("\nEnter the correct answer to the question (a, b, c, or d): ").lower()
            while correct not in ['a', 'b', 'c', 'd']:
                print("That is invalid input!. Please enter a, b, c, or d.")
                correct = input("Enter the correct answer (a, b, c, or d")
            
            # these will write the inputs into the file
            file.write(f"Subject: {subject}\n")
            file.write(f"Difficulty: {difficulty}\n")
            file.write(f"Question: {question}\n")
            file.write(f"a) {a}\n")
            file.write(f"b) {b}\n")
            file.write(f"c) {c}\n")
            file.write(f"d) {d}\n")
            file.write(f"Correct answer: {correct}\n\n")
            
            print("\n--- Question preview ---")
            print(f"Subject: {subject}")
            print(f"Difficulty: {difficulty}")
            print(f"Question: {question}")
            print(f"a) {a}")
            print(f"b) {a}")
            print(f"c) {c}")
            print(f"d) {c}")
            print(f"Correct answer: {correct}")
            
            confirm = input("\nSave this question? (yes/no): ").lower()
            if confirm != 'yes':
                print("Question discarded. Enter it again if needed.")
                continue

            print("\nQuestions saved succesfully!.")
       
    print("\nAll questions have been saved to 'created_questions.txt'.")

if __name__ == "__main__":
    collect_questions()
    
    
    
    
    # TO make this program this more amazing I will make this into a app and user more friendly
