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
            print("Here's an espresso!")
        case 'latte':
            print("Here's a latte!")
        case 'cappuccino':
            print("Here's a cappuccino!")
        case 'report':
            report()
        case _:
            print("Not an espresso!")


order = "report"
make_drink(order)
