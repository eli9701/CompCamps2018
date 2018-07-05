import random
import sys
name = input("who dares challenge the MITs? ")
health = 60


class MIT:
    """MITs - The Enemies."""
    def __init__(self, name):
        self.name = name
        self.health = random.randint(1,15)
        self.damage = random.randint(5,15)

    def isAlive(self):
        return self.health > 0

    def attack(self):
        damage = random.randint(0,10)
        self.health -= damage
        return damage

class Mentor(MIT):
    def __init__(self, name):
        super().__init__(self, name)

mits = [
    MIT("kaitlen"),
    MIT("bennett"),
    MIT("austin"),
    MIT("rhi rhi"),
    MIT("travis")
        ]


score = 0

while len(mits) > 0:
    mit = mits.pop()
    print("A wild {} appears! they have {} health".format(mit.name, mit.health))
    while mit.isAlive():
        print("you have {} health".format(health))
        print("do you want to fight or retreat or rest")
        action = input("fight/retreat/rest >")
        if action.lower() == "fight":
            damage = mit.attack()
            score += damage
            print("you did {} damage!".format(damage))
            print("{} has {} health ".format(mit.name, mit.health))
            health -= mit.damage
            if health < 0:
                print("game over")
                sys.exit(0)
        elif action.lower() == "rest":
            rest = random.randint(5,11)
            health += rest
            print("you have rested and healed {} health".format(rest))
            health -= mit.damage
            print("{} did {} damage".format(mit.name, mit.damage))
            print("{} has {} health ".format(mit.name, mit.health))
        else:
            Caught = random.randint(1,5) == 1
            if not Caught:
                print ("you have escaped")
                print("you score was {}".format(score))
                sys.exit(0)
            else:
                print("you failed to run away!")


health = health + 50

print("you have {} health".format(health))
print("prepare to enter the dungeon of the mits")
print("oh no before you fight the final boss (brett) you must fight his minion the mighty c breeze")
print("the Mentor c breeze appears")

print("you have {} health".format(health))
print("do you want to fight or rest")
action = input("fight/rest >")
