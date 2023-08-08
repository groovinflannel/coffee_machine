from menu import MENU
from resources import resources


# 1. Print report of all of the coffee machine's resources
# 2. Check that resources are sufficient to make drink order
# 3. Check that coins given are more than the cost of the drink
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
                total_paid = take_coins()
                if check_cost(order, total_paid):
                    resources['water'] = resources['water'] - MENU["espresso"]["ingredients"]["water"]
                    resources['coffee'] = resources['coffee'] - MENU["espresso"]["ingredients"]["coffee"]
                    return_change(drink_type, total_paid)
                else:
                    print(f"Not enough paid for a {order}.")
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
                total_paid = take_coins()
                if check_cost(order, total_paid):
                    resources['water'] = resources['water'] - MENU["latte"]["ingredients"]["water"]
                    resources['milk'] = resources['milk'] - MENU["latte"]["ingredients"]["milk"]
                    resources['coffee'] = resources['coffee'] - MENU["latte"]["ingredients"]["coffee"]
                    return_change(drink_type, total_paid)
                else:
                    print(f"Not enough paid for a {order}.")
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
                total_paid = take_coins()
                if check_cost(order, total_paid):
                    resources['water'] = resources['water'] - MENU["cappuccino"]["ingredients"]["water"]
                    resources['milk'] = resources['milk'] - MENU["cappuccino"]["ingredients"]["milk"]
                    resources['coffee'] = resources['coffee'] - MENU["cappuccino"]["ingredients"]["coffee"]
                    return_change(drink_type, total_paid)
                else:
                    print(f"Not enough paid for a {order}.")
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
        return False
    elif drink_type == 'latte' and payment < int(MENU['latte']['cost']):
        return False
    elif drink_type == 'cappuccino' and payment < int(MENU['cappuccino']['cost']):
        return False
    else:
        return True


def return_change(drink_type, payment):
    if drink_type == 'espresso':
        print(f"Payment successful! Your change is ${round(payment - int(MENU['espresso']['cost']), 2)}")
    elif drink_type == 'latte':
        print(f"Payment successful! Your change is ${round(payment - int(MENU['latte']['cost']), 2)}")
    elif drink_type == 'cappuccino':
        print(f"Payment successful! Your change is ${round(payment - int(MENU['cappuccino']['cost']), 2)}")
    else:
        print("Payment error.")


order = input("What would you like? Type espresso, latte, or cappuccino and press Enter. Type report "
              "to get a report on machine resources or quit to end the program. ")

if order == 'quit':
    make_drink(order)
else:
    while order != 'quit':
        make_drink(order)
        order = input("What would you like? (espresso/latte/cappuccino) ")
        if order == 'quit':
            make_drink(order)


