from abc import ABC, abstractmethod

class Weapon(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def __init__(self):
        super().__init__('меч')
    def attack(self):
        return 'удар мечом'

class Bow(Weapon):
    def __init__(self):
        super().__init__('лук')
    def attack(self):
        return 'выстрел из лука'

class Mace(Weapon):
    def __init__(self):
        super().__init__('булава')
    def attack(self):
        return 'удар булавой'

class Fighter():
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon
        print(f'{self.name} выбирает {self.weapon.name}')

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f'{self.name} выбирает {self.weapon.name}')

    def buttle(self, monster):
        self.monster = monster
        print(f'{self.name} делает {self.weapon.attack()}')
        print(f'{self.monster.name} побежден!')

class Monster():
    def __init__(self, name):
        self.name = name

sword = Sword()
bow = Bow()
mace = Mace()

fighter = Fighter('Боец', sword)
monster = Monster('Монстр')

fighter.buttle(monster)
fighter.change_weapon(bow)
fighter.buttle(monster)

