def rock_paper_scissor():
    #import necessary library
    import random

    # assigning variable
    options = ['rock','paper', 'scissor']

    #welcome message

    print("""\nHello Welcome to rock paper scissor game!\n\nHere are the game instructions for you:
        - Rock smashes scissors.
        - Paper covers rock.
        - Scissors cut paper.
        - If you type invalid key computer gets a point\n \nThe one who reaches 5 points first wins the game!\n""")


    #counter variable assignment
    player = 0
    computer = 0
    while player <= 5 or computer <= 5:
        
        #user choice
        user_choice = input("What do you choose? Rock, Paper or Scissor:\N ").lower()
        print("Your Choice :", user_choice)
        
        #computer choice
        computer_choice = random.randint(0, 2)
        print("Computer Choice : ",options[computer_choice] )

        if user_choice == 'rock' and options[computer_choice] == 'paper':
            computer+=1
            print("Oops! You Lose\n")
            print(f'you: {player}    computer: {computer}\n')

        elif user_choice == 'rock' and options[computer_choice] == 'scissor':
            player+=1
            print("Hurray! You won\n")
            print(f'you: {player}    computer: {computer}\n')
            
        elif user_choice == 'scissor' and options[computer_choice] == 'rock':
            computer+=1
            print("Oops! You Lose\n")
            print(f'you: {player}    computer: {computer}\n')
            
        elif user_choice == 'scissor' and options[computer_choice] == 'paper':
            player+=1
            print("Hurray! You won\n")
            print(f'you: {player}    computer: {computer}\n')
            
        elif user_choice == 'paper' and options[computer_choice] == 'rock':
            player+=1
            print("Hurray! You won\n")
            print(f'you: {player}    computer: {computer}\n')
            
        elif user_choice == 'paper' and options[computer_choice] == 'scissor':
            computer+=1
            print("Oops! You Lose\n")
            print(f'you: {player}    computer: {computer}\n')
            
        elif user_choice == options[computer_choice] :
            print("It's a draw\n")
            print(f'you: {player}    computer: {computer}\n')
        else:
            computer+=1
            print("You typed an invalid number, you lose!\n")
            print(f'you: {player}    computer: {computer}\n')
        if player == 5 or computer == 5:
            break
    if player == 5:
        return 'Hurray! You are the  winner of the game'
    else:
        return 'You lost to computer'
        

rpc = rock_paper_scissor()
print(rpc)