# Coin Change Problem: Main File - Gavin Pierce

import csv

CURRENCY_OPTIONS = {
    "1": "USD",
    "2": "Euro",
    "3": "Yen",
    "4": "British Pound"
}

def load_denominations(currency_name):
    try:
        with open('currency.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Strip spaces and handle quoted currency names (remove quotes)
                currency_in_csv = row[0].strip().lower().replace('"', '')  # Handle quotes and spaces
                if currency_in_csv == currency_name.lower():
                    all_data = row[1:]
                    denominations = []
                    for item in all_data:
                        try:
                            name, value = item.split('-')
                            denominations.append((name.strip(), int(value)))
                        except ValueError:
                            continue
                    return sorted(denominations, key=lambda x: -x[1])
        print(f"Currency '{currency_name}' not found in the file.")
        return []
    except FileNotFoundError:
        print("Error: 'currency.csv' not found.")
        return []


def calculate_change(amount, currency):
    denominations = load_denominations(currency)
    if not denominations:
        return []

    total_cents = int(round(float(amount) * 100))
    result = []

    for name, value in denominations:
        count = total_cents // value
        if count > 0:
            result.append((name, count))
            total_cents -= count * value

    return result

def main():
    print("💰 Welcome to the Currency Changer 💰")
    
    while True:
        choice = input("""\nWhat would you like to do?
1. View supported currencies
2. Make change
3. Exit
Choose an option (1, 2, or 3): """).strip()

        if choice == "1":
            print("\nSupported currencies:")
            for key, val in CURRENCY_OPTIONS.items():
                print(f"{key}. {val}")
        elif choice == "2":
            print("\nSelect the currency:")
            for key, val in CURRENCY_OPTIONS.items():
                print(f"{key}. {val}")
            currency_choice = input("Choose a currency (1-4): ").strip()
            currency = CURRENCY_OPTIONS.get(currency_choice)

            if not currency:
                print("Invalid choice. Please choose a number from 1 to 4.")
                continue

            amount = input(f"Enter the amount in {currency} (e.g., 99.99): ").strip()
            try:
                amount = float(amount)
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                change = calculate_change(amount, currency)
                if change:
                    print(f"\nChange for {amount} {currency}:")
                    for name, count in change:
                        print(f"{count} x {name}")
                else:
                    print("Could not calculate change.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

# Running the main function
if __name__ == "__main__":
    main()
