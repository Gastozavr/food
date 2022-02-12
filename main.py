class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def eat(self):
        # map.del
        pass


class Coins(Food):
    def eat_coins(self):
        # pacman add coins
        self.eat()


class Buff(Food):
    def eat_buff(self):
        self.eat()
        #изменение характеристик
        
