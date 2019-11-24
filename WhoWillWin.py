import random


class Sprite:

    def __init__(self, blood, damage):
        self.blood = blood
        self.damage = damage

    def hit(self):
        """
        每回合的攻击力
        :return: round_damage
        """
        round_damage = self.damage + random.randint(-5, 5)
        return round_damage


class Hero(Sprite):
    def __int__(self, blood, damage):
        Sprite.__init__(self, blood, damage)

    def hit(self):
        """
        扩展父类方法，输出英雄每回合攻击力
        :return:
        """
        print('英雄在此回合攻击力', Sprite.hit(self))
        return Sprite.hit(self)


class Monster(Sprite):
    def __int__(self, blood, damage):
        Sprite.__init__(self, blood, damage)

    def hit(self):
        """
        扩展父类方法，输出怪物每回合攻击力
        :return: round_damage
        """
        print('怪物在此回合攻击力', Sprite.hit(self))
        return Sprite.hit(self)


if __name__ == '__main__':
    hero = Hero(200, 10)
    monster = Monster(100, 20)
    print('英雄的血量', hero.blood, '怪物的血量', monster.blood)
    fight_round = 1
    while hero.blood > 0 and monster.blood > 0:
        print('这是第{}回合'.format(fight_round))
        hero.blood = hero.blood - monster.hit()
        monster.blood = monster.blood - hero.hit()
        if hero.blood <= 0:
            print('英雄死了')
            break
        elif monster.blood <= 0:
            print('怪物死了')
            break
        fight_round += 1
    else:
        print('初始数值错误')
