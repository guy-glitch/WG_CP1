#WG 1st Text Based Adventure Game
#import random as r
import random as r
import time as t
#Create Remy's stat dictionary with three stats Star rating: 4, Cooking Sense: 5%, Control: 75%
remy = {"Star rating": 4, "Cooking sense": 5, "Control": 75, "trust":0}
#Last name dictionary of critic last names, correlated with the ingredient that name enjoys Tommato, Zucchhini, Mozzeralla, Baslil, Sausasge, Peperoncini, Swoup
critic_last ={"Tommato": "Tomato", "Zuchhini":"Zuchini", "Mozzeralla":"Mozzarella", "Baslil":"Basil", "Sausasge":"Sausage", "Peperocnini":"Peperoncini", "Galcir":"Garlic"}
#First name dictionary of critic first names correlated with the presentation wanted Circel, Zgiazg, Sritpe, Retow
critic_first = {"Circel":"Circle", "Zgiazg":"Zigzag", "Sritpe":"Stripe", "Retow":"Tower"}
#list of possible formats for the meal
presentation_options = ["Circle", "Zigzag", "Stripe", "Tower", "Arch"]
#create dictionary for the head critic first name = Carh, last name = LePineapp
head_critic = {"first name":"Carh", "last name":"LePineapp"}
#variable trained = no
trained = False
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
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("The kitchen at Gusteau's is a large, vibrant space designed to look like an authentic, high-end Parisian restaurant kitchen, blending functional industrial elements with rustic charm. It's constantly bustling with activity, noise, and steam. The floors are a mixture of tile and brick, and the walls are partially tiled, giving it a lived-in, professional feel.")
        t.wait(90)
        print("The central visual appeal comes from the extensive use of gleaming copper cookware—pots and pans hang from racks or are stacked high, catching the warm, golden light cast by the overhead lamps and the numerous gas burners.")
        t.wait(90)
        print("The atmosphere is further enhanced by piles of fresh, colorful vegetables and ingredients visible throughout the various preparation stations. It appears both chaotic and efficient, a true working kitchen that embodies the passion and energy of a demanding French culinary environment.")
        #Set enter to yes
        enter = "yes"
    #while entered == yes
    while entered == "yes":
        #if cooking pot is uncollected collect it and change stats

        #if seasoning is uncollected collect it and change stats

        #else nothing is done in this room
#create a function for moving around
def moving(choice):
    if choice == "choice":
    #allow them to choose what room they want to go into
        room = input("Do you want to go to the kitchen, the dining room, the office, the pantry, the private dining room, the rat's next, the street, the entery hall, or the apartment")
    #check what room they want to go into and move them there
    else:
        room = choice
    choice
