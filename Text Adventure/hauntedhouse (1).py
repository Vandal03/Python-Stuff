import textFunctions


def start():
#The adventure begins while arriving in a vehicle at your uncles house!
    textFunctions.slowText("You are heading to your uncles house and were dropped off by a Taxi Driver", .05, 1)
    textFunctions.slowText("You are dropped off at the house by the taxi driver and he expects his payment", .05, 1)
    textFunctions.slowText("How do you pay?", .05, 1)
    textFunctions.slowText(" 1 Card or 2 Cash", .05, 1)

    answer = input (">")
#Potential inputs for decisions with Taxi Driver

## The = sign is for assignment. Use == for comparisons 
## Use a : after the inital part of the if and elif statements, like you did with else lines.
## Lines below each if, elif, or else need to be indented in

##Python is weird, have to compare both options to the variable when using conditional statements - not the case with languages like c#

    if answer == 'Card' or answer == '1':
        textFunctions.slowText("Your information was stolen and the taxi driver shot you so that you would not remember him!", .05, 1)
        game_over()
        textFunctions.slowText("Cash is always a better idea...", .05, 1)
        play_again()
    elif answer == 'Cash' or answer == '2':
        enter_house()
    else:
        textFunctions.slowText("Have you not the intelligence to write the appropriate response?", .05, 1)
        play_again()

#Upon entering the house
## When creating a function, be sure to put a : after the function name and arguments
def enter_house(): 
    textFunctions.slowText("You've approached the house and have opened the door.", .05, 1)
    textFunctions.slowText("It's dark, and only a dim light in the back right corner illuminates the surrounding area", .05, 1)
    textFunctions.slowText("There are multiple doors throughout the house.", .05, 1)
    textFunctions.slowText("You attempt to turn a light on, but the light does not work", .05, 1)
    textFunctions.slowText("Do you:", .05, 1)
    textFunctions.slowText("1. Continue your way through the house.", .05, 1)
    textFunctions.slowText("2. Turn back to the door and return to the street.", .05, 1) 

#Potential inputs for decisions with front door arrival
    answer = input (">")
## Same comments as above with If statements
    if answer == "1" or answer == "2":
        textFunctions.slowText("You hear a noise that sounds of screeching and the front door closes behind you!", .05, 1)
        textFunctions.slowText("You pull on the front door and the door is locked and will not budge!", .05, 1)
        door_locked()

#From the point where the door is locked and can't be opened
def door_locked():
    textFunctions.slowText("Your heart begins to pound and you start to sweat.", .05, 1)
    textFunctions.slowText("You analyze the room and notice 6 dimly noticeable doors from the common room and stairs leading to a second floor.", .05, 1)
    textFunctions.slowText("The doors each contain a number etched 1-6", .05, 1)
    textFunctions.slowText("You feel you need to hide, which door do you want to open?", .05, 1)
    common_room()

#Entering the common room

def common_room():
    textFunctions.slowText("While in the common room, you must select a door to hide.", .05, 1)
    textFunctions.slowText("Select a room, 1-6 or (s)stairs.", .05, 1)
    
    answer = input (">")

    if answer == "1":
        bath_room()
    elif answer == "2":
        childs_room()
    elif answer == "3":
        master_room()
    elif answer == "4":
        kitchen_room()
    elif answer == "5":
        family_room()
    elif answer == "6":
        basement_room()
    elif answer == "s":
        stairs()
            

#The bathroom experience 
## Make sure if, elif, and else are indented the same amount
def bath_room():
    textFunctions.slowText("Do you want to enter the bathroom?", .05, 1)
    answer = input (">")
    if answer == "yes" or answer == "y":
        textFunctions.slowText("Where would you want to hide?", .05, 1)
        textFunctions.slowText("1. Hide behind the toilet.", .05, 1)
        textFunctions.slowText("2. Hide in the shower.", .05, 1)

        answer = input (">")
            
        if answer == "1":
            textFunctions.slowText("As you hide behind the toilet, the mirror begins to glow a red hue.", .05, 1)
            textFunctions.slowText("A loud screech pierces your ears and you are attacked by an unknown object.", .05, 1)
            textFunctions.slowText("You died", .05, 1)
            game_over()
            textFunctions.slowText("Better luck next time!", .05, 1)
            play_again()
        
        elif answer == "2":
            textFunctions.slowText("As you hide in the shower, you notice through the shower curtain a red hue.", .05, 1)
            textFunctions.slowText("You are paralyzed in fear and notice that you cannot move.", .05, 1)
            textFunctions.slowText("The shower knob starts to turn and acid begins to spray out.", .05, 1)
            textFunctions.slowText("Your flesh is dissolved to the bone.", .05, 1)
            textFunctions.slowText("You died!", .05, 1)
            game_over()
            textFunctions.slowText("That was a painful way to go.", .05, 1)
            play_again()
       
    else:
        common_room()

