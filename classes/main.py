#classes and objects in python, Gavin Pierce

sentence = "the quick brown fox jumped over the lazy dog"

print(sentence.upper())

class subject:
    def __init__(self, content, teacher, period, room):
        self.content = content
        self.period = period
        self.teacher = teacher
        self.room = room

        def __str__(self):
            return f'Name: {self.content}\nPeriod: {self.period}\nTeacher: {self.teacher}\nRoom: {self.room}'


first = subject("CS Principles", 1, "LaRose", 200)
second = subject("CP2", 2, "LaRose", 200)

print(first.content)
print(second.content)

#what is a class?

    #a class is a blueprint for an object

#what is an object?

    #is the specific instance

#how do classes relate to objects

class pokemon:
    def __init__(self, name,species,hp,dmg ):
        self.name= name
        self.species= species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f'{self.name} is a {self.species} and the have {self.hp} HP and do {self.dmg} amount of damage in battle.'
    
    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f'{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}.')

            if opponent.hp <=0:
                print(f'{opponent.name} is knocked out. {self.name} wins')
            else:
                self.hp -= opponent.dmg
                print(f'{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}.')
                
                if self.hp <= 0:
                    print(f'{self.name} is knocked out. {opponent.name} wins')

fluffy = pokemon("Fluffy", "Arcanine", 280, 110)
slimy = pokemon("slimy", "Ditto", 100, 70)
spiky = pokemon("spiky", "jolteon", 150, 100)


fluffy.battle(spiky)
slimy.battle(spiky)