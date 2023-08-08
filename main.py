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
            if resources['water'] < 50:
                print("Not enough water to make an espresso.")
                return
            elif resources['coffee'] < 18:
                print("Not enough coffee to make an espresso.")
                return
            else:
                print("Here's an espresso!")
                return
        case 'latte':
            print("Here's a latte!")
        case 'cappuccino':
            print("Here's a cappuccino!")
        case 'report':
            report()
        case _:
            print("Not an espresso!")


order = "espresso"
make_drink(order)
