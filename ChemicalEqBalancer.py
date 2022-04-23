import math
import re

reactants = []
product = []

# Each element is formatted in this way: [Name, Subscript, Coefficient]
def createArray(userInput):
    letters = ""
    subscript = ""
    for i in userInput:
        if i.isdigit():
            subscript += i
        else:
            letters += i
    if subscript == "":
        subscript = "1"
    return [letters, int(subscript), 1]

# Getting users reactants
for i in range(2):
    userInput = input("Reactant " + str(i+1) + ": ")
    assert not userInput[0].isdigit(), "Cannot have integer in front of element"
    reactants.append(createArray(userInput))

# Getting users product
userInput = input("Product: ")
assert not userInput[0].isdigit(), "Cannot have integer in front of product"
splitInput = re.sub( r"([A-Z])", r" \1", userInput).split()

product.append(createArray(splitInput[0]))
product.append(createArray(splitInput[1]))

# First element, reactant and product
elementOneR = reactants[0]
elementOneP = product[0]

# Second element, reactant and product
elementTwoR = reactants[1]
elementTwoP = product[1]

# Makes sure elements are the same as reactant and product
if elementOneR[0] != elementOneP[0]:
    elementOneP = product[1]
    elementTwoP = product[0]
    
assert elementOneR[0] == elementOneP[0], elementOneR[0] + " is not the same as " + elementOneP[0]
assert elementTwoR[0] == elementTwoP[0], elementTwoR[0] + " is not the same as " + elementTwoP[0]

# Balancing Algorithm

# Checks if the product of the corresponding elements coefficient and subscript are the same
def isBalanced(elementOneR, elementOneP, elementTwoR, elementTwoP):
    return elementOneR[1] * elementOneR[2] == elementOneP[1] * elementOneP[2] and elementTwoR[1] * elementTwoR[2] == elementTwoP[1] * elementTwoP[2]

# Balances one element (elementReactant and elementProduct), and copies coeffient of elementProduct to otherProduct
def balanceElement(elementReactant, elementProduct, otherProduct): 
    lcm = math.lcm(elementReactant[1] * elementReactant[2], elementProduct[1] * elementProduct[2])
    elementReactant[2] = int(lcm/elementReactant[1])
    elementProduct[2] = int(lcm/elementProduct[1])
    otherProduct[2] = elementProduct[2]

# Cycles between balancing element one and two
balancing1 = True
while not isBalanced(elementOneR, elementOneP, elementTwoR, elementTwoP):
    if balancing1:
        balanceElement(elementOneR, elementOneP, elementTwoP)
    else:
        balanceElement(elementTwoR, elementTwoP, elementOneP)
    balancing1 = not balancing1

# Simplifies all coefficients together
gcd = math.gcd(elementOneR[2], elementOneP[2], elementTwoR[2], elementTwoP[2])
elementOneR[2] //= gcd
elementOneP[2] //= gcd
elementTwoR[2] //= gcd
elementTwoP[2] //= gcd

def getElementStr(elementList):
    temp = str(elementList[2]) + elementList[0]
    if elementList[1] != 1:
        temp += str(elementList[1])
    return temp

part1 = getElementStr(elementOneR)
part2 = getElementStr(elementTwoR)
part3 = str(elementOneP[2]) + userInput

print(part1 + " + " + part2 + " -> " + part3)