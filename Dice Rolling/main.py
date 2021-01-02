import random

def roll():
    outcome = random.randrange(1,7)
    print(f"You rolled a {outcome}")
    play_again()
        
        
def play_again():
    response = input("Would you like to roll again? Enter Y or N > ")
    
    if response.upper() == "Y":
        roll()
    elif response.upper() == "N":
        print("Too bad")
    else:
        print("Try entering your response again.")
        play_again()
        
        
        
        
roll()