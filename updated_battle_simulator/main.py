import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
from faker import Faker

# Initialize Faker
fake = Faker()

# ==== Classes ====

class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type
        self.effect = effect

    def __str__(self):
        return f"{self.name} ({self.item_type})"

class Character:
    def __init__(self, name, char_class, health, strength, defense, speed, level=1, experience=0):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.strength = strength
        self.defense = defense
        self.speed = speed
        self.level = level
        self.experience = experience
        self.inventory = []

    def calculate_damage(self, target):
        base_damage = self.strength - target.defense
        return max(base_damage, 1)

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= 100:
            self.level += 1
            self.experience -= 100
            print(f"{self.name} leveled up! Now at level {self.level}.")

    def special_ability(self, target):
        if self.char_class == "warrior":
            extra_damage = 10
            target.health = max(0, target.health - extra_damage)
            print(f"{self.name} uses Power Strike! {target.name} takes {extra_damage} extra damage.")
        elif self.char_class == "mage":
            extra_damage = 15
            target.health = max(0, target.health - extra_damage)
            print(f"{self.name} casts Fireball! {target.name} takes {extra_damage} fire damage.")
        elif self.char_class == "rogue":
            extra_damage = self.speed
            target.health = max(0, target.health - extra_damage)
            print(f"{self.name} uses Shadow Strike! {target.name} takes {extra_damage} damage based on speed.")

    def add_item(self, item):
        self.inventory.append(item)

# ==== Helper Functions ====

