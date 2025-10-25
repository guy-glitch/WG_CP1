#WG 1st combat function
import random
print("Chose your class")
player = "alive"
monster_life = "alive"
monster_health = 30
monster_defense = 17
monster_attack = "D20 + 2"
monster_damage = "D10 + 3"
turn =  0
while player == "alive" and monster_life == "alive":
    def player_turn():
        while turn == "Player":
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
                        turn = "Monster"
                elif action == "enemy sacrafice":
                    print("Roll to hit")
                    hit = random.randint(1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        print("You hit roll for damage")
                        damage = random.randint(1,6) + health/40
                        print(f"You did {damage}")
                        monster_health -= damage
                        health += damage
                        turn = "Monster"
                    else:
                        print("You missed")
                        turn = "Monster"
                elif action == "burning health":
                    burn_health == input("Do you want to burn half of your health to double damage? yes or no")
                    print("Roll to hit")
                    hit = random.randint( 1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        if burn_health == "yes":
                            print("You hit roll for damage")
                            damage = (random.randint(1,6) + health/40) * 2
                            print(f"You did {damage}")
                            monster_health -= damage
                            health = health / 2
                            turn = "Monster"
                        else:
                            print("You hit roll for damage")
                            damage = random.randint(1,6) + health/40
                            print(f"You did {damage}")
                            monster_health -= damage
                            turn = "Monster"
                    else:
                        print("YOU missed")
                        turn = "Monster"
                elif action == "sword strike":
                    print("Roll to hit")
                    hit = random.randint(1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        print("You hit roll for damage")
                        damage = random.randint(1,6) + health/40
                        print(f"You did {damage}")
                        monster_health -= damage
                        turn = "Monster"
                    else:
                        print("You missed")
                        turn = "Monster"
            elif class_choice == "blur knife":
                action = input("What would you like to do? \n multistrike\nbluring strike\n dagger strike")
                if action == "multistrike":
                    print("Roll to hit")
                    hit = random.randint(1,20) + health_sacraficed
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        print("You hit roll for damage on your first strike")
                        damage = ((random.randint(1,8) + 1)*2)/3 
                        print(f"You did {damage}")
                        monster_health -= damage
                        print("You hit roll for damage on your second strike")
                        damage = ((random.randint(1,8) + 1)*2)/3 
                        print(f"You did {damage}")
                        monster_health -= damage
                        turn = "Monster"
                    else:
                        print("You missed")
                        turn = "Monster"
                elif action == "enemy sacrafice":
                    print("Roll to hit")
                    hit = random.randint(1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        print("You hit roll for damage")
                        damage = random.randint(1,6) + health/40
                        print(f"You did {damage}")
                        monster_health -= damage
                        health += damage
                        turn = "Monster"
                    else:
                        print("You missed")
                        turn = "Monster"
                elif action == "burning health":
                    burn_health == input("Do you want to burn half of your health to double damage? yes or no")
                    print("Roll to hit")
                    hit = random.randint( 1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        if burn_health == "yes":
                            print("You hit roll for damage")
                            damage = (random.randint(1,6) + health/40) * 2
                            print(f"You did {damage}")
                            monster_health -= damage
                            health = health / 2
                            turn = "Monster"
                        else:
                            print("You hit roll for damage")
                            damage = random.randint(1,6) + health/40
                            print(f"You did {damage}")
                            monster_health -= damage
                            turn = "Monster"
                    else:
                        print("YOU missed")
                        turn = "Monster"
                elif action == "sword strike":
                    print("Roll to hit")
                    hit = random.randint(1,20) + health/20
                    print(f"{hit} was your roll to hit")
                    if hit > monster_defense:
                        print("You hit roll for damage")
                        damage = random.randint(1,6) + health/40
                        print(f"You did {damage}")
                        monster_health -= damage
                        turn = "Monster"
                    else:
                        print("You missed")
                        turn = "Monster"
            
    def combat():
        first = random.randint(1,2)
        if first == 1:
            turn = "Player"
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