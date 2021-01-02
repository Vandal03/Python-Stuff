import time
import sys


def slowText(string, speed, newLineBool):
    for c in string:
        sys.stdout.flush()
        print(c, end="")
        time.sleep(speed)
    
    if int(newLineBool) == 1:
        time.sleep(0.5)
        print("\n")
    else:
        time.sleep(0.5)
        print(" ", end = "")
        

def mirrorPull():
    i = 0
    k = 0
    while i < 5:
        j = 0
        while j < 5:
            if j == 0 + k:
                slowText("*", .05, 0)
                j += 1
            else:
                slowText("|", .05, 0)
                j += 1
        print("\n")
        i += 1 
        k += 1