import random
from abc import ABC, abstractmethod



class Weapon(ABC): #abstract class for weapons

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def info(self):
        pass

class Swords(Weapon): #class for creating swords

    def __init__(self, name, attack_points, health_points, price):
        super().__init__(name)

        self.attack_points = attack_points
        self.health_points = health_points
        self.price = price

    def info(self):
        Info = self.name + " is attack weapon that increases attack points" + " for " + str(self.attack_points) + " pts and health points for " + str(self.health_points) + "!"
        return Info

    def __str__(self):

        return "Sword name: {}\nSword attack: +{}\nSword price: {}\n".format(self.name,
                                                                             self.attack_points,
                                                                             self.price)


Elf_Sword = Swords("Elf Sword", 6, 6, 100)
Fire_Sword = Swords ("Fire Sword", 8, 8, 130)
Space_Sword = Swords("Space Sword", 10, 10, 180)

#print(Elf_Sword.info())
#print(Elf_Sword)
#print(Fire_Sword)
#print(Space_Sword)


class Shield(Weapon): #class for creating shields
    
    def __init__(self, name, defence_points, health_points, price):
        super().__init__(name)

        self.defence_points = defence_points
        self.health_points = health_points
        self.price = price

    def info(self):
        Info = self.name + " is defence weapon that increases defence points" + " for " + str(self.defence_points) + " pts and health points for " + str(self.health_points) + "!"

        return Info

    def __str__(self):

        return "Shield name: {}\nShield defence: +{}\nShield price: {}\n".format(self.name.strip().title(),
                                                                             self.defence_points,
                                                                             self.price)


Elf_Shield = Shield("Elf Shield", 6, 6, 100)
Fire_Shield = Shield ("Fire Shield", 8, 8, 130)
Space_Shield = Shield("Space Shield", 10, 10, 180)

#print(Elf_Shield.info())
#print(Elf_Shield)
#print(Fire_Shield)
#print(Space_Shield)


class Armory(): #class for creating armory (with swords and shields)

    def __init__(self, name):
        self.name = name

        self.attack_Weapons = [Elf_Sword, Fire_Sword, Space_Sword]
        self.defence_Weapons = [Elf_Shield, Fire_Shield, Space_Shield]

    def my_Attack_Weapons(self): #get all weapons for attack

        print("\nAttack weapons:\n")
        
        i = 0
        for weapon in self.attack_Weapons:
            i+=1
            print(i, ")", weapon)

    def my_Defence_Weapons(self): #get all weapons for defence

        print("\nDefence weapons:\n")
        
        i = 0
        for weapon in self.defence_Weapons:
            i+=1
            print(i, ")", weapon)


myArmory = Armory ("Armory")

#myArmory.my_Attack_Weapons()    
#myArmory.my_Defence_Weapons()   


