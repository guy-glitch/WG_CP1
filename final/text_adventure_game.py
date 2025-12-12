#WG 1st Text Based Adventure Game
#import random as r
import random as r
import time as t
#Create Remy's stat dictionary with three stats : 4, Cooking Sense: 5%, Control: 75%
remy = {"Star rating": 4, "Cooking sense": 0.5, "Control": 75, "trust":0}
#Last name dictionary of critic last names, correlated with the ingredient that name enjoys Tommato, Zucchhini, Mozzeralla, Baslil, Sausasge, Peperoncini, Swoup
critic_last ={"Tommato": "Tomato", "Zuchhini":"Zuchini", "Mozzeralla":"Mozzarella", "Baslil":"Basil", "Sausasge":"Sausage", "Peperocnini":"Peperoncini", "Galcir":"Garlic"}
#First name dictionary of critic first names correlated with the presentation wanted Circel, Zgiazg, Sritpe, Retow
critic_first = {"Circel":"Circle", "Zgiazg":"Zigzag", "Sritpe":"Stripe", "Retow":"Tower"}
critic_first_name = ["Circle", "Zgiazg", "Sritpe", "Retow"]
critic_last_name = ["Tommato", "Zuchhini", "Mozzeralla", "Baslil", "Sausasge", "Peperocnini", "Galcir"]
#list of possible formats for the meal
presentation_options = ["Circle", "Zigzag", "Stripe", "Tower", "Arch"]
#create dictionary for the head critic first name = Carh, last name = LePineapp
head_critic = {"first name":"Carh", "last name":"LePineapp"}
#variable trained = no
trained = False
entryhall_entry =  "first"
#variable cooking_practice = no
cooking_practice = False
 #create variable cooking pot = uncollected
