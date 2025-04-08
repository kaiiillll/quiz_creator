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
        
# use the while true loop
# if statement
# break to stop the while true loop
# save the file 
# save the name of user then continue to the loop