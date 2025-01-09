# Gavin Pierce Financial Calculator
#this is the main file and will hvae the major amounts of code.
def main():
    Acount_Amount=int(input("what is your back acounts amount right now? "))
    #this will caslculate your intrest.
    def intrest_calculator():
        
        Amount_with_intrest=Acount_Amount*.06
        print(Amount_with_intrest, "is you amount of intrest")
        intrest_Amount=Amount_with_intrest+Acount_Amount
        print(f"{intrest_Amount} this is your amount with incest.")

    intrest_calculator()
    pass
main()