def childs_room():
    textFunctions.slowText("You realize door number 2 is a child's bedroom.", .05, 1)
    textFunctions.slowText("Do you want to enter room?", .05, 1)

    answer = input (">")
            
    if answer == "y" or answer == "yes":
        textFunctions.slowText("You've entered the childs room", .05, 1)
        textFunctions.slowText("You see a few places you could hide.", .05, 1)
        textFunctions.slowText("Do you:", .05, 1)
        textFunctions.slowText("1. Hide under the bed.", .05, 1)
        textFunctions.slowText("2. Hide in the closet.", .05, 1)
    
    answer = input (">")
        
    if answer == "1":
        textFunctions.slowText("As you hide under the bed, you notice a lever.", .05, 1)
        textFunctions.slowText("The lever being pulled causes spikes to come up from the floors which pierce your body.", .05, 1)
        textFunctions.slowText("You died!", .05, 1)
        game_over()
        textFunctions.slowText("The point was rather sharp on that one, ouch!", .05, 1)
        play_again()
    elif answer == "2":
        textFunctions.slowText("You hide away in the closet and hear footsteps getting louder.", .05, 1)
        textFunctions.slowText("You notice a lever next to you.", .05, 1)
        textFunctions.slowText("Do you press the switch?", .05, 1)
        answer = input (">")
        if answer == "y" or answer == "yes":
            secret_passage()
        elif answer == "n" or answer == "no":
            textFunctions.slowText("The door flings open, the closet door no longer hides you.", .05, 1)
            textFunctions.slowText("An unknown objects makes a loud screeching noise, dashes toward you and rips your heart out.", .05, 1)
            textFunctions.slowText("You died!", .05, 1)
            game_over()
            textFunctions.slowText("Maybe you should have pressed that button?", .05, 1)
            play_again()
    else:
        common_room

def secret_passage ():               
        textFunctions.slowText("You have pushed the button, it opened a secret passage which lead to another room.", .05, 1)
        master_room()
    

def master_room():
    textFunctions.slowText("Do you want to enter the master room?", .05, 1)
    answer = input (">")
    if answer == "yes" or answer == "y":
        textFunctions.slowText("You've found a huge room that looks like a master bedroom.", .05, 1)
        textFunctions.slowText("You notice a huge wardrobe in against the wall or a walk in closet.", .05, 1)
        textFunctions.slowText("Do you want to hide in the:", .05, 1)
        textFunctions.slowText("1. Wardrobe or 2. Closet", .05, 1)
    
    answer = input (">")
        
    if answer == "1":
        textFunctions.slowText("You've entered the wardrobe, but as you shut the door, you felt something to your side.", .05, 1)
        textFunctions.slowText("The object screeched, pushed you out of the wardrobe and killed you.", .05, 1)
        textFunctions.slowText("You died!", 0.05, 1)
        game_over()
        textFunctions.slowText("I suppose the walk in closet would have been a better choice!", .05, 1)
        play_again()
    elif answer == "2":
        textFunctions.slowText("You've been searching around and found a vent which you could pass through.", .05, 1)
        textFunctions.slowText("As you pass through, you find a note which states how to get out", .05, 1)
        textFunctions.slowText("The note states 'An artifact obtained, to fight the object, found somewhere below.", .05, 1)
        textFunctions.slowText("Shall you leave the vent space back to the common room?", .05, 1)

        answer = input (">")
        
        if answer == "yes" or answer == "y":
            common_room()
        else:
            game_over()
        textFunctions.slowText("The object found you as you were sitting around being lazy!", .05, 1)
        play_again()
    else:
        common_room()

def kitchen_room():
    textFunctions.slowText("Door number 4 happens to be the kitchen.", .05, 1)
    textFunctions.slowText("Do you want to enter?", .05, 1)
    
    answer = input (">")
    
    if answer == "yes" or answer == "y":
        textFunctions.slowText("You've entered the kitchen.", .05, 1)
        textFunctions.slowText("You notice a two locations to hide:", .05, 1)
        textFunctions.slowText("1. In the cubboards.", .05, 1)
        textFunctions.slowText("2. In the pantry", .05, 1)

        answer = input (">")

        if answer == "1":
            textFunctions.slowText("As you hide in the cubbards, you feel the skulls of those that have been found before you.", .05, 1)
            textFunctions.slowText("Unintendedly, you scream loudly", 0.05, 1)
            textFunctions.slowText("The object finds you and you become another decoration in the cubbards.", .05, 1)
            game_over()
            textFunctions.slowText("At least your remains will be on display...", .05, 1)
            play_again()
        elif answer == "2":
            textFunctions.slowText("You got hungry and started to eat the box of cheezits.", .05, 1)
            textFunctions.slowText("With a full stomach, you decide to return back to the common room.", .05, 1)
            common_room()
    else:
        common_room

