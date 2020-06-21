#guessing the number from 1 to 100
import random
import sys

def playGame():

    answer = random.randint(int(sys.argv[1]), int(sys.argv[2]))

    #get inpit from the user 
  
    while True:
        try:
            num = int(input(f'Enter Number for check between {sys.argv[1]} to {sys.argv[2]}'))
            if int(sys.argv[1]) <= num <= int(sys.argv[2]):
                #perform guess game 
                if num == answer:
                    print("Thats a correct guess!!")
                else:
                    print(f'Sorry entered number was {answer}, better luck next time')
                
                break
                
            else:
                print(f'Please eEnter Number for check between {sys.argv[1]} to {sys.argv[2]}') 
            
        except ValueError:
            print("Enter A Number")

   

playGame()
while True:
    playAgain = bool(int(input("Enter any key to play again (Enter: 0/ False/ Just hit enter -> Quit)?")))
    print(playAgain)
    if playAgain == True:
        playGame()
    else:
        print("Thanks for playing the game")
        break