cooking_pot = "uncollected"
seasoning = "uncollected"
#create variable practice meal = unmade
practice_meal = "unmade"
#create a list of the ingredients that they can choose from at base level.
base_ingredients = ["Tomato", "Zuchini", "Mozzarella", "Sausage", "Peperoncini", "Basil", "Garlic"]
#create a list of the ingredients that are in the pantry
pantry_ingredients = ["Pineapple","Cheese","Mozzarella","Sausage","Peperoncini","Basil","Tomato","Zuchini","Garlic","Butter", "Olive oil", "Cream","Nutmeg","Cardomom"]
#create location variable
location = "aparment"
#list of possible presenattion
presentation = []
#ingredients used in the meal
ingredients = []
def kitchen():
    global cooking_pot, seasoning, practice_meal
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("The kitchen at Gusteau's is a large, vibrant space designed to look like an authentic, high-end Parisian restaurant kitchen, blending functional industrial elements with rustic charm. It's constantly bustling with activity, noise, and steam. The floors are a mixture of tile and brick, and the walls are partially tiled, giving it a lived-in, professional feel.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        #if cooking pot is uncollected collect it and change stats
        if cooking_pot == "uncollected":
            use = input("Would you like to use the cooking pot y/n ")
            if use == "y":
                remy["Cooking sense"] += 1
                cooking_pot = 0
            else:
                print("Okay")
        #if seasoning is uncollected collect it and change stats
        if seasoning == "uncollected":
            pick_up = input("Would you like to use the seasoning y/n ")
            if pick_up == "y":
                remy["Cooking sense"] += 0.5
                seasoning = 0
            else:
                print("Okay")
        #give them an order
        if practice_meal == "unmade":
            practice_meal = 0
            print("Archei Guodda the head chef wants you to make him a meal to prove your worth")
            ingredients_practice = input("Do you want to but broccli, brussel sprouts, or gouda in the meal. ").lower().strip()
            display_practice = input("Do you want to make an arch a circle or a tower. ").lower().strip()
            if ingredients_practice == "gouda":
                print("He likes the flavor, especially the gouda")
            if display_practice == "arch":
                print("Your use of the arch amazes him")
        name = critics_name()
        cooking()
#create a function for moving around
def moving(choice):
    if choice == "choice":
    #allow them to choose what room they want to go into
        room = input("Do you want to go to the kitchen, the dining room, the office, the pantry, the private dining room, the rats next, the street, the entry hall, or the apartment")
        if room == "kitchen":
            kitchen()
        elif room == "street":
            street()
        elif room == "dining room":
            dining_room()
        elif room == "office":
            office("none")
        elif room == "pantry":
            pantry()
        elif room == "private dining room":
            private_dining()
        elif room == "rats nest":
            rats_nest()
        elif room == "entry hall":
            entry_hall()
        elif room == "apartment":
            apartment()
        else:
            moving("choice")
    #check what room they want to go into and move them there
    else:
        room = choice
#create the function for cooking
def cooking():
    #display the cooking instructions
    print("To cook select the ingredients you want to add to your meal, then select the format")
    #display the order name based on function critic name
    critic_name = critics_name()
    print(f"The critics name is {critic_name[0], critic_name[1]}")
    #let them choose if they want to cook for the critic
    cooking = input("Do you want to cook for the critic")
    #if they choose to cook for the critic:
    if cooking == "yes":
        ingredients = []
        #ask them if they want to go to the pantry or just cook with what they have on hand
        ingredient_location = input("Do you want to go to the pantry or use the ingredeints you have")
        #if they want to go to the pantry
        if ingredient_location == "pantry":
            #display the ingredients in the pantry      
            print(pantry_ingredients)
            #let them choose what ingredients they want to take and use, with a maximum of five
            for i in range(5):
                ingredient = input("What ingredeints do you want to use?").strip()
                ingredients.append(ingredient)
        #else
        else:
            #display the basic ingredients list
            print(base_ingredients)
            #let them choose what ingredients they want to use, with a maximum of six
            for i in range(6):
                ingredient = input("What ingredeint do you want to use?").strip()
                ingredients.append(ingredient)
        #let them choose the presentation they want to use form a set list
        print(presentation_options)
        presentation_choice = input("What presentationdo you want to use.")
        #using there control stat as a basis give them a certain percent chance of getting caught
        caught = r.randint(1,101)
        if caught > remy["Control"]:
            moving("rats nest")
            return "You were caught"
        #check if the ingredients correlated with the name is in the meal
        if critic_last[critic_name[1]] in ingredients:
            #increase star rating by 0.1 and display the original and the new
            remy["Star rating"] += 0.1
            print("The critic liked the ingredeints star rating increased by 0.1")
            print(f"Your new star rating is {remy['Star rating']}")
        #check if the presentation correlated with the first name is used
        if presentation_choice == critic_first[critic_name[0]]:
            #increase star rating by 0.1 and display the original and the new
             remy["Star rating"] += 0.1
             print(f"The critic liked the presentation star rating increased by {0.1*remy["Cooking sense"]}")
             print(f"Your new star rating is {remy['Star rating']}")
    #else if they choose not to cook for the critic
    elif cooking == "no":
        #decrease star rating by .5
        remy["Star rating"] -= 0.5
        print("The critic is mad you didn't cook for them star rating decrease by 0.5")
        print(f"Your new star rating is {remy['Star rating']}")
        if remy["Star rating"] < 3:
            print("You have been fired from Gusteau's")
            moving("rats nest")
    #ask them if they want to keep cooking
        keep_cooking = input("Do you want to keep cooking y/n ")
        if keep_cooking == "n":
            moving("choice")
    #else:
    else:
        #  rerun the function
        cooking(critic_name)
#Create the function for the office
def office(reason):
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Tucked just off the bustling heart of Gusteau’s kitchen, the head cook’s office is a compact but authoritative space—part command center, part sanctuary from the constant clang of pots and the shouts of line cooks. The room is dimly lit by a single brass lamp that casts a warm glow across stacks of menus, delivery invoices, and half-scribbled recipe notes")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "":
        #if they came in here to be congratulated
        if reason == "congratulated":
            #give them a congratulated message for raising the star rating
            print("Congratulations you raised the star rating by 0.5")
            moving("choice")
        #if they came because they dropped the star rating give them an angry message and send them out to be a server
        if reason == "delegated":
            dining_room("yes")
        if reason == "none":
            print("Why are you in here get out!")
            moving("choice")
#Create the function for the dining room with argument delegated
def dining_room(delegated):
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just beyond the controlled chaos of Gusteau’s kitchen lies the dining room—a realm of elegance where the clang of pots fades into murmured conversations and the soft clink of cutlery. Warm golden lighting spills from ornate chandeliers, casting a gentle glow over crisp white tablecloths and polished glassware that glitters like tiny stars.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        #if delegated is no
        if delegated == "no ":
            #let them inspect the room nothing else happens, they do have the choice to ask what their customers are liking their food
            wonder_opinion = input("Do you want to ask your customers if they like the food. ")
            if wonder_opinion == "yes":
                if remy["Star rating"] < 4:
                    remy["Star rating"] += 0.1
                    print(f"The customers think it was better than the star rating, star rating increased by 0.1 new star rating is {remy['Star rating']}")
                    moving("choice")
        #else
        else:
            ##give a list of random things that could be in there path.
            directions = ["Shadowy circle","Wavering shape","small space","moving shadows close to the ground", "empty space", "towering arch"]
            #give them training information, then run through the training
            
            #use a loop to let them move 10 times
            for i in range(10):
                ##set each of the variables to one of the option from the directions
                front = r.choice(directions)
                left = r.choice(directions)
                right = r.choice(directions)
                behind =  r.choice(directions)
                # Describe the shadows they see round them
                print(f"To your left you see a {left}, in front of you you see a {front}, to your right you see a {right}, behind you is a {behind}")
                # ask them what direction they want to move in based off of the shadows
                direction = input("Do you want to move left forward, right or backwards or do you want to stay where you are.")
                #if they move successfully increase the trust
                if direction == "stay":
                    continue
                elif direction == "right" and right != "Shadowy circle" and right != "Wavering shape" and right != "moving shadows close to the ground":
                    remy["trust"] += 2
                elif direction == "forward" and front != "Shadowy circle" and front != "Wavering shape" and front != "moving shadows close to the ground":
                    remy["trust"] += 2
                elif direction == "left" and left != "Shadowy circle" and left != "Wavering shape" and left != "moving shadows close to the ground":
                    remy["trust"] += 2
                elif direction == "backward" and behind != "Shadowy circle" and behind != "Wavering shape" and behind != "moving shadows close to the ground":
                    remy["trust"] += 2
                else:
                    print("You stay where you are.")
                    continue
            #describe them getting called back into the kitchen and ask them if they want to move back to the kitchen if so move them back to the kitchen and also increase the control by trust
            remy["Control"] += remy["trust"]
            print("Alffredo they need you bakc in the kitchens")
            go = input("Do you want to return to the kitchen")
            if go == "yes":
                moving(kitchen())
#Create the function for the office
def apartment():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Perched above the glowing streets of Paris, the apartment is a charming but undeniably cramped hideaway—a patchwork of mismatched furniture, thrift-store treasures, and the lingering scent of burnt toast. The dim light from a single window spills across the room, illuminating dust motes that float lazily in the air like they have nowhere else to be.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        stay = input("Do you want to stay or leave")
        if stay == "yes":
            print("There is nothing to do here this is just where you sleep")
            continue
        else:
            moving("choice")
#Create the function for the street
def street():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just outside the warm glow of Gusteau’s windows, the Parisian street stretches like a ribbon of motion and murmurs—a place where the aroma of fresh bread mingles with the distant hum of traffic. Streetlamps cast soft pools of amber light across the cobblestones, giving the night an almost theatrical glow as shadows dance between passing pedestrians.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        trash = input("Do you want to eat some trash y/n ")
        if trash == "y":
            return "your dead"
        elif trash == "n":
            leave = input("Do you want to leave. y/n ").strip().lower()
            if leave == "n":
                print("Okay sorry but you need to get back to work. ")
                t.sleep(5)
                kitchen()
            else:
                moving("choice")
#Create the function for the pantry
def pantry():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Tucked just beyond the main bustle of Gusteau’s kitchen, the pantry is a treasure trove of aromas and carefully hoarded ingredients—a quiet haven where the noise of sizzling pans fades into the soft rustle of paper sacks and the gentle clink of glass jars. Warm, ambient light spills across rows of shelves stacked high with spices, grains, and preserved delicacies from every corner of France.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        #give them a list of the ingredients
        print(f"These are the ingredeints in the pantry {pantry_ingredients}")
        leave = input("Do you want to leave y/n ").strip()
        if leave == "y":
            moving("choice")
        else:
            pantry()
#Create the function for the private dining room
def private_dining():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Hidden behind a discreet velvet curtain, the private dining room is a world apart from the lively hum of Gusteau’s main floor—a sanctuary of quiet elegance reserved for those whose opinions can shape the fate of an entire restaurant. Soft, amber light from ornate sconces glows against deep burgundy walls, casting long, thoughtful shadows that seem to whisper of countless judgments made within these confines.")
        t.sleep(1)
        #Set enter to yes
        entered = "yes"
    #while entered == yes
    while entered == "yes":
        #describe the reaction of the critic depending on how closely the thing aligns with their tastes
        print("The room is empty. ")
        moving("choice")
#Create the function for the rat's nest
def rats_nest():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Deep beneath the bustling world of Paris, the rats’ nest is a hidden labyrinth of woven scraps, scavenged trinkets, and cozy nooks—a lively underground community where the glow of lanterns bounces off stone walls and the scent of foraged food lingers in the air. Despite its humble materials, the space feels warm and alive, shaped by countless tiny paws working in harmony.")
        t.sleep(1)
        #Set enter to yes
        entered = "y"
    #while entered == yes
    while entered == "y":
        #if you were kicked out of the restaurant you die from poisoned food
        if remy["Star rating"] < 3:
            print("You die from food poisoning")
            quit
        #if else you are inviting them to return with you to the restaurant they come with you
        elif remy["Star rating"] > 4.5:
            print("You invite them to come with you and they turn you down. ")
            moving("choice")
        #else they talk with you and give you gross food
        else:
            print("They tell you about there normal life and give you gross food. ")
            moving("choice")
#Create the function for the entry hall
def entry_hall():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just before the whirlwind energy of Gusteau’s kitchen lies the entry hall—a narrow but purposeful corridor where the aromas of simmering sauces drift out to greet anyone passing through. Soft, muted lighting reflects off tiled floors worn smooth by decades of hurried footsteps, giving the space an understated warmth despite its constant traffic.")
        t.sleep(1)
        #Set enter to yes
        entered = "y"
    if entryhall_entry == "first":
            entryhall_entry_entry = "first"
    #while entered == yes
    while entered == "y":
        #if it is first time you entered the entry hall introduce the other cooks
        if entryhall_entry_entry == "first":
            print("The head cooks name is Archie Guodda \n The sou chefs name is Jerry Lee \n The assistant chefs name is Estabon the Magnificent")
            entryhall_entry_entry = 0
            moving("choice")
        #else nothing is done in this room
        else:
            moving("choice")
#create the function that generates the critics name
def critics_name():
    #critic name = []
    critic_name1 = []
    #get a random value from critics first name dictionary
    critic_name1.append(r.choice(critic_first_name))
    #get a random value from the critic last name dictionary
    critic_name1.append(r.choice(critic_last_name))
    #get the key that corresponds with the value of the first name and add to the list critic name
    #return critic name in a well formatted list
    return critic_name1
#give starting intro
print("\033[33mThe moon hung low over Paris, spilling silver light across the narrow apartment windows. Inside one of them, a single lamp glowed—dim, warm, and flickering like it wasn’t sure it wanted to stay turned on. \n Alfredo Linguini pushed open the door with a sigh heavy enough to knock it down. His new apartment wasn’t much: peeling wallpaper, a squeaky bed, and a refrigerator that made a mysterious buzzing noise every time he walked past it. Still… it was better than the alley. \n Home, he mumbled uncertainly, dropping his bag on the floor with a thud.")
t.sleep(1)
print("Up in the ceiling vent, Remy perked his ears.\nThe human was back.\nThe clumsy one.\nRemy had slipped into this apartment earlier simply because it smelled like food—not good food, but food. A half-eaten baguette on the counter, a forgotten wedge of cheese, a few vegetables that had definitely seen better days. It was enough.\nBut now the human was here again, dragging his feet and muttering to himself as he rummaged through the refrigerator.\nRemy crept closer, silent on the metal vent. The human pulled out a container, sniffed it, made a face, and put it back.\n“Ugh… maybe cereal,” he said, collapsing at the tiny kitchen table.")
t.sleep(1)
print("Then it happened.\nThe vent grill came loose.\nJust a little.\nJust enough.\nRemy slipped—tumbled—and landed on the table with an undignified thump right in front of Linguini’s cereal bowl.\nFor a moment, neither moved.\nRemy froze, whiskers twitching.\nLinguini blinked. Once. Twice. Three times.\n“Oh no,” he whispered. I’ve been here five minutes and it’s already infested!\nRemy squeaked in offense. Infested? He was a culinary artist, thank you very much.\nLinguini jumped to his feet, then tripped over the chair he’d just stood up from, crashing to the floor. The bowl tipped, milk sloshed, and Remy dodged out of instinct, landing lightly on the edge of the table.") 
t.sleep(1)
print("They stared at each other again—this time at eye level.\nAnd in the quiet chaos of the tiny apartment, something strange hung in the air:\nNot fear.\nNot anger.\nRecognition.")
#while loop that is infinite
while True:
    #ask them if they want to go to work with Alfredo Linguini
    work = input("\033[33mDo you want to work with Alfredo Linguini, and become a chef y/n")
    #if they don't want to go to work
    if work == "n":
        #allow them to choose whether or not they want to return to the rat's nest or wander the streets allowing
        live = input("Do you want to return to the rats nest or wander the streets alone")
        #if they return to rat's nest
        if live == "rats nest":
            print("You die on poisoned food")
            again = input("Do you want to play again")
            if again == "yes":
                continue
            else:
                break
        #else if they want to be alone
        elif live == "alone":
            #describe them running into a mouse trap and dying
            print("you run into a moust trap and die")
            again = input("Do you want to play again")
            if again == "yes":
                continue
            else:
                break
        #else
        else:
            #continue
            continue
    #if else they do want to go to work with him
    elif work == "y":
        #send them to work with him
        entry_hall()