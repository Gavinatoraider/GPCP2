# Gavin Pierce Financial Calculator
#this is the main file and will hvae the major amounts of code.
def main():
    Acount_Amount=int(input("what is your bank acounts amount right now? "))
    #this will caslculate your intrest.

def intrest_calculator():
    global Acount_Amount
    Amount_with_intrest=Acount_Amount*.06
    print(Amount_with_intrest, "is you amount of intrest")
    intrest_Amount=Amount_with_intrest+Acount_Amount
    print(f"{intrest_Amount} this is your amount with intrest.")
    pass

def budget_allocator():
    global monthly_income= int(input("what is you income per mounth? "))
    #food: 15%
    food=monthly_income*.15
    #entertainment: 5%
    entertainment=monthly_income*.05
    #rent: 30%
    rent=monthly_income*.3
    #taxes: 4.85%
    taxes=monthly_income*.0485
    #saveings: 20%
    saveing=monthly_income*.2
    #other: 25.15%
    other=monthly_income*.2515
    print("you can spend ",food, " on food")
    print("you can spend ",entertainment, "ontertainment.")
    print("you can spend ",rent," on rent")
    print("you can spend ",saveings," on saveings")
    print("you can spend ", ," on other things")
    pass   
    
main()