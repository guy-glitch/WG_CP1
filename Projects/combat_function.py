#WG 1st combat function
import time
import random
class_choice=input("Choose your species lich, demon, bunny").strip().lower()
player="alive"
monster_life="alive"
monster={"health":30, "defense":17, "attack":"D20 + 2", "damage":"D8 + 3"}
turn =  0
stats = {"health": 30, "defense":14, "attack": "D20 + 2", "damage":"D10","attack one" : 0, "attack two":0}
if class_choice=="bunny":
    stats["health"]=30
    stats["defense"]=14
    stats["attack"]="D20 + 2"
    stats["damage"]="D10"
    stats["attack one"]="multikick"
    stats["attack two"]="bite"
    for key, value in stats.items():
        print(f"{key} = {value}")
elif class_choice=="lich":
    stats["health"]=40
    stats["defense"]=10
    stats["attack"]="D20 + 2"
    stats["damage"]="D8"
    stats["attack one"]="draining touch"
    stats["attack two"]="death bolt"
    for key, value in stats.items():
        print(f"{key} = {value}")
elif class_choice=="demon":
    stats["health"]=20
    stats["defense"]=15
    stats["attack"]="D20"
    stats["damage"]="D10"
    stats["attack one"]="burning claw"
    stats["attack two"]="torment"
    for key, value in stats.items():
        print(f"{key} = {value}")
else:
    print("Incorrect input try again")
def player_turn(player,monster_life):
    attack_choice=input(f"type 1 for attack {stats['attack one']} or type 2 for attack {stats['attack two']} type 2?").strip().lower()
    if attack_choice=="1":
        print(f"You used {stats['attack one']}")
        if class_choice=="bunny":
            attack_roll = random.randint(1,20) + 2
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll=random.randint(1,10)
                print(f"You hit the diamond ant for {damage_roll} damage!")
                time.sleep(3)
                monster["health"]-=damage_roll
                damage_roll = (random.randint(1,10)) * 0.5
                print(f"You hit the diamond ant for an additional {damage_roll} damage with your multikick!")
                monster["health"]-=damage_roll
                time.sleep(3)
                if monster["health"]<=0:
                    print("You have defeated the diamond ant!")
                    monster_life="dead"
            else:
                print("You missed!")
        elif class_choice=="lich":
            attack_roll=random.randint(1,20) + 2
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll=random.randint(1,8)
                print(f"You hit the diamond ant for {damage_roll} damage!")
                time.sleep(3)
                monster["health"]-=damage_roll
                stats["health"]+=damage_roll
                print(f"You drained {damage_roll} health from the diamond ant!")
                time.sleep(3)
                if monster["health"]<=0:
                    print("You have defeated the diamond ant!")
                    monster_life = "dead"
            else:
                print("You missed!")
        elif class_choice=="demon":
            attack_roll=random.randint(1,20)
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll = random.randint(1,10)
                print(f"You hit the diamond ant for {damage_roll} damage!")
                time.sleep(3)
                monster["health"]-=damage_roll
                if monster["health"]<=0:
                    print("You have defeated the diamond ant!")
                    monster_life="dead"
            else:
                print("You missed!")
    if attack_choice=="2":
        print(f"You used {stats['attack one']}")
        if class_choice=="bunny":
            attack_roll=random.randint(1,20) + 2
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll=(random.randint(1,10))*1.2
                print(f"You hit the diamond ant for {damage_roll} damage!")
                monster["health"]-=damage_roll
                time.sleep(3)
                damage_roll=(random.randint(1,10)) * 0.3
                print(f"You hit the diamond ant for an additional {damage_roll} damage with your multikick!")
                time.sleep(3)
                monster["health"]-=damage_roll
                if monster["health"]<=0:
                    print("You have defeated the diamond ant!")
                    monster_life="dead"
            else:
                print("You missed!")
        elif class_choice=="lich":
            attack_roll=random.randint(1,20) + 2
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll=(random.randint(1,8)) * 1.1
                print(f"You hit the diamond ant for {damage_roll} damage!")
                time.sleep(3)
                monster["health"]-=damage_roll
                if monster["health"] <= 0:
                    print("You have defeated the diamond ant!")
                    monster_life="dead"
            else:
                print("You missed!")
        elif class_choice=="demon":
            attack_roll=random.randint(1,20)
            print(f"you rolled a {attack_roll}")
            time.sleep(3)
            if attack_roll>=monster["defense"]:
                damage_roll=(random.randint(1,10)) * 1.3
                print(f"You hit the diamond ant for {damage_roll} damage!")
                time.sleep(3)
                monster["health"]-=damage_roll
                if monster["health"]<=0:
                    print("You have defeated the diamond ant!")
                    monster_life="dead"
            else:
                print("You missed!")
        return monster_life, player
def monster_turn():
    print("The diamond ant is attacking!")
    attack = random.randint(1,2)
    if attack==1:
        print("The diamond and sprays acid at you!")
        attack_roll=random.randint(1,20) + 2
        print(f"The diamond ant rolled a {attack_roll}")
        time.sleep(3)
        if attack_roll>=stats["defense"]:
            damage_roll=random.randint(1,8) + 3
            print(f"The diamond ant hit you for {damage_roll} damage!")
            time.sleep(3)
            stats["health"]-=damage_roll
            print(f"Your health is now {stats['health']}")
            time.sleep(3)
            if stats["health"]<=0:
                print("You have been defeated by the diamond ant!")
                player="dead"
        else:
            print("The diamond ant missed!")
    if attack==2:
        print("The diamond ant bites you!")
        time.sleep(3)
        attack_roll=random.randint(1,20)+2
        print(f"The diamond ant rolled a {attack_roll}")
        time.sleep(3)
        if attack_roll>=stats["defense"]:
            damage_roll=random.randint(1,8)+3
            print(f"The diamond ant hit you for {damage_roll} damage!")
            time.sleep(3)
            stats["health"]-=damage_roll
            print(f"Your health is now {stats['health']}")
            if stats["health"]<=0:
                print("You have been defeated by the diamond ant!")
                player == "dead"
        else:
            print("The diamond ant missed!")
order = random.randint(1,2)
while player == "alive" and monster_life=="alive":
    print("You are being attacked by a diamond ant!")
    if order==1:
        player_turn(player,monster_life)
        monster_life = player_turn(monster_life)
        player = player_turn(player)
        time.sleep(3)
        if monster_life=="alive":
            monster_turn()
    else:
        monster_turn()
        monster_life = player_turn(monster_life)
        player = player_turn(player)
        time.sleep(3)
        if player=="alive":
            player_turn()