army1 = []
army2 = []

class Weapon:
    weapons = ["Sword", "Bow and Arrow", "Slingshot"]

    weapon = 0
    damage = 0
    critChance = 0
    critMulti = 0

    def __init__(self, weaponChoice):
        #sword
        self.weapon = weaponChoice
        if weaponChoice is 1:
            self.damage = 18
        #Bow
        elif weaponChoice is 2:
            self.damage = 9
        #Slingshot
        elif weaponChoice is 3:
            self.damage = 1



class Monster:
    health = 0
    typeOfMonster = ""
    attack = 0


    monsters = ["Orc", "Giant", "Zombie"]

    def __init__(self, typeOfMon):
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

print("Welcome to this battle simulation game!\nThe two players playing this game will each control army comprising of "
      "Orcs, Giants, and Zombies.")
print("Each class has the following stats:\n"
      "Orcs: ")
