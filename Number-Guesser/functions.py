def playGame(randomNumber):
  response = input("Do you want to play the guessing game? (Y/N)\n >")
  if response.upper() == 'Y':
    print("Great! Let's get started.")
    hintsGiven = []
    guessesLeft = 5
    hintsGuesses(randomNumber, hintsGiven, guessesLeft)
  elif response.upper() == 'N':
    print("Too bad. Come back later if you want.")
  else:
    print("That response wasn't valid.")
    playGame(randomNumber)


def hintsGuesses(randomNumber, hintsGiven, guessesLeft):
  if randomNumber % 3 == 0 and 1 not in hintsGiven:
    print("The number is divisible by 3")
    hintsGiven.append(1)
  elif randomNumber % 2 == 0 and 2 not in hintsGiven:
    print("The number is divisible by 2")
    hintsGiven.append(2)
  elif randomNumber > 50 and 3 not in hintsGiven:
    print("The number is > 50")
    hintsGiven.append(3)
  elif randomNumber < 50 and 4 not in hintsGiven:
    print("The number is < 50")
    hintsGiven.append(4)
  elif randomNumber < 25 and 5 not in hintsGiven:
    print("The number is < 25")
    hintsGiven.append(5)
  elif randomNumber > 75 and 6 not in hintsGiven:
    print("The number is > 75")
    hintsGiven.append(6)
  elif guessesLeft == 1:
    calcAnswer = randomNumber * 7
    print("Solve the following equation to get the number")
    print(f"x * 7 = {calcAnswer}")
  
  guess = input('Please take a guess \n >')
  try: 
    if int(guess) == randomNumber:
      print("You did it! Good job")
    elif int(guess) != randomNumber:
      guessesLeft -= 1
      if guessesLeft == 0:
        print(f"Game Over. The number was {randomNumber}")
      else:
        print(f"Incorrect. Sorry, but you have {guessesLeft} guesses left")
        hintsGuesses(randomNumber, hintsGiven, guessesLeft)
  except:
    print("Please enter an integer!")
    hintsGiven.pop()
    hintsGuesses(randomNumber, hintsGiven, guessesLeft)