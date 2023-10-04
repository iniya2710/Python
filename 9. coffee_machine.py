#create code for an coffee machine
'''
**key points**
1. coffee falvor and resource
    - Coffee flavors: 
        - Expresso (150ml water + 18g coffee powder)
        - Latte (200ml water + 24g coffee powder+ 150ml milk)
        - Cappucino (250ml water + 24g coffee powder + 100ml milk)
    - Resource limit:
        - Water 500ml
        - Milk 500ml
        - Coffee powder 300g

2. coin operate
    - Expresso cost Rs.30
    - Latte cost Rs.40
    - Cappucino cost Rs.50

3. secret code for maintainance purpose
    - off
    - Report --> shows available milk, coffee powder and water
'''

def coffee_machine():

    import time

    #Resource assignment
    water = 2000
    milk = 2000
    coffee = 300
    flavor = ['latte', 'expresso', 'cappucino', 'report', 'no']

    coffee_logo = r"""
    (  )   (   )  )
     ) (   )  (  (
     ( )  (    ) )
     _____________
    <_____________> ___
    |             |/ _ \
    |               | | |
    |               |_| |
    |             |\___/
     \___________/
    """
    while True:
        user_prefer = input(f'{coffee_logo}\nWhat would you like to have? (Latte/ Expresso/ Cappucino):').lower()

        if user_prefer in flavor:
            if user_prefer == 'report':
                return f'''Resource availability:\n
                        Water = {water}ml\n
                        Milk = {milk}ml\n
                        Coffee Powder = {coffee}g
                        '''
            if user_prefer == 'expresso':
                water = water - 150
                coffee = coffee - 18

                if water < 150:
                    print('Not enough Water! Contact the maintenance team nearby!')
                elif coffee < 18:
                    print('Not enough Coffee powder! Contact the maintenance team nearby!')
                else: 
                    money = int(input('Your Expresso is Rs.30.\nPlease drop the money here!'))
                    if money == 30:
                        print('Enjoy your Latte!')
                    elif money > 30:
                        change = money - 30
                        print(f'Here is your change {change}. Enjoy your Expresso!')
                    else:
                        insuff_money = 30 - money
                        remaining_money = int(input(f'Your amount is not sufficient. Please provide the remaining amount {insuff_money} here:'))
                        final_amount = remaining_money + 30
                        if final_amount == 30:
                            print('Enjoy your Expresso!')
                        elif final_amount > 30:
                            change = money - 30
                            print(f'Here is your change {change}. Enjoy your Expresso!')
            if user_prefer == 'latte':
                water = water - 200
                coffee = coffee - 74
                milk = milk - 150

                if water < 200:
                    print('Not enough Water! Contact the maintenance team nearby!')
                elif coffee < 74:
                    print('Not enough Coffee powder! Contact the maintenance team nearby!')
                elif milk < 150:
                    print('Not enough Milk! Contact the maintenance team nearby!')
                else: 
                    money = int(input('Your Latte is Rs.40.\nPlease drop the money here!'))
                    if money == 40:
                        print('Enjoy your Latte!')
                    elif money > 40:
                        change = money - 40
                        print(f'Here is your change {change}. Enjoy your Latte!')
                    else:
                        insuff_money = 40 - money
                        remaining_money = int(input(f'Your amount is not sufficient. Please provide the remaining amount {insuff_money} here:'))
                        final_amount = remaining_money + 40
                        if final_amount == 40:
                            print('Enjoy your Latte!')
                        elif final_amount > 40:
                            change = money - 40
                            print(f'Here is your change {change}. Enjoy your Latte!')
            if user_prefer == 'Cappucino':
                water = water - 250
                coffee = coffee - 24
                milk = milk - 100

                if water < 250:
                    print('Not enough Water! Contact the maintenance team nearby!')
                elif coffee < 24:
                    print('Not enough Coffee powder! Contact the maintenance team nearby!')
                elif milk < 100:
                    print('Not enough Milk! Contact the maintenance team nearby!')
                else: 
                    money = int(input('Your Latte is Rs.50.\nPlease drop the money here!'))
                    if money == 50:
                        print('Enjoy your Latte!')
                    elif money > 50:
                        change = money - 50
                        print(f'Here is your change {change}. Enjoy your Cappucino!')
                    else:
                        insuff_money = 50 - money
                        remaining_money = int(input(f'Your amount is not sufficient. Please provide the remaining amount {insuff_money} here:'))
                        final_amount = remaining_money + 50
                        if final_amount == 50:
                            print('Enjoy your Cappucino!')
                        elif final_amount > 50:
                            change = money - 50
                            print(f'Here is your change {change}. Enjoy your Cappucino!')  
            if user_prefer == 'no':
                break
        else: 
            print('The one you selected is not available')
        time.sleep(5)

coffee_machine()