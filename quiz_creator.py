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
            