def password_generator():
    #importing necessary libraries
    import random 
    import string

    #variable setting
    letters = string.ascii_letters
    digits = string.digits
    punctuations = string.punctuation

    #getting user suggestions
    n_letters = int(input('How many letters you want in your password: '))
    n_digits = int(input('How many digits you want in your password: '))
    n_punct = int(input('How many punctuations you want in your password: '))

    #password generation
    password = []
    for char in range(0,n_letters+1):
        password.append(random.choice(letters))
    for num in range(0,n_digits+1):
        password.append(random.choice(digits))
    for num in range(0,n_punct+1):
        password.append(random.choice(punctuations))
    random.shuffle(password)
    password = ''.join(password)
    return password
    
password = password_generator()
print('Your password is:', password)