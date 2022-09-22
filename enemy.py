class Enemy:

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage
        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.hit_points))
        else:
            self.lives -= 1

    def __str__(self):
        return "Name: {0.name}, Hit points: {0.hit_points}, Lives:{0.lives}".format(self)


class Troll(Enemy):

    def __init__(self, name):
        # Enemy.__init__(self, name=name, hit_points=23, lives=5) #used in till python 2.9
        # super(Troll, self).__init__(name=name, hit_points=23, lives=5) # super is used in python 3 and above
        super().__init__(name=name, hit_points=23, lives=5) # alternate best way

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))

