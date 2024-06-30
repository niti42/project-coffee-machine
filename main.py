MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money_earned = 0
# Money value:
# Penny is worth 1 cent = $0.01
# Nickel is worth 5 cents = $0.05
# Dime is worth 10 cents = $0.10
# Quarter is worth 25 cents = $0.25


def take_instruction():
    response = input("What would you like? (espresso/latte/cappuccino):")
    return response


def ask_user_for_money():
    try:
        quarters = int(input("how many quarters?"))
        dime = int(input("how many dimes?"))
        nickel = int(input("how many nickels?"))
        penny = int(input("how many pennies?"))

        total_money = quarters*0.25+dime*0.1+nickel*0.05+penny*0.01
        return total_money

    except:
        print("Enter only numbers")
        return ask_user_for_money()


def money_check(money, coffee):
    coffee_cost = MENU.get(coffee).get('cost')
    if money >= coffee_cost:
        change = money - coffee_cost
        return True, change
    return False, money


def resource_check(coffee):
    ingredients = MENU.get(coffee).get('ingredients')
    not_enough_msg = []
    for item in ingredients:
        if resources[item] >= ingredients[item]:
            # update resource
            resources[item] = resources[item] - ingredients[item]
        else:
            not_enough_msg.append(f"Sorry there is not enough {item}")

    is_enough = (not len(not_enough_msg) > 0)

    return is_enough, not_enough_msg


def success_message(drink, change):
    display_msg = f"""
Here is ${round(change,2)} in change."
Here is your {drink} ☕. Enjoy!
"""
    print(display_msg)


def print_report():
    report = f"""
Water : {resources.get('water')}ml
Milk : {resources.get('water')}ml
Coffee : {resources.get('water')}g
Money : ${money_earned}
"""
    print(report)


def make_coffee(resp):
    global money_earned
    money_inserted = ask_user_for_money()
    if money_inserted is not None:
        money_ok, change = money_check(money_inserted, resp)
    if money_ok:
        resource_ok, shortage_report = resource_check(resp)
        if resource_ok:
            success_message(resp, change)
            # update money earned
            money_earned += money_inserted-change
        else:
            for shortage_msg in shortage_report:
                print(shortage_msg)

    else:
        print("Sorry that's not enough money. Money refunded.")


def coffee_machine():
    power_switch = True
    while power_switch:
        resp = take_instruction()
        if resp in MENU:
            make_coffee(resp)

        elif resp == "report":
            print_report()

        elif resp == 'off':
            power_switch = False

        else:
            print("Please enter appropriate command")


if __name__ == "__main__":
    coffee_machine()
