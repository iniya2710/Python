def hangman():
    import random

    #collecting random words
    vocabs = ['consider', 'minute', 'accord', 'evident', 'intend', 'concern', 'commit', 'issue', 
             'approach', 'establish', 'utter', 'conduct', 'engage', 'obtain', 'policy', 'stock', 
             'apparent', 'property', 'fancy', 'concept', 'court', 'appoint', 'passage', 'vain', 
             'instance', 'coast', 'project', 'commission', 'constant', 'level', 'affect', 'constitute',
             'render', 'appeal', 'generate', 'theory', 'range', 'league', 'labor', 'grant', 'dwell', 
             'yield', 'wander', 'inspire']
    
    #welcome message
    player = input('Enter your name: ')
    print(f'Hi {player} welcome to hangman game. You have 10 guessed to find the word!)')

    computer_guess = random.choice(vocabs)

    

    word = []
    for _ in range(len(computer_guess)):
        word.append('_')
    word = "".join(word)
    print(f'Word: {word}')
    #player making guess
    chances = 0
    while chances <=10:
        player_guess = input(f'Hi {player} guess the letter here:\n')
        if player_guess not in computer_guess:
            print('Oops! wrong guess')
            print(f'Word: {word}')
        else:
            print('Hurray you guessed the letter')
            index = []
            for i in range(len(computer_guess)):
                if computer_guess[i] == player_guess: 
                    index.append(i)
            for i in index:
                word = word[:i] + player_guess + word[i+1:] 
            print(f'Word: {word}')
        
        if  computer_guess == word:
            
            break
            
        chances +=1

    if  computer_guess == word:
        return 'Hurray! You guessed the word. You won the game!'
    if computer_guess != word:
        return f'''The word is '{computer_guess}' You failed to guess the word. You lost!'''

hangman_game = hangman()
print(hangman_game)