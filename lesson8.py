class Character():
    def __init__(self, hp, name):
        self.hp = hp
        self.name = name

class Warrior(Character):
    def __init__(self, hp, name, strength):
        super().__init__(hp, name)
        self.strength = strength

    def attack(self):
        print(f"{self.name} атакує!")
        aim = input("Введіть імя цілі: ")
        if aim.lower() == m.name.lower():
            print(f'{self.name} атакує {m.name} із силою {self.strength}')
            m.hp -= self.strength
            print(f"У {m.name} залишилося {m.hp} НР")
        elif aim.lower() == m1.name.lower():
            print(f'{self.name} атакує {m1.name} із силою {self.strength}')
            m1.hp -= self.strength
            print(f"У {m1.name} залишилося {m1.hp} НР")
        elif aim.lower() == w.name.lower():
            print("Ви не можете нанести удар собі")
        else:
            print("Такого гравця немає")
            return

w=Warrior(100,"Konan", 30)
w1=Warrior(120,"Artur", 35)
w2=Warrior(150,"Shao Khan", 50)

class Mage(Character):
    def __init__(self, hp, name, mana):
        super().__init__(hp, name)
        self.mana = mana

    def attack(self):
        aim=input("Введіть імя цілі: ")
        if aim.lower()==w.name.lower():
            print(f'{self.name} атакує {w.name} із силою магії {self.mana}')
            w.hp -= m.mana
            print(f"У {w.name} залишилося {w.hp} НР")
        elif aim.lower()==w1.name.lower():
            print(f'{self.name} атакує {w1.name} із силою магії {self.mana}')
            w1.hp -= m.mana
            print(f"У {w1.name} залишилося {w1.hp} НР")
        elif aim.lower()==w2.name.lower():
            print(f'{self.name} атакує {w2.name} із силою магії {self.mana}')
            w2.hp -= m.mana
            print(f"У {w2.name} залишилося {w2.hp} НР")
        else:
            print("Такого гравця немає")
            return

m=Mage(100,"Demon", 40)
m1=Mage(120,"Loren", 45)

w.attack()
w1.attack()



