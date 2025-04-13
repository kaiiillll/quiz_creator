# use def function 
def collect_questions():
# print all following instructions
    print("Quiz Creator")
    print("Enter your desired questions, subject, difficulty, and the answers. Type 'EXIT' to stop the program.\n")

    with open("created_questions.txt", "a") as file:
        while True:
            question = input("Enter the question (or 'EXIT' to quit): ")
            if question.lower() == 'EXIT': # I used .lower so it will accept different input from user
                break # to stop the loop of while
            
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
    
    
# additional features of this program
# 1. the user will choose what subject the question is under
# 2. the user will choose the quiz difficulties