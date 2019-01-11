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
