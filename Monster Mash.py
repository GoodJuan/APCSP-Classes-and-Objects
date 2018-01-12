army1 = []
army2 = []

class Weapon:
    weapons = ["Sword", "Bow and Arrow", "Slingshot"]

    weapon = ""
    damage = 0
    critChance = 0
    critMulti = 0

    def __init__(self, weaponChoice):
        #sword
        if weaponChoice is 1:
            self.damage = 18
            self.critChance = 0.2
            self.critMulti = 1.5
            self.weapon = "Sword"
        #Bow
        elif weaponChoice is 2:
            self.damage = 9
            self.critChance = 0.1
            self.critMulti = 2
            self.weapon = "Bow and Arrow"
        #Slingshot
        elif weaponChoice is 3:
            self.damage = 1
            self.critChance = 0.05
            self.critMulti = 4
            self.weapon = "Slingshot"

    def getWeapon(self):
        return self.weapon



class Monster:
    health = 0
    typeOfMonster = ""
    attack = 0
    weapon = Weapon("")

    monsters = ["Orc", "Giant", "Zombie"]

    def __init__(self, typeOfMon, weaponOfChoice):
        self.typeOfMonster = typeOfMon
        #Orc
        if typeOfMon is 1:
            self.typeOfMonster = self.monsters[0]
            self.attack = 15
            self.health = 50

        #Giant
        elif typeOfMon is 2:
            self.typeOfMonster = self.monsters[1]
            self.attack = 8
            self.health = 100

        #Zombie
        elif typeOfMon is 3:
            self.typeOfMonster = self.monsters[2]
            self.attack = 12
            self.health = 65
        self.weapon = Weapon(weaponChoice)


    def returnTraits(self, typeMonster):
        return self.typeOfMonster + ": \n" \
                "Attack: " + str(self.attack) + \
                "\nHealth: " + str(self.health) +\
                "\nWeapon: " + self.weapon.getWeapon()



print("Welcome to this battle simulation game!\nThe two players playing this game will each control army comprising of "
      "Orcs, Giants, and Zombies.")
print("Each class has the following stats:\n")
print("Orc: \n"
      "Attack: 15\n"
      "Health: 50\n\n"

      "Giant: \n"
      "Attack: 8 \n"
      "Health: 100\n\n"

      "Zombie:\n"
      "Attack: 12\n"
      "Health: 65.")
print("Each weapon has the following stats:\n")
print("Sword: \n"
      "Attack: 18\n"
      "Crit Chance: 20%\n"
      "Crit Multiplier: 150% of original damage\n\n"

      "Bow and Arrow: \n"
      "Attack: 9\n"
      "Crit Chance: 10%\n"
      "Crit multiplier: 200% of original damage\n\n"

      "Slingshort: \n"
      "Attack: 1\n"
      "Crit Chance: 5%\n"
      "Crit multiplier: 400% of original damage.\n\n")

print("Player 1 please create your team.")
count = 0
while count < 5:
    race = raw_input("Please input the following for your race:\n"
                     "1) Orc\n"
                     "2) Giant\n"
                     "3) Zombie\n")
    weaponChoice = raw_input("Please input the following for your weapon of choice for this character.\n"
                             "1) Sword\n"
                             "2) Bow and Arrow\n"
                             "3) Slingshot.\n")
    tempMonster = Monster(race, weaponChoice)

