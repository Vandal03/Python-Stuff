import textFunctions
import character
import items
import potions
import weapons
import rooms

def entrance(choice):
    if int(choice) == 1:
        textFunctions.slowText("*Knock*, *Knock*, ", 0.05, 0)
        textFunctions.slowText(". . . . ", 0.5, 1)
        textFunctions.slowText("The door slowly opens, and you find yourself alone in the common area. ", 0.05, 1)
    elif int(choice) == 2:
        textFunctions.slowText("You slowly open the door, and find yourself alone in the common area. ", 0.05, 1)
    else:
        newChoice = input("Please enter a valid option > ")
        entrance(newChoice)
    
    textFunctions.slowText("In the middle of the room you see a mirror. ", 0.05, 1)
    textFunctions.slowText("You slowly approach the mirror, and as you do, you forget who you are. ", 0.05, 1)
    textFunctions.slowText("Gazing in the mirror your mind trys to hold onto anything it can. You can only hold on to your first name... ", 0.05, 1)
    firstName = input("Enter your first name > ")
    player = character.character(firstName)
    print("\n")
    textFunctions.slowText(f"Hello, {player.firstName}. Says a voice from the mirror... ", 0.05, 1)
    return player
    
def mirror(player):
    textFunctions.slowText("Before you have a chance to comprehend what happened, you are pulled through the mirror. ", 0.05, 1)
    textFunctions.slowText("You fly through some sort of expanse. ", 0.05, 1)
    textFunctions.mirrorPull()
    textFunctions
    textFunctions.slowText("You fly out of the mirror, and come to stop after hitting the floor. ", 0.05, 1)
    textFunctions.slowText("You slowly stand up and notice everything looks familiar. There's only one problem... It's all backwards. ", 0.05, 1)
    textFunctions.slowText("There's something else. There is a bag on your back. You slowly open the bag to find a few items. ", 0.05, 1)
    
    potion = potions.potion("Health Potion", "Potion", "Health", 5, "Restores 5 health.")
    player.addItem(potion)
    
    weapon = weapons.weapon("Iron Dagger", "Weapon", "Dagger", 2, "Small iron dagger (2 damage)" )
    player.addItem(weapon)
    
    return player 


def createHouse():
    