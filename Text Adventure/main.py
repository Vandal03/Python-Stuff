import rooms
import textFunctions
import character
import intro

textFunctions.slowText("You come across an abandoned house in the woods. It's quiet, and you hear a noise coming from inside. ", 0.05, 1)
textFunctions.slowText("Do you want to knock on the door, or walk on in? ", 0.05, 1)
choice = input("Enter 1 to knock, and enter 2 to walk on in. > ")
print("\n")
player = rooms.entrance(choice)

player = rooms.mirror(player)

