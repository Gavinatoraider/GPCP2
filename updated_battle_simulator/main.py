import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from faker import Faker

# Initialize Faker instance for random name generation
fake = Faker()

# Classes for Items and Characters

class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type  # e.g., "weapon", "armor"
        self.effect = effect  # A dictionary of stat changes, e.g., {"strength": 5}

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
        self.inventory = []  # This is the character's inventory, which holds items

    def calculate_damage(self, target):
        base_damage = self.strength - target.defense
        return max(base_damage, 1)

    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= 100:
            self.level += 1
            self.experience -= 100
            print(f"{self.name} leveled up! Now at level {self.level}.")

    def add_item(self, item):
        self.inventory.append(item)

    def display_stats(self):
        return f"Name: {self.name}, Class: {self.char_class}, Health: {self.health}, Strength: {self.strength}, Defense: {self.defense}, Speed: {self.speed}"

# Main functions for RPG functionality

def main():
    print("Welcome to the RPG Adventure!")
    
    while True:
        choice = input("""What would you like to do? 
                     1. Create a new character
                     2. View existing characters
                     3. Battle with your characters
                     4. Character stat analysis
                     5. Forecast character growth
                     6. Explore the game world
                     7. Exit the game
                     Choose an option: """)

        if choice == "1":
            create_character()
        elif choice == "2":
            view_characters()
        elif choice == "3":
            battle()
        elif choice == "4":
            analyze_stats()
        elif choice == "5":
            forecast_growth()
        elif choice == "6":
            explore_world()
        elif choice == "7":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def create_character():
    name = fake.name()
    char_class = input("Choose your character's class (warrior, mage, rogue): ").lower()
    while char_class not in ["warrior", "mage", "rogue"]:
        print("Invalid class. Choose from 'warrior', 'mage', 'rogue'.")
        char_class = input("Choose your character's class: ").lower()

    health = random.randint(50, 100)
    strength = random.randint(5, 20)
    defense = random.randint(1, 10)
    speed = random.randint(5, 15)

    new_character = Character(name, char_class, health, strength, defense, speed)

    sword = Item("Sword of Power", "weapon", {"strength": 5})
    new_character.add_item(sword)

    save_character_to_csv(new_character)
    print(f"Character {new_character.name} has been created!")

def save_character_to_csv(character):
    with open('characters.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        inventory_data = [item.name for item in character.inventory]
        writer.writerow([character.name, character.char_class, character.health, character.strength, character.defense, character.speed, character.level, character.experience, ";".join(inventory_data)])

def load_characters_from_csv():
    characters = []
    try:
        with open('characters.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, char_class, health, strength, defense, speed, level, experience, inventory_data = row
                character = Character(name, char_class, int(health), int(strength), int(defense), int(speed), int(level), int(experience))
                if inventory_data:
                    item_names = inventory_data.split(";")
                    for item_name in item_names:
                        if item_name == "Sword of Power":
                            character.add_item(Item("Sword of Power", "weapon", {"strength": 5}))
                characters.append(character)
    except FileNotFoundError:
        print("No saved characters found.")
    return characters

def view_characters():
    characters = load_characters_from_csv()
    if characters:
        for character in characters:
            print(character.display_stats())
    else:
        print("No characters found. Create one first.")

def battle():
    characters = load_characters_from_csv()
    if len(characters) >= 2:
        print("\nChoose two characters to battle:")
        for idx, character in enumerate(characters):
            print(f"{idx + 1}. {character.name} ({character.char_class})")

        p1_idx = int(input("Select first character: ")) - 1
        p2_idx = int(input("Select second character: ")) - 1

        character1 = characters[p1_idx]
        character2 = characters[p2_idx]

        print(f"\n{character1.name} is battling {character2.name}!")
        while character1.health > 0 and character2.health > 0:
            damage1 = character1.calculate_damage(character2)
            character2.health -= damage1
            print(f"{character1.name} attacks {character2.name} for {damage1} damage!")

            if character2.health <= 0:
                print(f"{character2.name} has been defeated!")
                character1.gain_experience(50)
                break

            damage2 = character2.calculate_damage(character1)
            character1.health -= damage2
            print(f"{character2.name} attacks {character1.name} for {damage2} damage!")

            if character1.health <= 0:
                print(f"{character1.name} has been defeated!")
                character2.gain_experience(50)
                break

        save_character_to_csv(character1)
        save_character_to_csv(character2)
    else:
        print("You need at least two characters to battle!")

def analyze_stats():
    characters = load_characters_from_csv()
    if characters:
        data = {
            "Name": [char.name for char in characters],
            "Health": [char.health for char in characters],
            "Strength": [char.strength for char in characters],
            "Defense": [char.defense for char in characters],
            "Speed": [char.speed for char in characters]
        }
        df = pd.DataFrame(data)
        print(df.describe())
        df.plot(kind="bar", figsize=(10, 6))
        plt.title('Character Stats')
        plt.xlabel('Character')
        plt.ylabel('Stat Value')
        plt.show()
    else:
        print("No characters found.")

def forecast_growth():
    level_increase = int(input("Enter the number of levels to forecast: "))
    characters = load_characters_from_csv()
    if characters:
        for character in characters:
            future_health = character.health + (level_increase * 10)
            future_strength = character.strength + (level_increase * 2)
            future_defense = character.defense + (level_increase * 1)
            future_speed = character.speed + (level_increase * 1)
            print(f"{character.name}'s growth over {level_increase} levels:")
            print(f"Future Health: {future_health}, Strength: {future_strength}, Defense: {future_defense}, Speed: {future_speed}")
            
            # Simple forecast visualization
            forecast_data = {
                "Level": list(range(1, level_increase + 1)),
                "Health": [character.health + i * 10 for i in range(level_increase)],
                "Strength": [character.strength + i * 2 for i in range(level_increase)],
                "Defense": [character.defense + i * 1 for i in range(level_increase)],
                "Speed": [character.speed + i * 1 for i in range(level_increase)]
            }

            df = pd.DataFrame(forecast_data)
            df.plot(x='Level', y=['Health', 'Strength', 'Defense', 'Speed'], kind='line', figsize=(10, 6))
            plt.title(f'{character.name} Growth Forecast')
            plt.xlabel('Levels')
            plt.ylabel('Stat Value')
            plt.show()

def explore_world():
    print("Exploring the world...")
    world_data = {
        "Location": ["Forest", "Mountain", "Castle", "Village"],
        "NPC": ["Orc", "Wizard", "Knight", "Villager"],
        "Quest": ["Find treasure", "Defeat dragon", "Rescue princess", "Gather herbs"]
    }
    df = pd.DataFrame(world_data)
    print(df)
    df.plot(kind='scatter', x='Location', y='Quest', figsize=(10, 6), color='blue')
    plt.title('Game World Map')
    plt.xlabel('Location')
    plt.ylabel('Quest')
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
