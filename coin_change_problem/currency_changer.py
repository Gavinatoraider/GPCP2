#coin change problem: currrency_changer Gavin Pierce

"""program uses four currency
USD
Euro
Yen
British pound
this is housed in the money csv
"""

currency_type=["USD","Euro","Yen","British Pound"]

print("welcome to the currency changer")

coin_type=input("what is the currency you trying to exchange from? (USD, Euro, Yen and British pound. these are the only valid options) (if you have the same to it will try to exchange to the smallest form of change) ")

if coin_type not in currency_type:
    print("you need a valid currency.")

coin_change_amount=input("what is the amount you of money you want to use in ", coin_type, "?")