def save_character_to_csv(character):
    with open('charatures.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        inventory_data = [item.name for item in character.inventory]
        writer.writerow([character.name, character.char_class, character.health, character.strength,
                         character.defense, character.speed, character.level, character.experience,
                         ";".join(inventory_data)])

def load_characters_from_csv():
    characters = []
    try:
        with open('charatures.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, char_class, health, strength, defense, speed, level, experience, inventory_data = row
                character = Character(name, char_class, int(health), int(strength), int(defense),
                                      int(speed), int(level), int(experience))
                if inventory_data:
                    item_names = inventory_data.split(";")
                    for item_name in item_names:
                        if item_name == "Sword of Power":
                            character.add_item(Item("Sword of Power", "weapon", {"strength": 5}))
                        elif item_name == "Steel Shield":
                            character.add_item(Item("Steel Shield", "armor", {"defense": 3}))
                characters.append(character)
    except FileNotFoundError:
        print("No saved characters found.")
    return characters

# ==== Game Features ====

def create_character():
    print("\nLet's create your character!")
    name = input("Enter your character's name: ")
    char_class = input("Choose your character's class (warrior, mage, rogue): ").lower()
    while char_class not in ["warrior", "mage", "rogue"]:
        print("Invalid class choice. Please choose from 'warrior', 'mage', or 'rogue'.")
        char_class = input("Choose your character's class (warrior, mage, rogue): ").lower()

    health = int(input("Enter your character's health: "))
    strength = int(input("Enter your character's strength: "))
    defense = int(input("Enter your character's defense: "))
    speed = int(input("Enter your character's speed: "))

    new_character = Character(name, char_class, health, strength, defense, speed)
    sword = Item("Sword of Power", "weapon", {"strength": 5})
    new_character.add_item(sword)

    save_character_to_csv(new_character)
    print(f"\nCharacter {new_character.name} has been created and saved. Ready for adventure!")

def view_characters():
    characters = load_characters_from_csv()
    if characters:
        print("\nHere are your saved characters:")
        for idx, character in enumerate(characters):
            print(f"{idx + 1}. {character.name} ({character.char_class})")
            print(f"   Health: {character.health}, Strength: {character.strength}, Defense: {character.defense}, Speed: {character.speed}")
            print(f"   Level: {character.level}, Experience: {character.experience}\n")
    else:
        print("Oops! You don't have any saved characters yet. Create one first!")

def battle():
    characters = load_characters_from_csv()
    if len(characters) >= 2:
        print("\nLet's get ready for a battle!")
        for idx, character in enumerate(characters):
            print(f"{idx + 1}. {character.name} ({character.char_class})")

        p1_idx = int(input("Choose your first character (number): ")) - 1
        p2_idx = int(input("Choose your second character (number): ")) - 1

        character1 = characters[p1_idx]
        character2 = characters[p2_idx]

        print(f"\n{character1.name} is battling {character2.name}!")

        while character1.health > 0 and character2.health > 0:
            use_special = input(f"{character1.name}, use special ability? (y/n): ")
            if use_special.lower() == "y":
                character1.special_ability(character2)
            else:
                damage1 = character1.calculate_damage(character2)
                character2.health = max(0, character2.health - damage1)
                print(f"{character1.name} attacks {character2.name} for {damage1} damage!")

            if character2.health <= 0:
                print(f"{character2.name} has been defeated!")
                character1.gain_experience(50)
                break

            use_special = input(f"{character2.name}, use special ability? (y/n): ")
            if use_special.lower() == "y":
                character2.special_ability(character1)
            else:
                damage2 = character2.calculate_damage(character1)
                character1.health = max(0, character1.health - damage2)
                print(f"{character2.name} attacks {character1.name} for {damage2} damage!")

            if character1.health <= 0:
                print(f"{character1.name} has been defeated!")
                character2.gain_experience(50)
                break

        save_character_to_csv(character1)
        save_character_to_csv(character2)
    else:
        print("You need at least two characters to battle. Create more characters and try again!")

def generate_random_character():
    name = fake.first_name()
    backstory = fake.sentence(nb_words=12)
    char_class = random.choice(["warrior", "mage", "rogue"])
    health = random.randint(60, 120)
    strength = random.randint(10, 30)
    defense = random.randint(5, 25)
    speed = random.randint(5, 25)

    new_char = Character(name, char_class, health, strength, defense, speed)
    new_char.backstory = backstory
    sword = Item("Sword of Power", "weapon", {"strength": 5})
    new_char.add_item(sword)

    save_character_to_csv(new_char)
    print(f"\n🎲 Generated character: {name} the {char_class}")
    print(f"Backstory: {backstory}")

# ==== Visualization (Matplotlib) ====

def display_character_stats(character):
    stats = {
        'Health': character.health,
        'Strength': character.strength,
        'Defense': character.defense,
        'Speed': character.speed
    }

    # Plotting bar chart for character stats
    plt.figure(figsize=(6, 4))  # Optional: Makes the plot bigger and more readable
    plt.bar(stats.keys(), stats.values(), color=['blue', 'green', 'red', 'purple'])
    
    # Adding titles and labels
    plt.title(f"{character.name}'s Stats", fontsize=14)
    plt.xlabel("Attributes", fontsize=12)
    plt.ylabel("Values", fontsize=12)
    
    # Display the plot
    plt.tight_layout()  # This adjusts the layout to ensure no overlapping text
    plt.show()  # Ensure this is called to actually render the plot

# ==== Statistical Analysis (Pandas) ====

def analyze_character_data():
    characters = load_characters_from_csv()
    if characters:
        # Convert characters list to DataFrame for analysis
        data = {
            'Name': [char.name for char in characters],
            'Health': [char.health for char in characters],
            'Strength': [char.strength for char in characters],
            'Defense': [char.defense for char in characters],
            'Speed': [char.speed for char in characters]
        }
        
        df = pd.DataFrame(data)
        print("\nCharacter Data Analysis")
        print(f"Mean Health: {df['Health'].mean():.2f}")
        print(f"Max Strength: {df['Strength'].max()}")
        print(f"Min Speed: {df['Speed'].min()}")

        # Display the DataFrame
        print(df)

    else:
        print("No characters found to analyze.")

# ==== Main ====

def main():
    print("Welcome to the RPG Adventure!")

    while True:
        choice = input("""
What would you like to do today? 
1. Create a new character
2. View existing characters
3. Battle with your characters
4. Create a random character (Faker)
5. Display character stats (Matplotlib)
6. Analyze character data (Pandas)
7. Exit the game
Choose an option: """)

        if choice == "1":
            create_character()
        elif choice == "2":
            view_characters()
        elif choice == "3":
            battle()
        elif choice == "4":
            generate_random_character()
        elif choice == "5":
            char_idx = int(input("Enter the character number to display stats: ")) - 1
            characters = load_characters_from_csv()
            if 0 <= char_idx < len(characters):
                display_character_stats(characters[char_idx])
            else:
                print("Invalid character selection.")
        elif choice == "6":
            analyze_character_data()
        elif choice == "7":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

# Run the game
main()