#create the function for cooking
def cooking(critic_name):
    #display the cooking instructions
    print("To cook select the ingredients you want to add to your meal, then select the format")
    #display the order name based on function critic name
    print(f"{critic_name}")
    #let them choose if they want to cook for the critic
    cooking = input("Do you want to cook for the critic")
    #if they choose to cook for the critic:
    if cooking == "yes":
        ingredients = []
        meal = []
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
        print(presentation)
        presentation_choice = input("What presentationdo you want to use.")
        #using there control stat as a basis give them a certain percent chance of getting caught
        caught = r.randint(1,101)
        if caught > remy("Control"):
            return "You were caught"
        #check if the ingredients correlated with the name is in the meal
        if critic_last[critic_name] in ingredients:
            #increase star rating by 0.1 and display the original and the new
            remy["Star rating"] += 0.1
            print("The critic liked the ingredeints star rating increased by 0.1")
            print(f"Your new star rating is {remy['Star rating']}")
        #check if the presentation correlated with the first name is used
        if presentation == critic_first[critic_name]:
            #increase star rating by 0.1 and display the original and the new
             remy["Star rating"] += 0.1
             print(f"The critic liked the presentation star rating increased by {0.1*remy("Cooking sense")}")
             print(f"Your new star rating is {remy['Star rating']}")
    #else if they choose not to cook for the critic
    elif cooking == "no":
        #decrease star rating by .5
        remy["Star rating"] -= 0.5
        print("The critic is mad you didn't cook for them star rating decrease by 0.5")
        print(f"Your new star rating is {remy['Star rating']}")
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
        t.wait(90)
        print("A heavy wooden desk dominates the center, its surface polished by years of elbows, urgent planning, and culinary crises. On the wall hangs a framed portrait of Chef Gusteau, slightly askew, as if knocked crooked by the whirlwind energy of the kitchen outside. Shelves overflow with spice jars, culinary manuals, and well-worn notebooks full of experiments never intended for the public eye.")
        t.wait(90)
        print("Despite its small size, the office radiates authority. It’s a place where decisions are made quickly and often loudly—a room where chefs argue, dream, and occasionally panic. Yet there’s also a strange warmth to it, a reminder that behind every great dish and every chaotic dinner rush is a human (or sometimes rat) striving to live up to the restaurant’s towering legacy.")
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
#Create the function for the dining room with argument delegated
def dining_room(delegated):
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just beyond the controlled chaos of Gusteau’s kitchen lies the dining room—a realm of elegance where the clang of pots fades into murmured conversations and the soft clink of cutlery. Warm golden lighting spills from ornate chandeliers, casting a gentle glow over crisp white tablecloths and polished glassware that glitters like tiny stars.")
        t.wait(90)
        print("Rows of neatly arranged tables fill the space, each one set with meticulous attention to detail, as if every folded napkin and perfectly placed fork were part of a choreography. Along the walls hang rich tapestries and framed paintings depicting Parisian life, giving the room an atmosphere equal parts sophistication and comfort.")
        t.wait(90)
        print("Though serene on the surface, the dining room pulses with its own energy. Laughter rises and falls like waves, servers glide between tables with practiced grace, and the savory aroma of freshly plated dishes drifts through the air. It’s a place where guests savor not only food but moments—where celebrations unfold, romances spark, and every plate carries the promise of Gusteau’s enduring magic.")

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
                    remy("trust") += 2
                elif direction == "forward" and front != "Shadowy circle" and front != "Wavering shape" and front != "moving shadows close to the ground":
                    remy("trust") += 2
                elif direction == "left" and left != "Shadowy circle" and left != "Wavering shape" and left != "moving shadows close to the ground":
                    remy("trust") += 2
                elif direction == "backward" and behind != "Shadowy circle" and behind != "Wavering shape" and behind != "moving shadows close to the ground":
                    remy("trust") += 2
                else:
                    print("You stay where you are.")
                    continue
            #describe them getting called back into the kitchen and ask them if they want to move back to the kitchen if so move them back to the kitchen and also increase the control by trust
            remy("Control") += remy("trust")
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
        t.wait(90)
        print("A battered sofa sits lopsided in the corner, its cushions worn from nights spent collapsing after long shifts at Gusteau’s. Nearby, a tiny kitchenette fights for space against stacks of dirty dishes, half-finished attempts at cooking, and an enthusiastic but chaotic assortment of pots and pans clearly used by someone still learning their way around a stove.")
        t.wait(90)
        print("Despite its clutter, the apartment holds a quiet charm. It’s a place where ideas simmer just as much as sauces do, where a rat and a young chef once shared secrets, breakthroughs, and the occasional kitchen disaster. It may be small and perpetually messy, but within its four walls lives a sense of possibility—a reminder that greatness can come from the most unexpected corners of Paris.")
        #Set enter to yes

    #while entered == yes

#Create the function for the street
def street():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just outside the warm glow of Gusteau’s windows, the Parisian street stretches like a ribbon of motion and murmurs—a place where the aroma of fresh bread mingles with the distant hum of traffic. Streetlamps cast soft pools of amber light across the cobblestones, giving the night an almost theatrical glow as shadows dance between passing pedestrians.")
        t.wait(90)
        print("Cafés spill onto the sidewalks with small round tables, each one hosting quiet conversations, clinking cups, and the occasional burst of laughter. Bicycles rattle over uneven stones, delivery vans rumble past with sleepy determination, and the Seine’s gentle breeze carries hints of river mist and roasting chestnuts from nearby vendors.")
        t.wait(90)
        print("Though busy, the street has a charm all its own. It’s a place where stories intersect—tourists pausing in awe, locals navigating with effortless rhythm, and dreamers wandering with no destination except possibility. Under the soft glow of Parisian night, even a simple stroll feels like the beginning of something extraordinary.")

        #Set enter to yes

    #while entered == yes

        #if they came in here to be congratulated

            #give them a congratulated message for raising the star rating

        #if they came because they dropped the star rating give them an angry message and send them out to be a server

#Create the function for the pantry
def pantry():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Tucked just beyond the main bustle of Gusteau’s kitchen, the pantry is a treasure trove of aromas and carefully hoarded ingredients—a quiet haven where the noise of sizzling pans fades into the soft rustle of paper sacks and the gentle clink of glass jars. Warm, ambient light spills across rows of shelves stacked high with spices, grains, and preserved delicacies from every corner of France.")
        t.wait(90)
        print("Wooden crates filled with fresh produce sit neatly along the floor—tomatoes still carrying the scent of the morning market, onions braided together like rustic garlands, and herbs tied in bundles that perfume the entire room. Glass jars line the walls in perfect order, each one a tiny universe of colors: golden saffron, deep paprika, fragrant lavender, and countless others waiting their turn to transform a dish.")
        t.wait(90)
        print("Despite its stillness, the pantry hums with possibility. It’s a place where chefs pause to think, where recipes begin as whispers, and where Remy once found both temptation and inspiration among the neatly labeled treasures. In this quiet, ingredient-filled sanctuary, every great meal begins long before it reaches the heat of the kitchen.")
        #Set enter to yes

    #while entered == yes

        #give them a list of the ingredients

        #let them choose five ingredients

        #get the length of the list and remove any that are above the five max.

        #return the ingredients that they chose

