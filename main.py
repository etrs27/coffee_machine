from data import MENU, resources


# TODO 1. Print report
# TODO 2. Check resources
# TODO 3. Process coins
# TODO 4. Check transaction successful?
# TODO 5. Make coffee


def report():
    """Returns the quantity of the resources and total coins."""
    items = resources
    print(f"Water:{items["water"]} ml \nMilk:{items["milk"]} ml \nCoffee:{items["coffee"]} g \nMoney: ${total_coins}")


def supplies(drink):
    """Checks if there is enough ingredients to make the beverage."""
    drink = MENU[drink]["ingredients"]
    items = resources
    for ingredient in drink:
        if drink[ingredient] > items[ingredient]:
            print(f"Sorry, not enough {ingredient}.")
        else:
            return True


def payment():
    """Calculates payment."""
    quarters = int(input("How many quarters? ")) * .25
    dimes = int(input("How many dimes? ")) * .10
    nickels = int(input("How many nickels? ")) * .05
    pennies = int(input("How many pennies? ")) * .01
    return round(quarters + dimes + nickels + pennies, 2)


def sufficient_funds(item, pay):
    """Checks if payment is successful or not."""
    cost = MENU[item]["cost"]
    drink = MENU[item]["ingredients"]
    items = resources
    if pay < cost:
        print("Insufficient funds. Money refunded.")
        return False
    else:
        for ingredient in drink:
            items[ingredient] -= drink[ingredient]
        print(f"Here is your change {round(pay - cost, 2)}.")
        print(f"Here is your {item}. Enjoy!")
        return True


total_coins = 0
machine_power = True
while machine_power:
    select = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if select == "off":
        machine_power = False
    elif select == "report":
        report()
    elif select == "espresso" or select == "latte" or select == "cappuccino":
        if supplies(select):
            coins = payment()
            if sufficient_funds(select, coins):
                total_coins += MENU[select]["cost"]

