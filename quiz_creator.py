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
        
        if not all([question,subject, difficulty, options["a"], options["b"], options["c"], options["d"], correct]):
            messagebox.showerror("Error", "Please fill all fields!")
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
        preview_text += f"Difficulty: {difficulty_var.get()}\n"
        preview_text += f"Question: {question_entry.get('1.0', tk.END).strip()}\n"
        preview_text += f"a) {option_a.get()}\n"
        preview_text += f"b) {option_b.get()}\n"
        preview_text += f"c) {option_c.get()}\n"
        preview_text += f"d) {option_d.get()}\n"
        preview_text += f"Correct: {correct_answer.get().lower()}"
        
        messagebox.showinfo("Preview", preview_text)
        
    def clear_fields():
        question_entry.delete("1.0", tk.END)
        subject_var.set("Math")
        difficulty_var.set("Easy")
        option_a.delete(0, tk.END)
        option_b.delete(0, tk.END)
        option_c.delete(0, tk.END)
        option_d.delete(0, tk.END)
        correct_answer.delete(0, tk.END)
        
    root = tk.Tk()
    root.title("Teacher's Quiz Maker")
    root.geometry("500x550")
    root.configure(bg="#e6f2ff")
    
    # Question Entry
    tk.Label(root, text="Question:").pack(pady=5)
    question_entry = tk.Text(root, height=4, width=50)
    question_entry.pack(pady=5)

    # Subject
    tk.Label(root, text="Subject:").pack(pady=5)
    subject_var = tk.StringVar()
    subjects = ["Math", "Science", "History", "English", "General"]
    tk.OptionMenu(root, subject_var, *subjects).pack(fill="x", padx=50)

    # Difficulty
    tk.Label(root, text="Difficulty:").pack(pady=5)
    difficulty_var = tk.StringVar()
    difficulties = ["Easy", "Medium", "Hard"]
    tk.OptionMenu(root, difficulty_var, *difficulties).pack(fill="x", padx=50)
    
     # Answer Options
    tk.Label(root, text="Options:").pack(pady=5)
    option_a = tk.Entry(root, width=50)
    option_a.pack(pady=2)
    option_b = tk.Entry(root, width=50)
    option_b.pack(pady=2)
    option_c = tk.Entry(root, width=50)
    option_c.pack(pady=2)
    option_d = tk.Entry(root, width=50)
    option_d.pack(pady=2)

    # Correct Answer
    tk.Label(root, text="Correct Answer (a-d):").pack(pady=5)
    correct_answer = tk.Entry(root, width=5)
    correct_answer.pack()
    
    # Buttons
    tk.Button(root, text="Save Question", command=save_question, bg="green", fg="white").pack(pady=10)
    tk.Button(root, text="Preview", command=preview).pack(pady=5)
    tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

    root.mainloop()
        
if __name__ == "__main__":
    collect_questions()
    