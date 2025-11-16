import random
gameChoices = ('rock', 'paper', 'scissors') 
user_win = 0
computer_win = 0 
while True :
    user_choice = input("Choose option (Rock, Paper, Scissors, Q for quit): ").lower().strip()
    if user_choice in ('q', 'quit'):
         break 
    if user_choice not in gameChoices:
        print("invalid choice please choose one of the options ")
        continue
    computer_choice = random.choice(gameChoices)
    if user_choice == 'rock' and computer_choice == 'scissors' : 
        print('Computer chose : ' ,computer_choice )
        print('YOU WON !!')
        user_win += 1 
     #scissors beats paper
    elif user_choice == 'scissors' and computer_choice == 'paper' : 
        print('Computer chose : ' ,computer_choice )
        print('YOU WON !!')
        user_win += 1 
    #paper beats rock
    elif user_choice == 'paper' and computer_choice == 'rock' : 
        print('Computer chose : ' ,computer_choice )
        print('YOU WON !!')
        user_win += 1
    elif user_choice == computer_choice :
        print('Computer chose : ' , computer_choice)
        print('TIE')
    else : 
        print('Computer chose : ' , computer_choice)
        print('Computer won :-( ')
        computer_win += 1 
        
print(f'The final score : Computer Score is  {computer_win} and Your score is {user_win}')

