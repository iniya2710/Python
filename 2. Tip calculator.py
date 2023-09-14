def tip_calculator():
    """This python function will calculate the bill along with the tip 
    shared by people who went for lunch together."""

    #Welcome message
    print('Welcome to the tip calculator.')

    #getting info from user
    bill = float(input('What was the total bill? $'))
    tip = float(input('What percentage tip would you like to give? 10, 12 or 15? '))
    people = int(input('How many people to split the bill? '))

    #calculating bill and tip per person
    tip_ammount = bill * tip / 100
    total_bill = bill + tip_ammount
    bill_per_person = total_bill / people
    
    return bill_per_person

tip_calc = tip_calculator()
print(f'Each person should pay: ${tip_calc}')