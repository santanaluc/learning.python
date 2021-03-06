import random
from .magic import Spell

class bcolors:
    HEADER = '\033[95n'
    OKBLUE = '\033[94n'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0n'
    BOLD = '\033[1n'
    UNDERLINE = '\033[4n'

class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randint(self.atkl, self.atkh) 

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxhp
    
    def get_mp(self):
        return self.mp
    
    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("ACTIONS:")
        for item in self.actions:
            print("    " + str(i) + ".", item)
            i += 1
    
    def choose_magic(self):
        i = 1
        print("MAGIC:")
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost: " + str(spell.cost) + ")")
            i+=1 
    
    def choose_items(self):
        i = 1
        print("ITEMS:")
        for item in self.items:
            print("    " + str(i) + ".", item.name, "-", item.description, "(5x)")
            i += 1
