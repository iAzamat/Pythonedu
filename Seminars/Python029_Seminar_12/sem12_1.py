class Hero:

    def __init__(self, name, life=100, damage=10, shield=3):
        self.name = name    # Имя
        self.life = life    # Жизнь
        self.damage = damage    # Наносимый урон
        self.shield = shield    # Защита

    # Удар героя
    def hit(self, enemy):
        loc_damage = self.damage - enemy.shield
        if loc_damage > 0:
            enemy.life -= self.damage - enemy.shield


class Knight(Hero):
    def diff_shield(self, inc):
        self.shield += inc


class Wizard(Hero):
    def __init__(self, name, life=100, damage=10, shield=3, visible='Да'):
        super().__init__(name, life, damage, shield)
        self.visible = visible


class Dragon(Hero):
    pass


class Game:
    unit_dict = {1: Knight, 2: Wizard, 3: Dragon}
    def __init__(self) -> None:
        self.heroes = dict()

    def unit_add(self, unclass, name, life, damage, shield):
        unit = self.unit_dict[unclass](name, life, damage, shield)
        if not self.heroes:
            self.heroes[1] = unit
        else:
            cn = max(self.heroes.keys())
            self.heroes[cn+1]  = unit
        

    def heroes_print(self):
        for i in range(1, 4):
            print(
                f'{self.heroes[i].name}: Жизнь-{self.heroes[i].life}, Урон-{self.heroes[i].damage}, Защита-{self.heroes[i].shield}')
            if i == 2:
                print(
                    f'{self.heroes[i].name}: Видимость-{self.heroes[i].visible}')


game = Game()
game.unit_add(1, 'Рыцарь', 50, 10, 5)
game.unit_add(2, 'Маг', 40, 15, 3)
game.unit_add(3, 'Дракон', 100, 20, 8)

game.heroes_print()
print('\n')
game.heroes[1].hit(game.heroes[2])
game.heroes_print()
