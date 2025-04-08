# use def function 
def collect_questions():
# print all following instructions
    print("Quiz Creator")
    print("Enter your desired questions and the answers. Type 'EXIT' to stop the program.\n")

    with open("created_questions.txt", "a") as file:
        while True:
            question = input("Enter the question (or 'EXIT' to quit): ")
            if question.lower() == 'EXIT': # I used .lower so it will accept different input from user
                break # to stop the loop of while
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
            file.write(f"Question: {question}\n")
            file.write(f"a) {a}\n")
            file.write(f"b) {b}\n")
            file.write(f"c) {c}\n")
            file.write(f"d) {d}\n")
            file.write(f"Correct answer: {correct}\n\n")
            
            print("\nQuestions saved succesfully!.")
       
    print("\nAll questions have been saved to 'created_questions.txt'.")

if __name__ == "__main__":
    collect_questions()