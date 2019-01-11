import random

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
                

    def show_attack_weapons(self):  #show all attack weapons that player has

        i = 0
        if not self.attack_weapons:
            print("\n", self.name, "has 0 attack weapons!")

        else:
            print("\n", self.name,"'s attack weapon list:\n")
            for weapon in self.attack_weapons:
                i += 1
                print(i,")", weapon.name)


    def buy_Shield(self, shield_name):  #enter the name of the shield that you want to buy

        for shield in myArmory.defence_Weapons:

            if shield_name.strip().lower() == shield.name.strip().lower() and self.coins >= shield.price:
                print(self.name,"bought", shield.name, "for", shield.price, "coins!")
                self.coins -= shield.price
                self.defence_weapons.append(shield)

                self.defence = [(i + shield.defence_points) for i in self.defence]
                self.health += shield.health_points

            elif shield_name.strip().lower() == shield.name.strip().lower() and self.coins < shield.price:
                print("You do not have enough coins to buy", shield.name,"!")
                

    def show_defence_weapons(self): #show all defence weapons that player has

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


#Konan.show_attack_weapons()
##Konan.buy_Sword("fire sword")
#Konan.buy_Sword("  space sword  ")
#Konan.buy_Shield("  Elf Shield")
#Konan.buy_Shield("  fire Shield ")

#Konan.show_attack_weapons()
#Konan.show_defence_weapons()
#print(Konan)


#Goku.upgradeAttack(1)
#Konan.upgradeDefence(2)

#Goku.upgradeHealth(1)
#Konan.upgradeHealth(2)

#print(Goku.healthPoints())
#print(Konan.healthPoints())

#print(Goku)
#print(Konan)


