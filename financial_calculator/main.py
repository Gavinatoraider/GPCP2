# Gavin Pierce Financial Calculator
# This is the main file and will have the major amounts of code.

def main():
    like_to_do = input("""What would you like to do? 
                     1 Interest Calculator
                     2 Budget Allocator
                     3 Saving Goal
                     4 Price Discounter
                     5 Tipper
                     6 Stop\n""")
    
    while like_to_do != "6":
        if like_to_do == "1":
            like_to_do = intrest_calculator()
        elif like_to_do == "2":
            like_to_do = budget_allocator()
        elif like_to_do == "3":
            like_to_do = saving_goal()
        elif like_to_do == "4":
            like_to_do = price_discounter()
        elif like_to_do == "5":
            like_to_do = tipper()
        else:
            print("Invalid choice, please select again.")
            like_to_do = input("""What would you like to do? 
                     1 Interest Calculator
                     2 Budget Allocator
                     3 Saving Goal
                     4 Price Discounter
                     5 Tipper
                     6 Stop\n""")

def intrest_calculator():
    Acount_Amount = int(input("What is your bank account's amount right now? "))
    Amount_with_intrest = Acount_Amount * 0.06
    print(f"{Amount_with_intrest} is your amount of interest.")
    intrest_Amount = Amount_with_intrest + Acount_Amount
    print(f"{intrest_Amount} is your amount with interest.")
    
    return input_choice()

def budget_allocator():
    monthly_income = int(input("What is your income per month? "))
    # Food: 15%
    food = monthly_income * 0.15
    # Entertainment: 5%
    entertainment = monthly_income * 0.05
    # Rent: 30%
    rent = monthly_income * 0.30
    # Taxes: 4.85%
    taxes = monthly_income * 0.0485
    # Savings: 20%
    saving = monthly_income * 0.20
    # Other: 25.15%
    other = monthly_income * 0.2515
    
    print(f"You can spend {food} on food.")
    print(f"You can spend {entertainment} on entertainment.")
    print(f"You can spend {rent} on rent.")
    print(f"You can spend {saving} on savings.")
    print(f"You can spend {other} on other things.")
    
    return input_choice()

#need to apply for coast of item not income?

def saving_goal():
    item_price = int(input("What is the price of the item? "))
    how_long = int(input("How many weeks will you be saving for? "))
    saving_amount = item_price // how_long
    print(f"You will need to save {saving_amount} per week.")
    
    return input_choice()

def price_discounter():
    item_price = int(input("What is the price of the item? "))
    item_discount = int(input("What is the discount? "))
    # Discounts price
    percent_maker = item_discount / 100
    discounted_price = item_price * (1 - percent_maker)
    print(f"The item's price after discount is ${discounted_price}.")
    
    return input_choice()

def tipper():
    meal_price = int(input("What was the price of your meal? "))
    tip_amount = meal_price * 0.15
    print(f"You should tip ${tip_amount}.")
    
    return input_choice()

def input_choice():
    return input("""What would you like to do? 
                     1 Interest Calculator
                     2 Budget Allocator
                     3 Saving Goal
                     4 Price Discounter
                     5 Tipper
                     6 Stop\n""")

# Run the main function
main()