def family_room():
        textFunctions.slowText("As you open door 5, it displays a family room.", 0.05, 1)
        textFunctions.slowText("Do you want to 1enter the family room?", 0.05, 1)

        answer = input(">")

        if answer == "y" or answer == "yes":
            textFunctions.slowText("There is nothing interesting in this room and no where to hide.", 0.05 , 1)
            textFunctions.slowText("Lets go back to the common room.", 0.05, 1)
            common_room()
        else:
            common_room()

def basement_room():
    textFunctions.slowText("As you open door 6, its a flight of stairs that lead to a basement", .05, 1)
    textFunctions.slowText("It's dark, do you want to go into the basement?", .05, 1)
    
    answer = input (">")

    if answer == "yes" or answer == "y":
        textFunctions.slowText("As you approach the bottom of the steps, you notice a bright light in the back corner.", .05, 1)
        textFunctions.slowText("You also notice a noise coming from a vent in the wall.", .05, 1)
        textFunctions.slowText("Which sensory object do you want to check?", .05, 1)
        textFunctions.slowText("1. Bright Light", .05, 1)
        textFunctions.slowText("2. Weird Sound", .05, 1)

        answer = input(">")

        if answer == "1":
            textFunctions.slowText("You've found an orb key; it looks like it is responsible for unlocking something.", .05, 1)
            textFunctions.slowText("There must be something to unlock in another room.", .05, 1)
            common_room_orb()
        elif answer == "2":
            textFunctions.slowText("As you approach the noise, it stops.", .05, 1)
            textFunctions.slowText("Confused, you look closer, and closer, and.....", .05, 1)
            textFunctions.slowText("The object pops out of the vent and eats your head.", .05, 1)
            game_over()
            textFunctions.slowText("You died", .05, 1)
            play_again()
    else:
        common_room()

def stairs():
    textFunctions.slowText("As you walk up the stairs, you hear the loud screeching coming across the common room floor.", .05, 1)
    textFunctions.slowText("The object follows you up the stairs.", .05, 1)
    textFunctions.slowText("You see an open window, do you jump?", .05, 1)

    answer = input (">")
    
    if answer == "y" or answer == "yes":
        textFunctions.slowText("You fell out of the window and broke all your bones.", .05, 1)
        textFunctions.slowText("The object comes for you and drags your body back into the house.", .05, 1)
        textFunctions.slowText("You died!", .05, 1)
        game_over()
        textFunctions.slowText("Suffering is a part of the terror!", .05, 1)
        play_again()
    if answer == "n" or answer == "no":
        textFunctions.slowText("The object catches up with you while passing the open window.", .05, 1)
        textFunctions.slowText("There was no getting away, the object bit you limb by limb.", .05, 1)
        textFunctions.slowText("You died! Bit by Bit", .05, 1)
        game_over()
        textFunctions.slowText("When you find out you taste like chicken!", .05, 1)
        play_again()

def common_room_orb():
    textFunctions.slowText("You've returned to the common room, where should you go from here to find the way out?", .05, 1)
    textFunctions.slowText("There must be a way now, choose doors 1-6 or (s)stairs.", .05, 1)

    answer = input (">")

    if answer == "1":
        bath_room_orb()
    elif answer == "2":
        childs_room()
    elif answer == "3":
        master_room()
    elif answer == "4":
        kitchen_room()
    elif answer == "6":
        basement_room()
    elif answer == "s":
        stairs()

def bath_room_orb():
    textFunctions.slowText("Do you want to enter the bathroom?", .05, 1)

    answer = input(">")

    if answer == "yes" or answer == "y":
        textFunctions.slowText("Where would you want to hide?", .05, 1)
        textFunctions.slowText("1. Hide behind the toilet.", .05, 1)
        textFunctions.slowText("2. Hide in the shower.", .05, 1)

        answer = input (">")

        if answer == "1" or answer == "2":
            textFunctions.slowText("Wait a second, the illumination of the orb has shown a box on the floor.", .05, 1)
            textFunctions.slowText("Should you open it?", .05, 1)

            if answer == "yes" or "y":
                textFunctions.slowText("You've discovered an artifact with a note.", .05, 1)
                textFunctions.slowText("The note states: You can stay and kill the object or take your chances at the door!", .05, 1)
            elif answer == "no" or answer == "n":
                textFunctions.slowText("You hear a noise and a screech.", .05, 1)
                textFunctions.slowText("The object found you and wants the orb back!", .05, 1)
                textFunctions.slowText("He destroys you to an unrecognizeable form.", .05, 1)
                game_over()
                textFunctions.slowText("You died.", .05, 1)
    else:
        common_room()

    



#Functions for game over and replay
def game_over():
    textFunctions.slowText("Game Over", .05, 1)
def play_again():
    textFunctions.slowText("Do you want to play again?", .05, 1)
    
    answer = input (">")

    if answer == "yes" or answer == "y":
        start()
    else:
        quit()

    
      
##Calling function below:
start()

    
      