#Create the function for the private dining room
def private_dining():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Hidden behind a discreet velvet curtain, the private dining room is a world apart from the lively hum of Gusteau’s main floor—a sanctuary of quiet elegance reserved for those whose opinions can shape the fate of an entire restaurant. Soft, amber light from ornate sconces glows against deep burgundy walls, casting long, thoughtful shadows that seem to whisper of countless judgments made within these confines.")
        t.wait(90)
        print("A single, impeccably set table dominates the center of the room, its white linen flawless and its silverware gleaming with almost intimidating precision. Plush high-backed chairs cradle their occupants in comfort, while framed sketches of culinary masterpieces line the walls like a gallery dedicated to gastronomic artistry.")
        t.wait(90)
        print("Though hushed and refined, the room holds a palpable tension—an invisible weight born from anticipation. Here, every dish is presented with reverence, every detail scrutinized, and every bite carries the power to elevate or unravel a chef’s career. In this intimate chamber of judgment, silence speaks louder than applause, and a single raised eyebrow can echo louder than the clamor of the entire kitchen.")

        #Set enter to yes

    #while entered == yes

        #describe the reaction of the critic depending on how closely the thing aligns with their tastes

        #its empty if there is not a critic order

#Create the function for the rat's nest
def rats_nest():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Deep beneath the bustling world of Paris, the rats’ nest is a hidden labyrinth of woven scraps, scavenged trinkets, and cozy nooks—a lively underground community where the glow of lanterns bounces off stone walls and the scent of foraged food lingers in the air. Despite its humble materials, the space feels warm and alive, shaped by countless tiny paws working in harmony.")
        t.wait(90)
        print("Tunnels twist and wind into chambers lined with soft fabric shreds, mismatched buttons, and carefully arranged treasures collected from the human world above. Bits of string, bottle caps, and colorful paper are repurposed with surprising creativity, turning everyday refuse into furniture, tools, and decorations that sparkle in the dim light.")
        t.wait(90)
        print("Though hidden far from human eyes, the nest hums with vibrant energy—rats chattering in quick bursts, families sharing meals, and dreams simmering in the minds of those bold enough to imagine more. It’s a place of community, resourcefulness, and ambition, a reminder that even in the shadows, hope can thrive and greatness can begin in the unlikeliest of homes.")
        #Set enter to yes

    #while entered == yes

        #if you were kicked out of the restaurant you die from poisoned food

        #if else you are inviting them to return with you to the restaurant they come with you

        #else they talk with you and give you gross food

#Create the function for the entry hall
def entry_hall():
    #variable entered = no
    entered = "no"
    #if variable entered == no
    if entered == "no":
        #describe the room
        print("Just before the whirlwind energy of Gusteau’s kitchen lies the entry hall—a narrow but purposeful corridor where the aromas of simmering sauces drift out to greet anyone passing through. Soft, muted lighting reflects off tiled floors worn smooth by decades of hurried footsteps, giving the space an understated warmth despite its constant traffic.")
        t.wait(90)
        print("Along the walls hang hooks cluttered with aprons, spare towels, and the occasional forgotten jacket left by a cook rushing into service. A bulletin board, peppered with handwritten notes, shift schedules, and half-faded reminders, adds a touch of organized chaos to the otherwise orderly passage.")
        t.wait(90)
        print("Though simple, the entry hall buzzes with anticipation. It’s the final quiet step before entering the storm: a place where chefs take a breath, adjust their sleeves, and prepare themselves for the heat, noise, and artistry beyond the swinging kitchen doors. In this small stretch of hallway, every service begins—not with a clang of pots, but with a moment of quiet resolve.")

        #Set enter to yes

    #while entered == yes

        #if it is first time you entered the entry hall introduce the other cooks

        #else nothing is done in this room

#create the function that generates the critics name
def critics_name():
    #critic name = []
    critic_name1 = []
    critic_values = []
    #get a random value from critics first name dictionary
    critic_values.append(r.choice(critic_first))
    #get a random value from the critic last name dictionary
    critic_values.append(r.choice(critic_first))
    #get the key that corresponds with the value of the first name and add to the list critic name
    for key, value in critic_first.items():
        if value == critic_values(0):
            critic_name1.append(key)
    #get the key that corresponds with the value of the first name and add to the list critic name
    for key, value in critic_first.items():
        if value == critic_values(1):
            critic_name1.append(key)
    #return critic name in a well formatted list
    return critic_name1
#give starting intro

#while loop that is infinite
while True:
    #ask them if they want to go to work with Alfredo Linguini
    work = input("\033[33mDo you want to work with Alfredo Linguini, and become a chef")
    #if they don't want to go to work
    if work == "no":
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

        #send them to work with him
