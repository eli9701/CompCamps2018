import random
import sys
name = input("who dares challenge the MITs? ")
health = 40
class MIT:
    """MITs - The Enemies."""
    def __init__(self, name):
        self.name = name
        self.health = random.randint(1,15)
        self.damage = random.randint(1,20)

    def isAlive(self):
        return self.health > 0

    def attack(self):
        damage = random.randint(0,10)
        self.health -= damage
        return damage


mits = [
    MIT("kaitlen"),
    MIT("bennett"),
    MIT("austin"),
    MIT("rhy rhy"),
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
        print (action.lower() == "rest")
        if action.lower() == "fight":
            damage = mit.attack()
            score += damage

            print("you did {} damage!".format(damage))
            health -= mit.damage
        elif action.lower() == "rest":
            rest = random.randint(5,15)
            health += rest
            print("you have rested and healed {} health".format(rest))
            damage = mit.attack()
        else:
            Caught = random.randint(1,5) == 1
            if not Caught:
                print ("you have escaped")
                print("you score was {}".format(score))
                sys.exit(0)
            else:
                print("you failed to run away!")

print("WOW I DID NOT EVEN NOW IT WAS POSSIBLE, YOU DID IT")
