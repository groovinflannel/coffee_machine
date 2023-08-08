from menu import MENU
from resources import resources


# 1. Print report of all of the coffee machine's resources
# TODO: 2. Check that resources are sufficient to make drink order
# TODO: 3. Check that coins given are more than the cost of the drink
# TODO: 4. Return the correct change to the user
# TODO: 5. Make the drink and print a successful message for the user

# Functions
def report():
    print(f"Current resource levels:")
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


def make_drink(drink_type):
    match drink_type:
        case 'espresso':
            if resources['water'] < MENU["espresso"]["ingredients"]["water"]:
                print("Not enough water to make an espresso.")
                return
            elif resources['coffee'] < MENU["espresso"]["ingredients"]["coffee"]:
                print("Not enough coffee to make an espresso.")
                return
            else:
                print("Here's an espresso!")
                return
        case 'latte':
            if resources['water'] < MENU["latte"]["ingredients"]["water"]:
                print("Not enough water to make an latte.")
                return
            elif resources['milk'] < MENU["latte"]["ingredients"]["milk"]:
                print("Not enough milk to make an latte.")
            elif resources['coffee'] < MENU["latte"]["ingredients"]["coffee"]:
                print("Not enough coffee to make an latte.")
                return
            else:
                print("Here's a latte!")
                return
        case 'cappuccino':
            if resources['water'] < MENU["cappuccino"]["ingredients"]["water"]:
                print("Not enough water to make an cappuccino.")
                return
            elif resources['milk'] < MENU["cappuccino"]["ingredients"]["milk"]:
                print("Not enough milk to make an cappuccino.")
            elif resources['coffee'] < MENU["cappuccino"]["ingredients"]["coffee"]:
                print("Not enough coffee to make an cappuccino.")
                return
            else:
                print("Here's a cappuccino!")
                return
        case 'report':
            report()
        case 'quit':
            print("Quitting program.")
            return
        case _:
            print("Not a valid entry!")


def take_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    total_inserted = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)

    return total_inserted


def check_cost(drink_type, payment):
    if drink_type == 'espresso' and payment < int(MENU['espresso']['cost']):
        print("You didn't pay enough for an espresso.")
        return
    elif drink_type == 'latte' and payment < int(MENU['latte']['cost']):
        print("You didn't pay enough for a latte.")
        return
    elif drink_type == 'cappuccino' and payment < int(MENU['cappuccino']['cost']):
        print("You didn't pay enough for a cappuccino.")
        return


order = input("What would you like? Type espresso, latte, or cappucino and press Enter. Type report "
              "to get a report on machine resources or quit to end the program. ")


make_drink(order)
total_paid = take_coins()
check_cost(order, total_paid)


