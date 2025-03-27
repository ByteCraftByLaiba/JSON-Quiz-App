import json

# Function to write in "RegisteredUser.json" using dump()
def writeInRegisteredUserFile(UsersDict):
    with open("RegisteredUser.json", "w") as outfile:
        json.dump(UsersDict, outfile, indent=4)

# Function to read from "RegisteredUser.json" using load()
def readFromRegisteredUserFile(UsersList):
    with open("RegisteredUser.json", "r") as registeredUsers:
        UsersDict = json.load(registeredUsers)
    UsersList = UsersDict["User"]
    return UsersList

# Function to read from "QuestionAnswer.json" using load()
def readFromQuestionAnswerFile():
    with open("QuestionAnswer.json", "r") as QA:
        questionsDict = json.load(QA)
    return questionsDict

# Function that display main menu of our Quiz App
def QuizAppMenu():
    print("----------------------------------------------------   ")
    print("    **** Welcome to our Quiz App ****             ")
    print("----------------------------------------------------\n")
    print("=> Press 1 to Login for the Quiz.")
    print("=> Press 2 to Sign up for the Quiz.")
    print("=> Press 3 to exit.\n")

# Function to login for the quiz app
def Login(UsersList):
    print("----------------------------------------------------")
    print("                Login in - Quiz App                 ")
    print("----------------------------------------------------\n")

    UserEmail = input("Enter your Email Address: ")
    UserPassword = input("Enter your Password: ")

    UsersList = readFromRegisteredUserFile(UsersList)

    for checkUser in UsersList:
        if checkUser["EmailAddress"] == UserEmail and checkUser["userPassword"] == UserPassword:
            print(
                "\n**************** CONGRATULATIONS! YOU HAVE LOGGED IN. ****************\n")
            START_QUIZ_FOR_USER(UsersList, UserEmail)
            return 0

    else:
        print("Invalid Credentials.\n")
        print("_________________________________________________________________")
        print("| Press 1 to Sign Up  | Press 2 to login again | Press 3 to exit |")
        print("_________________________________________________________________\n")

        while True:

            wantToRegister = input("Input your Desired Option: ")

            if (wantToRegister == '1'):
                SignUp(UsersList)

            elif (wantToRegister == '2'):
                Login(UsersList)
            
            elif (wantToRegister == '3'):
                break

            else:
                print("Invalid Option: Try Again...\n")

# Function to sign up for the quiz app
def SignUp(UsersList):

    print("--------------------------------------------")
    print("             Sign Up - Quiz App             ")
    print("--------------------------------------------\n")

    UsersList = readFromRegisteredUserFile(UsersList)

    print("   **** Register for the Quiz **** \n")

    while True:
        UserName = input("=> Enter your Name: ")
        isStudent = input("=> Are you a student? ")
        emailAddress = input("=> Enter your Email Address: ")
        userPassword = input("=> Enter you Password: ")
        totalQuizTaken = 0
        lastScore = 0
        if(checkUserExist(UsersList, emailAddress)):
            print("\nAccount already exist! Try again...\n")
        else:
            break

    User = {
        "UserName": UserName,
        "EmailAddress": emailAddress,
        "userPassword": userPassword,
        "isStudent": isStudent,
        "totalQuizTaken": totalQuizTaken,
        "lastScore": lastScore
    }

    UsersList.append(User)
    UsersDict = {"User": UsersList}
    writeInRegisteredUserFile(UsersDict)
    print("\n************ CONGRATULATIONS! YOU ACCOUNT HAS BEEN CREATED. ************\n")
    Login(UsersList)

# Function to check if the user, that is signing up, already exists in our system
def checkUserExist(UsersList, newUserEmail):
    for user in UsersList:
        if user["EmailAddress"] == newUserEmail:
            return True
    return False

# Function that display the menu to select Quiz Category 
def QuizMenu():
    print("\n----------------------------------------------------")
    print("                 === Quiz Menu ===                    ")
    print("----------------------------------------------------\n")

    print("Choose a quiz category:")
    print("1. Programming Quiz - Python")
    print("2. General Knowledge Quiz")
    print("3. English Language Quiz")
    print("4. Exit")

    print("\n----------------------------------------------------")

# function that take quiz from the user as per the category selected by the user
def startQuiz(quizCategory):
    TestScore = 0
    i = 1
    for quizQuestions in quizCategory:
        print(str(i) + "). " + quizQuestions["Question"])
        print("    A). " + quizQuestions["A)"],)
        print("    B). " + quizQuestions["B)"])
        print("    C). " + quizQuestions["C)"])
        print("    D). " + quizQuestions["D)"], "\n")

        SelectedAnswer = input("Enter Your Answer: ")

        correctAnswer = quizQuestions["CorrectAnswer"]

        if (SelectedAnswer == quizQuestions["CorrectAnswer"].lower() or SelectedAnswer == quizQuestions["CorrectAnswer"].upper()):
            print("*** CORRECT ANSWER ***\n")
            TestScore += 1
        else:
            print(f"INCORRECT ANSWER: Correct option is {correctAnswer}\n")
        i += 1

    print("----------------------------------------------------")
    print("                    Quiz Result                     ")
    print("----------------------------------------------------")
    print(f"You have scored {TestScore} out of 5 marks. ")
    print("----------------------------------------------------\n")

    return TestScore

# Function that update user test score and no of quiz taken data in "RegisteredUser.json" file
def updateTheFile(UsersList, UserEmail, TestScore):
    for user in UsersList:
        if user["EmailAddress"] == UserEmail:
            user["lastScore"] = TestScore
            user["totalQuizTaken"] += 1
    UsersDict = {"User": UsersList}
    writeInRegisteredUserFile(UsersDict)
# Function that implement the quiz app, it will display quiz categories and start quiz according to the category selected by user
def START_QUIZ_FOR_USER(UserList, UserEmail):

    QuizMenu()

    choice = input(
        "\nPlease enter the type of quiz you'd like to take (1-4): ")
    print("\n")

    questionsList = readFromQuestionAnswerFile()

    TestScore = 0

    while choice != '4':
        if (choice == '1'):
            print("----------------------------------------------------")
            print("            Programming Quiz - Python               ")
            print("----------------------------------------------------\n")
            TestScore = startQuiz(questionsList["Programming Quiz - Python"])
            updateTheFile(UserList, UserEmail, TestScore)

        elif (choice == '2'):
            print("----------------------------------------------------")
            print("               General Knowledge Quiz               ")
            print("----------------------------------------------------\n")
            TestScore = startQuiz(questionsList["General Knowledge"])
            updateTheFile(UserList, UserEmail, TestScore)

        elif (choice == '3'):
            print("----------------------------------------------------")
            print("               English Language Quiz                ")
            print("----------------------------------------------------\n")
            TestScore = startQuiz(questionsList["English Language"])
            updateTheFile(UserList, UserEmail, TestScore)

        else:
            print("No such option exist.")

        choice = input(
            "\nWould you like to take quiz again? (1-4): ")
        print("\n")

# --------------------------------------------------
#               Quiz App Main Interface
# --------------------------------------------------
UsersList = []

option = '0'

while option != '3':
    
    QuizAppMenu()
    option = input("Select your desired option: ")

    if option == '1':
         Login(UsersList)

    elif option == '2':
         SignUp(UsersList)

    else:
         print("INVALID OPTION: Try Again...\n")

print("----------------------------------------------------")
print("                      Good Bye :)                   ")
print("----------------------------------------------------")