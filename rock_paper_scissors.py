import random
print("****GAME STARTED****")

play='y'

def game():
    user=input("Enter your choice (rock or paper or scissors):")
    a=["rock","paper","scissors"]
    c=random.randint(0,2)
    computer=a[c]
    if computer=="rock":
        if user=="rock":
            print("Its a tie")
        elif user=="paper":
            print("You Won")
        elif user=="scissors":
            print("You Lost")
        else:
            print("Enter the correct choice")   

    elif computer=="paper":
        if user=="rock":
            print("You Lost")
        elif user=="paper":
            print("Its a tie")
        elif user=="scissors":
            print("You Won")
        else:
            print("Enter  the correct choice") 

    elif computer=="scissors":
        if user=="rock":
            print("You Won")
        elif user=="paper":
            print("You Lost")
        elif user=="scissors":
            print("Its a tie")

    else:
        print("Enter the correct choice") 

    print("Computer :",computer)
    print("User :",user)
    play=input("Do you want to play another round ? y or n? :")
    if play=='y':
        game()
    else:
        print("****Game Ended****")
game()