def guess_the_number():
    """Computer has to guess the number between 1 to 100. 
    We need to find the guessed number correctly. 
    Provide the user with 2 playing option easy and hard. 
    If the user selected the easy option he will get 10 guesses. 
    If the user selected hard option he will get 5 guesses. """

    #Import library
    import random
    
    while True:

        computer = random.randint(0,100)
        print("Welcome to Number guessing game!")

        mode = ['easy', 'hard']

        game_mode = input('You want to play easy or hard?: ')

        if game_mode.lower() == 'easy':
            a = 0
            while a<=5:
                player = int(input('Guess the number here: '))
                if player in range(computer+10, 101):
                    print('Your guess is too high!')
                    a += 1
                elif player in range(computer+1, computer+10):
                    print('You are near')
                    a += 1
                elif player in range(computer-10, computer-1):
                    print('You are near')
                    a += 1
                elif player in range(0, computer-10):
                    print('Your guess is too low')
                    a += 1
                elif player == computer:
                    print('Hurray you found the number')
                    break
            print('Opps! you are out of guesses. You lose!')

        if game_mode.lower() == 'hard':
            a = 0
            while a<=10:
                player = int(input('Guess the number here: '))
                if player in range(computer+10, 101):
                    print('Your guess is too high!')
                    a += 1
                elif player in range(computer+1, computer+10):
                    print('You are near')
                    a += 1
                elif player in range(computer-10, computer-1):
                    print('You are near')
                    a += 1
                elif player in range(0, computer-10):
                    print('Your guess is too low')
                    a += 1
                elif player == computer:
                    print('Hurray you found the number')
                    break
            print('Opps! you are out of guesses. You lose!')

        return f'The computer guessed number is {computer}.'
        
        if game_mode not in mode:
            print('You entered the wrong game mode. You lose!')

        contin = input('Do you want to continue? yes/no ')
        if contin == 'no':
            break

guess = guess_the_number()
print(guess)