#WG 1st combat function
import random
print("Chose your class")
player = "alive"
monster_life = "alive"
monster_health = 30
monster_defense = 15
monster_attack = "D20 + 2"
monster_damage = "D10 + 3"
while player == "alive" and monster_life == "alive":
    def player_turn():
        if class_choice == "sacraficial warrior":
            action = input("What would you like to do? \n sacrificial strike\n enemy sacrafice\nburning health\n sword strike")
            if action == "sacrificial strike":
                health_sacraficed = int(input(f"how much health do you want to sacrace?\n You have {health} health"))
                print("Roll to hit")
                hit = random.randint(1,20) + health_sacraficed
                print(f"{hit} was your roll to hit")
                if hit > monster_defense:
                    print("You hit roll for damage")
                    damage = random.randint(1,6) + health_sacraficed
                    print(f"You did {damage}")
                    monster_health -= damage
                    turn = "Monster"
                else:
                    print("You missed")
    def combat():
        first = random.randint(1,2)
        if first == 1:
            print("You move first")
            player_turn()
        else:
            print("The Diamond Ant attacks")
    class_choice = input("Do you want to be a sacraficial warrior, a blur knife, or a demon blood").strip()
    health = 0
    defense = 0
    attack = 0
    damage = 0
    if class_choice == "sacraficial warrior":
        print("Here are your stats.")
        health = 40
        defense = 10
        attack = f"D20 + {health/20}"
        damage = f"D6 + {health/40}"
    elif class_choice == "blur knife":
        print("Here are your stats.")
        health = 20
        defense = 15
        attack = f"D20 + 1"
        damage = f"D8 + 1"
    elif class_choice == "demon blood":
        print("Here are your stats.")
        health = 10
        defense = 17
        attack = f"D20"
        damage = f"D10 + 2"
    else:
        print("Incorrect input try again")