class Fighters:

    rounds = 10

    def __init__(self, name):

        self.name = name
        self.health = 100
        self.damage = [5, 10, 15, 20]
        self.defence = [1, 2, 3, 4]
        self.numOfWins = 0
        self.numOfDeaths = 0
        self.coins = 0
        self.attack_weapons = []
        self.defence_weapons = []


    def upgradeHealth(self, healthUp): #upgrade health for specific fighter
        price = healthUp * 10

        if price <= self.coins:
            self.coins = self.coins - price
            self.health = self.health + healthUp
            print(self.name,"'s health points upgraded | Health: +",healthUp)
        else:
            print("You cannot upgrade health! Not enough coins!")


    def upgradeAttack(self, attUp): #upgrade attack skill for specific fighter

        price = attUp * 10
        
        if price <= self.coins:
            self.coins = self.coins - price
            self.damage = [(i + attUp) for i in self.damage]
            print(self.name, "'s attack damage upgraded | Attack: +",attUp)
        else:
            print("You cannot upgrade attack! Not enough coins!")


    def upgradeDefence(self, defUp): #upgrade defence skill for specific fighter

        price = defUp * 10

        if price <= self.coins:
            self.coins = self.coins - price               
            self.defence = [(i + defUp) for i in self.defence]
            print(self.name, "'s defence upgraded | Defence: +", defUp)
        else:
            print("You cannot upgrade defence! Not enough coins!")

            
    def defencePoints(self):  #get defence points
        defPoints = sum(self.defence)
        return "{}'s defence points: {}\n".format(self.name, defPoints )


    def attackPoints(self): #get attack points
        attPoints = sum(self.damage)
        return "{}'s attack points: {}\n".format(self.name, attPoints )


    def healthPoints(self): #get health points
        return "{}'s health points: {}\n".format(self.name, self.health )


    def buy_Sword(self, sword_name):  #enter the name of the sword that you want to buy

        for sword in myArmory.attack_Weapons:

            if sword_name.strip().lower() == sword.name.strip().lower() and self.coins >= sword.price:
                print(self.name,"bought", sword.name, "for", sword.price, "coins!")
                self.coins -= sword.price
                self.attack_weapons.append(sword)

                self.damage = [(i + sword.attack_points) for i in self.damage]
                self.health += sword.health_points
                
            elif sword_name.strip().lower() == sword.name.strip().lower() and self.coins < sword.price:
                print("You do not have enough coins to buy",sword.name,"!")
                

    def show_attack_weapons(self):

        i = 0
        if not self.attack_weapons:
            print("\n", self.name, "has 0 attack weapons!")

        else:
            print("\n", self.name,"'s attack weapon list:\n")
            for weapon in self.attack_weapons:
                i += 1
                print(i,")", weapon.name)


    def buy_Shield(self, shield_name):  #enter the name of the sword that you want to buy

        for shield in myArmory.defence_Weapons:

            if shield_name.strip().lower() == shield.name.strip().lower() and self.coins >= shield.price:
                print(self.name,"bought", shield.name, "for", shield.price, "coins!")
                self.coins -= shield.price
                self.defence_weapons.append(shield)

                self.defence = [(i + shield.defence_points) for i in self.defence]
                self.health += shield.health_points

            elif shield_name.strip().lower() == shield.name.strip().lower() and self.coins < shield.price:
                print("You do not have enough coins to buy", shield.name,"!")
                

    def show_defence_weapons(self):

        i = 0
        if not self.defence_weapons:
            print("\n", self.name, "has 0 defence weapons!")

        else:
            print("\n", self.name,"'s defence weapon list:\n")
            for weapon in self.defence_weapons:
                i += 1
                print(i,")", weapon.name)
    

    def Attack(self, defenceFighter): #start the fight between two fighters

        i = 1

        while defenceFighter.health > 0 and i <= self.rounds:

            i += 1

            AttackDamage = random.choice(self.damage)
            DefencePoints = random.choice(defenceFighter.defence)
            
            defenceFighter.health = defenceFighter.health + DefencePoints - AttackDamage

            if defenceFighter.health > 0:
                print("{} attacks {}! | Defence for +{}hp | Hit for -{}hp | {}'s health: {}hp\n".format(self.name, defenceFighter.name,
                                                                                                        DefencePoints, AttackDamage,
                                                                                                        defenceFighter.name, defenceFighter.health))
            else:          
                defenceFighter.health = 0
                print("{} attacks {}! | Defence for +{}hp | Hit for -{}hp | {}'s health: {}hp\n".format(self.name, defenceFighter.name,
                                                                                                        DefencePoints, AttackDamage,
                                                                                                        defenceFighter.name, defenceFighter.health))
                
        else:
            
            if defenceFighter.health <= 0:
                
                defenceFighter.numOfDeaths += 1
                defenceFighter.coins -= 5
                if defenceFighter.coins < 0 :
                    defenceFighter.coins = 0
                
                self.numOfWins += 1
                self.coins += 20
                
                defenceFighter.health = 0
                print("{} killed {}! | {}'s health: {}hp\n{} wins!\n\n".format(self.name, defenceFighter.name,
                                                                       defenceFighter.name, defenceFighter.health, self.name))
            else:
                defenceFighter.numOfWins += 1
                defenceFighter.coins += 20

                self.numOfDeaths += 1
                self.coins -= 5
                if self.coins < 0 :
                    self.coins = 0

                print("{}'s attack failed! | {}'s remaining health: {}hp\n{} survived!\n\n".format(self.name, defenceFighter.name,
                                                                                         defenceFighter.health, defenceFighter.name))

        self.health = 100
        defenceFighter.health = 100


    def __str__(self):

        name = "\nFighter's name: {}\n".format(self.name)
        health = self.healthPoints()
        attackPoints = self.attackPoints()
        defencePoints = self.defencePoints()
        wins ="Wins: {}\n".format(self.numOfWins)
        defeats  = "Defeats: {}\n".format(self.numOfDeaths)
        coins = "Coins: {}\n\n".format(self.coins)

        fullInfo = name + health + attackPoints + defencePoints + wins + defeats + coins
        

        return fullInfo
                

Goku = Fighters("Goku")
Konan = Fighters("Konan")
#print(Goku,Konan)

for i in range(0,6):
    i+=1
    Goku.Attack(Konan)
    
print(Goku, Konan)


Konan.show_attack_weapons()
Konan.buy_Sword("fire sword")
Konan.buy_Sword("  space sword  ")
Konan.buy_Shield("  Elf Shield")
Konan.buy_Shield("  fire Shield ")

Konan.show_attack_weapons()
Konan.show_defence_weapons()
print(Konan)


#Goku.upgradeAttack(1)
#Konan.upgradeDefence(2)

#Goku.upgradeHealth(1)
#Konan.upgradeHealth(2)

#print(Goku.healthPoints())
#print(Konan.healthPoints())

#print(Goku)
#print(Konan)


