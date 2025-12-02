#WG 1st Text Based Adventure Game
#import random as r

#Create Remy's stat dictionary with three stats Star rating: 4, Cooking Sense: 5%, Control: 75%

#Last name dictionary of critic last names, correlated with the ingredient that name enjoys Tommato, Zucchhini, Mozzeralla, Baslil, Sausasge, Peperoncini, Swoup

#First name dictionary of critic first names correlated with the presentation wanted Circel, Zgiazg, Sritpe, Retow

#create dictionary for the head critic first name = Carh, last name = LePineapp

#variable trained = no

#variable cooking_practice = no

 #create variable cooking pot = uncollected

#create variable practice meal = unmade

#create a list of the ingredients that they can choose from at base level.

#create a list of the ingredients that are in the pantry


#create a function for moving around

    #allow them to choose what room they want to go into

    #check what room they want to go into and

#create the function for cooking
   
    #display the cooking instructions

    #display the order name based on function critic name

    #let them choose if they want to cook for the critic

    #if they choose to cook for the critic:

        #ask them if they want to go to the pantry or just cook with what they have on hand

        #if they want to go to the pantry
           
            #display the ingredients in the pantry      

            #let them choose what ingredients they want to take and use, with a maximum of five

        #else

            #display the basic ingredients list

            #let them choose what ingredients they want to use, with a maximum of six

        #let them choose the presentation they want to use form a set list

        #using there control stat as a basis give them a certain percent chance of getting caught

        #check if the ingredients correlated with the name is in the meal

            #increase star rating by 0.1 and display the original and the new

        #check if the presentation correlated with the first name is used

            #increase star rating by 0.1 and display the original and the new

    #else if they choose not to cook for the critic

        #decrease star rating by .5

    #else:

        #rerun the function


#Create the function for the dining room with argument delegated


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #if delegated is no
           
            #let them inspect the room nothing else happens, they do have the choice to ask what their customers are liking their food
           
        #else
            #use a loop to let them move 10 times
           
                #give them training information, then run through the training
               
                # Describe the shadows they see round them
               
                # ask them what direction they want to move in based off of the shadows
               
                #have a list of directions that they can't move in if they choose one of those directions decrease their trust


                #if they move successfully increase the trust


            #describe them getting called back into the kitchen and ask them if they want to move back to the kitchen if so move them back to the kitchen


#Create the function for the office


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #if they came in here to be congratulated


            #give them a congratulated message for raising the star rating


        #if they came because they dropped the star rating give them an angry message and send them out to be a server


#Create the function for the pantry


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #give them a list of the ingredients


        #let them choose five ingredients


        #get the length of the list and remove any that are above the five max.


        #return the ingredients that they chose
#Create the function for the street


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #if they dropped the star rating below the limit describe them separating and send them back to the rat's nest or let them stay on the street, they die if they stay on the street


        #else


            #let them move along the street or return to the entry hall.


#Create the function for the private dining room


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #describe the reaction of the critic depending on how closely the thing aligns with their tastes


        #its empty if there is not a critic order


#Create the function for the rat's nest


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #if you were kicked out of the restaurant you die from poisoned food


        #if else you are inviting them to return with you to the restaurant they come with you


        #else they talk with you and give you gross food


#Create the function for the entry hall


    #variable entered = no


    #if variable entered == no


        #describe the room


        #Set enter to yes


    #while entered == yes


        #if it is first time you entered the entry hall introduce the other cooks


        #else nothing is done in this room


#create the function that generates the critics name


    #critic name = []


    #get a random value from critics first name dictionary


    #get a random value from the critic last name dictionary


    #get the key that corresponds with the value of the first name and add to the list critic name


    #get the key that corresponds with the value of the first name and add to the list critic name


    #return critic name in a well formatted list


#give starting intro


#while loop that is infinite


    #ask them if they want to go to work with Alfredo Linguini


    #if they don't want to go to work


        #allow them to choose whether or not they want to return to the rat's nest or wander the streets allowing


        #if they return to rat's nest


            #call rat's nest function


        #else if they want to be alone


            #describe them running into a mouse trap and dying


            #break
        #else


            #continue


    #if else they do want to go to work with him


        #send them to work with him


#describe them dying



