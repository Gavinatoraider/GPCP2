#coin change problem: Main Gavin Pierce

import currency_changer

"""program uses four currency
USD
Euro
Yen
British pound
this is housed in the money csv
"""

"""
USD amounts
coin: penny (1 cent), nickel (5 cents), dime (10 cents), quarter (25 cents), half-dollar (50 cents), and dollar coin (100 cents)
dollar: $1, $2, $5, $10, $20, $50, $100 

Euro amounts
coin: €2, €1, 50c, 20c, 10c, 5c, 2c and 1c
bills: €5, €10, €20, €50, €100, €200 and €500

Yen amounts
coins:  one-yen, five-yen, 10-yen, 50-yen, 100-yen and 500-yen
bills: 1,000 yen, 2,000 yen, 5,000 yen, and 10,000 yen

British Pound
coins: 1p, 2p, 5p, 10p, 20p, 50p, £1 and £2.
Bills: £5, £10, £20, and £50
"""

def main():
    while 4:
        like_to_do=input("""what would you like to do?
                         1. see curent currencies
                         2. see curency exchange rates
                         3. change currencies
                         4. leave.
                         chose one of the numbers. (ex: 1 to see current currencies.) """)
        if like_to_do == "1":
            print("the current currenies are USD, Euro, Yen and the British Pound.")
        elif like_to_do == "2":
            print("""the current excahnge rates are:
            USD to EUR: 1 USD = .9264 EUR
            USD to British Pound: 1 USD = 0.7723 GBP
            Usd to Yen: 1 USD = 110.42 JPY""")
        elif like_to_do == "3":
            currency_changer
        elif like_to_do == "4":
                break
        else:
             print("you need valide option. remeber choose the number of the thing you want to do.")

main()