import random


def writeNums(F, action):
  fileOpen = open(F, action)
  i = 0
  while i < 100:
    randNum = random.randrange(0, 100)
    fileOpen.write(str(randNum) + "\n")
    i += 1
  fileOpen.close()


def readNums(F):
    nums = []
    fileOpen = open(F)
    lines = fileOpen.readlines()
    for line in lines:
        nums.append(line.strip("\n"))
    return nums


def sumNums(array):
    Sum = 0
    for num in array:
        Sum += int(num)
    return Sum

def numMin(array):
    array.sort()
    minNum = array[len(array) - (len(array))]
    return minNum

def numMax(array):
        array.sort()
        maxNum = array[len(array) - 1]
        return maxNum