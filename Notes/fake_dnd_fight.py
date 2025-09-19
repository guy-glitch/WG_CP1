# WG 1st Conditioinals Notes
import random
player_hp = 20
player_attack = 2
player_defense = 5
player_damage = 5

monster_name = "clang"
monster_hp = 15
monster_attack = 3
monster_damage = 10
monster_defense = 2

hit_roll = random.randint(1,20) 
print(f"You roll a {hit_roll} on your hit roll")

if hit_roll == 20:
    print("You got a crit! That means you get to roll for damage twice!")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_damage
    if damage_roll >= monster_defense:
        print(f"You did {damage_roll-monster_defense} damage")
        monster_hp -= damage_roll-monster_defense
    else:
        print("You did no damage")
elif hit_roll == 1:
    print("You failed, a true critical fail! Now the monster gets to attack you!")
    mdamage_roll = random.randint(1,12) + monster_damage
    player_hp -= mdamage_roll-player_defense
    print(f"The monster rolled {mdamage_roll}, your hp is now {player_hp}")
elif hit_roll + player_attack >= 12:
    print("You hit")
    damage_roll = random.randint(1,8) + player_damage
    print(f"You did {damage_roll} damage")
else:
    print("You missed. Failure")
print("Your turn is over")
