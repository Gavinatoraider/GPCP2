# RPG Game - Main File

# This is where the game starts and the user navigates the options

def main():
    print("Welcome to the RPG Adventure!")
    
    # Main menu loop
    while True:
        # Show the main menu options
        choice = input("""
        What would you like to do today? 
        1. Create a new character
        2. View existing characters
        3. Battle with your characters
        4. Exit the game
        Choose an option: """)

        if choice == "1":
            create_character()  # Call to create a new character
        elif choice == "2":
            view_characters()  # Call to view existing characters
        elif choice == "3":
            battle()  # Call to battle two characters
        elif choice == "4":
            print("Thank you for playing! Goodbye!")  # Exit the game
            break
        else:
            print("Oops! That's not a valid choice. Try again!")  # Invalid input prompt


def create_character():
    # Function to create a new character
    print("\nLet's create your character!")
    name = input("Enter your character's name: ")
    
    # Character class input with validation
    char_class = input("Choose your character's class (warrior, mage, rogue): ").lower()
    while char_class not in ["warrior", "mage", "rogue"]:
        print("Invalid class choice. Please choose from 'warrior', 'mage', or 'rogue'.")
        char_class = input("Choose your character's class (warrior, mage, rogue): ").lower()

    # Get character stats (health, strength, defense, speed)
    health = int(input("Enter your character's health: "))
    strength = int(input("Enter your character's strength: "))
    defense = int(input("Enter your character's defense: "))
    speed = int(input("Enter your character's speed: "))

    # Create the character
    new_character = Character(name, char_class, health, strength, defense, speed)

    # Add a default item (Sword of Power)
    sword = Item("Sword of Power", "weapon", {"strength": 5})
    new_character.add_item(sword)

    # Save the character to CSV for later retrieval
    save_character_to_csv(new_character)

    # Confirmation message
    print(f"\nCharacter {new_character.name} has been created and saved. Ready for adventure!")


def view_characters():
    # Function to view all saved characters
    characters = load_characters_from_csv()
    if characters:
        print("\nHere are your saved characters:")
        for idx, character in enumerate(characters):
            # Display each character's details
            print(f"{idx + 1}. {character.name} ({character.char_class})")
            print(f"   Health: {character.health}, Strength: {character.strength}, Defense: {character.defense}, Speed: {character.speed}")
            print(f"   Level: {character.level}, Experience: {character.experience}\n")
    else:
        print("Oops! You don't have any saved characters yet. Create one first!")


def battle():
    # Function to initiate a battle between two characters
    characters = load_characters_from_csv()
    if len(characters) >= 2:
        print("\nLet's get ready for a battle!")
        print("Select two characters to fight:")
        for idx, character in enumerate(characters):
            print(f"{idx + 1}. {character.name} ({character.char_class})")
        
        # Get player input to select the characters for battle
        p1_idx = int(input("Choose your first character (number): ")) - 1
        p2_idx = int(input("Choose your second character (number): ")) - 1
        
        # Get the selected characters for battle
        character1 = characters[p1_idx]
        character2 = characters[p2_idx]
        
        # Inform the players about the battle
        print(f"\n{character1.name} is battling {character2.name}!")

        # Battle loop - characters attack each other until one is defeated
        while character1.health > 0 and character2.health > 0:
            # Character 1's turn
            use_special = input(f"{character1.name}, do you want to use your special ability? (y/n): ")
            if use_special.lower() == "y":
                character1.special_ability(character2)  # Special ability used
            else:
                damage1 = character1.calculate_damage(character2)  # Normal attack
                character2.health -= damage1
                print(f"{character1.name} attacks {character2.name} for {damage1} damage!")
            
            # Check if character 2 is defeated
            if character2.health <= 0:
                print(f"{character2.name} has been defeated!")
                character1.gain_experience(50)  # Character 1 gains experience for winning
                break

            # Character 2's turn
            use_special = input(f"{character2.name}, do you want to use your special ability? (y/n): ")
            if use_special.lower() == "y":
                character2.special_ability(character1)  # Special ability used
            else:
                damage2 = character2.calculate_damage(character1)  # Normal attack
                character1.health -= damage2
                print(f"{character2.name} attacks {character1.name} for {damage2} damage!")

            # Check if character 1 is defeated
            if character1.health <= 0:
                print(f"{character1.name} has been defeated!")
                character2.gain_experience(50)  # Character 2 gains experience for winning
                break

        # After the battle, save the updated character data to CSV
        save_character_to_csv(character1)
        save_character_to_csv(character2)
    else:
        print("You need at least two characters to battle. Create more characters and try again!")


def save_character_to_csv(character):
    # Save the character and their inventory to a CSV file
    with open('characters.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Save character data and their items (inventory)
        inventory_data = [item.name for item in character.inventory]
        writer.writerow([character.name, character.char_class, character.health, character.strength, character.defense, character.speed, character.level, character.experience, ";".join(inventory_data)])


def load_characters_from_csv():
    # Load all saved characters from CSV
    characters = []
    try:
        with open('characters.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, char_class, health, strength, defense, speed, level, experience, inventory_data = row
                # Load character data
                character = Character(name, char_class, int(health), int(strength), int(defense), int(speed), int(level), int(experience))
                
                # Load character's inventory
                if inventory_data:
                    item_names = inventory_data.split(";")
                    for item_name in item_names:
                        # Add predefined items based on inventory data
                        if item_name == "Sword of Power":
                            character.add_item(Item("Sword of Power", "weapon", {"strength": 5}))
                        elif item_name == "Steel Shield":
                            character.add_item(Item("Steel Shield", "armor", {"defense": 3}))
                
                characters.append(character)
    except FileNotFoundError:
        print("No saved characters found.")
    return characters


class Item:
    def __init__(self, name, item_type, effect):
        self.name = name
        self.item_type = item_type  # e.g., "weapon", "armor"
        self.effect = effect  # A dictionary of stat changes, e.g., {"strength": 5}

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
        self.inventory = []  # This is the character's inventory, which holds items

    def calculate_damage(self, target):
        # Basic damage calculation (strength - target defense)
        base_damage = self.strength - target.defense
        return max(base_damage, 1)  # Minimum damage of 1, even if the defense is higher

    def gain_experience(self, amount):
        # Leveling up and experience gain logic
        self.experience += amount
        while self.experience >= 100:  # Level up every 100 experience points
            self.level += 1
            self.experience -= 100
            print(f"{self.name} leveled up! Now at level {self.level}.")

    def special_ability(self, target):
        # Special abilities for different character classes
        if self.char_class == "warrior":
            extra_damage = 10  # Warrior's power attack
            target.health -= extra_damage
            print(f"{self.name} uses Power Strike! {target.name} takes {extra_damage} extra damage.")
        elif self.char_class == "mage":
            extra_damage =

main()