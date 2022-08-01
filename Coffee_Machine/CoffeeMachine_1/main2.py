from data import MENU, resources, profit

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    quarters_inserted = int(input("how many quarters?: ")) * 0.25
    dimes_inserted = int(input("how many dimes?: ")) * 0.10
    nickles_inserted = int(input("how many nickles?: ")) * 0.05
    pennies_inserted = int(input("how many pennies?: ")) * 0.01
    total_inserted = quarters_inserted + \
                    dimes_inserted + \
                    nickles_inserted + \
                    pennies_inserted
    return total_inserted

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice}. Enjoy!")
        

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # check resources
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, profit):
                make_coffee(drink, drink["ingredients"])
        
        