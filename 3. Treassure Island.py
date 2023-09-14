def treassure_island():
    print("Welcome to Treasure Island.🏴‍☠️")
    print("Your mission is to find the treasure.🪙")
    choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" ⬅️ or "right" ➡️ :\n').lower()
    def dont_follow_instructions():
        # runs if the user does not follow the instructions correctly
        print('You don\'t know how to follow the instructions correctly!\nGAME OVER!')
    if choice1 == 'right':
        return 'You\'ve fall into a hole.\nGAME OVER!💀'

    elif choice1 == 'left':
        choice2 = input('You\'ve come to a lake. Do you wanna "swim"🏊 or "wait"🧍?\n').lower()
        if choice2 == 'swim':
            return 'You were attacked by an angry trout.\nGAME OVER!💀'
        elif choice2 == 'wait':
            choice3 = input('You arrive at the island unharmed. There is a house with 3 🚪 with different colors. Which 🚪 color do you choose: "red", "yellow" or "blue"?\n').lower()
            if choice3 == 'red':
                return 'You were burned by fire.\nGAME OVER!💀'
            elif choice3 == 'blue':
                return 'You were eaten by beasts.\nGAME OVER!💀'
            elif choice3 == 'yellow':
                return 'CONGRATULATIONS! YOU FOUND THE TREASURE! YOU WIN!🥇'
            else:
                dont_follow_instructions()
        else:
            dont_follow_instructions()
    else:
        dont_follow_instructions()

game = treassure_island()
print(game)