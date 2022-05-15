def new_game():  
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:   
        print("---------------------")
        print(key)
        
        for i in options[question_num - 1]:
            print(i)
        guess = input("Enter (A,B or C) : " )
        guess = guess.upper()        
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num+=1  

    display_score(correct_guesses,guesses)


def check_answer(answer , guess): # Checking the answer if it's correct or not
    if answer == guess:
        print("CORRECT !")
        return 1
    else:
        print("INCORRECT !")
        return 0


def display_score(correct_guesses,guesses):  # Displaying the score with (%)
    print("--------------------------")
    print("RESULTS")
    print("---------------------------")

    print("Answers : ",end =" ")
    for i in questions:
        print(questions.get(i),end="")
    print()

    print("Your guesses : ",end="")
    for i in guesses:
        print(i,end="")
    print()

    score = int(correct_guesses/len(questions)*100)
    print("Your score is "+str(score)+" %")
    

def play_again():   # Playing again
    response = input("Do you want to play again ?(Yes/no) : ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False
    
    
#------ DATA STORING ------

questions = {
'Who created relativity theory ? : ': "A",
'Who created Python programming language ? :':"B",
'Is the earth round ? : ':"A",
"What is the capital of morocco ":"B"
}

options = [["A.Albert einstein","B.Galiléo Galilé","C.Isaac Newton"],
           ["A.Elon Musk","B.Guido Van rossum","C.Bill gates"],
           ["A.Yes","B.No","C.Something else"],
           ["A.Paris","B.Rabat","C.Dehli"]]


new_game()


while play_again():
    new_game()
print("Thank you for playing ! ")



    

