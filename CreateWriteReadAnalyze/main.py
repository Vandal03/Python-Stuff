import os.path
import functions


##Open/Create Txt File
if os.path.isfile('numFile.txt'):
  functions.writeNums("numFile.txt", "w")
else:
  functions.writeNums("numFile.txt", "x")

##Read Txt File
nums = functions.readNums("numFile.txt")

##Anaylyze Nums
##Find Sum of numFile.txt
numSum = functions.sumNums(nums)

##Find Min of numFile.txt
numMin = functions.numMin(nums)

##Find Max of numFile.txt
numMax = functions.numMax(nums)

print("The sum of all the numbers is {sum}, the smallest number is {min}, and the largest number is {max}".format(sum = numSum, min = numMin, max = numMax))