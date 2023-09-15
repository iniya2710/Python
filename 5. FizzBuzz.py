def fizz_buzz():
    
    """This function will get the number from user.
    If the number is multiples of three print "Fizz" instead of the number and 
    If the number is of five print "Buzz". 
    If number that is multiples of three and five, print "FizzBuzz"."""

    number = int(input('Enter the range of number you want: '))
    for i in range(1,number+1):
        if i %3 == 0 and i %5 != 0:
            print('fizz')
        elif i %5 == 0 and i %3 != 0:
            print('Buzz')
        elif i %3 == 0 and i %5 == 0:
            print('fizzbuzz')
        else:
            print(i)
    return '--end--'
        
fb = fizz_buzz()
print(fb)