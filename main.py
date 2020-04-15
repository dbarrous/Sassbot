import re
import random

from quickResponses import QRregexList, responsesDict, smartComebacks, exitMessages
from dialogTrees import DTregexList, RegexToTree, Trees

# Searches and Assigns Regex Keys from the Quick Responses


def regexAssignment(userInput):
    if userInput == "":

        return ""
    else:
        for regex in QRregexList:
            check = re.search(regex, userInput, re.IGNORECASE)
            if check:
                return regex


# Searches and Assigns Responses based off the Regex keys from the Quick Responses

def responseAssignment(currentRegex):
    if currentRegex == None or currentRegex == "":
        return ""

    else:
        return random.choice(responsesDict[currentRegex])


# Searches and Starts a Special Dialog Tree Sequence

def dialogTraversal(userInput):
    node = 0
    for regex in DTregexList:
        check = re.search(regex, userInput, re.IGNORECASE)
        if check:
            tree = RegexToTree[regex]
            currentResponse = Trees[tree]
            node = 1
            treeLength = len(Trees[tree])
            print(currentResponse[node][0])
            dialogInput = input("Answer: ")
            while node < treeLength:
                regex = currentResponse[node][1]
                check = re.search(regex, dialogInput, re.IGNORECASE)
                if check:
                    node = node + 1
                    print(currentResponse[node][0])
                    if node < treeLength:
                        dialogInput = input("Answer: ")
                else:
                    print(random.choice(smartComebacks))
                    break
    if node < 1:
        print(random.choice(smartComebacks))


# Driver Function

def start():
    # Variables used throughout
    userInput = ""
    currentRegex = ""

    # Start Message/Information
    print("\nSassbot 3000 created by the Marvelous Damian and the Devious Alexander\n\nInstructions:\nTalk to it as you would any other chatbot, but beware it is not exactly helpful in anyway, only entertaining if being insulted by a computer is your idea of entertainment.\n\nHint: There are hidden dialog trees, maybe ask it about the meaning of life or about it's name.\n\nTo EXIT just hit enter on a blank line!")

    while True:
        userInput = input("You >  ")
        if userInput == "":
            exit(random.choice(exitMessages))
        currentRegex = regexAssignment(userInput)
        response = responseAssignment(currentRegex)
        if response == "":
            dialogTraversal(userInput)

        else:
            print(response)


# Starts it up

start()
