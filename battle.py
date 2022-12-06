import random

def battle ():
    player = 0
    computer = 0
    while True:
        choice = random.randint(1,3)
        choose = input("You know the drill. Rock, Paper, or Scissors? ")
        if choose.lower() == "rock":
            print("Your choice: Rock")
            if choice == 1:
                print("Computer's choice: Rock")
                print("Draw!")
            elif choice == 2:
                print("Computer's choice: Paper")
                print("Too bad, you lose!")
                computer += 1
            else:
                print("Computer's choice: Scissors")
                print("Nice job, you win!")
                player += 1
        elif choose.lower() == "paper":
            print("Your choice: Paper")
            if choice == 1:
                print("Computer's choice: Paper")
                print("Draw!")
            elif choice == 2:
                print("Computer's choice: Scissors")
                print("Too bad, you lose!")
                computer += 1               
            else:
                print("Computer's choice: Rock")
                print("Nice job, you win!")
                player += 1
        else: 
            print("Your choice: Rock")
            if choice == 1:
                print("Computer's choice: Rock")
                print("Draw!")
            elif choice == 2:
                print("Computer's choice: Paper")
                print("Too bad, you lose!")
                computer += 1              
            else:
                print("Computer's choice: Scissors")
                print("Nice job, you win!")
                player += 1
        
        what_now = input("Would you like to play again? (y/n)?")
        
        if what_now.lower() == 'n' or what_now.lower() == 'quit' or what_now.lower() == "no":
            break

    print("Your points: " + str(len(points)))
    print("Computer's points: " + str(len(computer)))
    if len(points) < len(computer):
        print("Better luck, next time!")
    elif len(points) > len(computer):
        print("Congratulations! You're the winner, overall!")
    else: 
        print("Draw! Better luck, next time!")
        
battle()