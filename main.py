from player import Player

tim = Player("Tim")

# print(tim.name)
# print(tim.lives)
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim.lives -= 1
# print(tim)
#
# tim._lives = 9
# print(tim)
#
# tim.level = 2
# print(tim)
#
# tim.level += 5
# print(tim)
#
# tim.level = 3
# print(tim)
#
# print()
# tim.score = 25
# print(tim)

from enemy import Enemy, Troll

# random_monster = Enemy("Monster1", 50, 5)
# print(random_monster)
# random_monster.take_damage(20)
# print(random_monster)
# random_monster.take_damage(30)
# print(random_monster)
# print("Since no Hit points left so lives will now get reduced by 1")
# random_monster.take_damage(20)
# print(random_monster)  # since no Hit points left so lives will now get reduced by 1

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll -{}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()