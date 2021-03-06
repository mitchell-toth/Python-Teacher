
#Magic you don't need to worry about
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checkAnswer(problemNumber, functionName, argumentPassed, expectedOutput, userOutput, multipleCorrectAnswers):
    print()
    expectedOutputString = ""
    if multipleCorrectAnswers:
        atLeastOneCorrect = False
        for i in range(len(expectedOutput)):
            if userOutput == expectedOutput[i]:
                atLeastOneCorrect = True
            expectedOutputString += str(expectedOutput[i])
            if (i != len(expectedOutput)-1):
                expectedOutputString += " or "
        if atLeastOneCorrect:
            rightOrWrong = "CORRECT!"
        else:
            rightOrWrong = "WRONG!"
    else:
        expectedOutputString = expectedOutput
        if userOutput == expectedOutput:
            rightOrWrong = "CORRECT!"
        else:
            rightOrWrong = "WRONG!"
    argumentPassedString = ""
    for i in range(len(argumentPassed)):
        if i == (len(argumentPassed)-1):
            argumentPassedString += str(argumentPassed[i])
        else:
            argumentPassedString += str(argumentPassed[i]) + ", "
        
    resultMessage = str(rightOrWrong)+" --> "+str(functionName)+"("+argumentPassedString+")"+"... "+"Expected Output: "+str(expectedOutputString)+"... "+"Your Ouput: "+str(userOutput)
    return userOutput == expectedOutput, resultMessage


def printOverallMessage(allCorrect):
    print()
    print()
    if (allCorrect == True):
        print("All correct! Good job!")
    else:
        print("Still some work to do!")


def iterateOverArguments(problemNumber, functionName, argumentsList, expectedOutputList, multipleCorrectAnswers, allCorrect, theFunction):
    print("Problem "+str(problemNumber)+":")
    print()
    for i in range(len(argumentsList)):
        userOutput = theFunction(*(argumentsList[i]))
        correct, resultMessage = checkAnswer(problemNumber, functionName, argumentsList[i], expectedOutputList[i], userOutput, multipleCorrectAnswers)
        print(resultMessage)
        if (correct == False):
            allCorrect = False
    return allCorrect


#Add new problems and their info here
def lookUpProblemInfo(problemNumber):
    multipleCorrectAnswers = False
    if problemNumber == 1:
        functionName = "isThisValueOne"
        theFunction = isThisValueOne
        argumentsList = [[-1], [0], [1], [10]]
        expectedOutputList = [False, False, True, False]
                
    elif problemNumber == 2:
        functionName = "areTheseTwoValuesTheSame"
        theFunction = areTheseTwoValuesTheSame
        argumentsList = [[86, 22], [34.5, 34.5], [-1, 1], [14, 14]]
        expectedOutputList = [False, True, False, True]
        
    elif problemNumber == 3:
        functionName = "areTheseThreeValuesTheSame"
        theFunction = areTheseThreeValuesTheSame
        argumentsList = [[12.4, 18.6, 12.4], [809, 124, 395], [1, 1, 1]]
        expectedOutputList = [False, False, True]
        
    elif problemNumber == 4:
        functionName = "isValue1DivisibleByValue2"
        theFunction = isValue1DivisibleByValue2
        argumentsList = [[28,7], [5,3], [16,4], [10,7]]
        expectedOutputList = [True, False, True, False]

    elif problemNumber == 5:
        functionName = "whichIsGreatest"
        theFunction = whichIsGreatest
        argumentsList = [[-5, 9, 0], [42.1, 42.1, 17], [13, 14, 12]]
        expectedOutputList = [9, 42.1, 14]

    elif problemNumber == 6:
        functionName = "doesThisStringContainRorA"
        theFunction = doesThisStringContainRorA
        argumentsList = [["Python yo"], ["Wassup brother Colin."], ["Really? A better way would be by train!"], [""]]
        expectedOutputList = [False, True, True, False]

    elif problemNumber == 7:
        functionName = "calculateInsuranceRate"
        theFunction = calculateInsuranceRate
        argumentsList = [[17, "male"], [18, "female"], [11, "male"], [34, "female"], [48, "male"], [62, "male"], [88, "female"]]
        expectedOutputList = [1000, 950, "Invalid", 350, 400, 200, 150]

    elif problemNumber == 8:
        functionName = "sumList"
        theFunction = sumList
        argumentsList = [[[1,1,1,1,1]], [[56,72,-3,7]], [[-6,-26,0]]]
        expectedOutputList = [5, 132, -32]

    elif problemNumber == 9:
        functionName = "combineTwoLists"
        theFunction = combineTwoLists
        argumentsList = [[[1,3,7,8],[2,1,4,2,9,-1,7]], [[3,4,5,5,5,1],[5,0,5,2]]]
        expectedOutputList = [[[1,7], [7,1]], [[5,5]]]
        multipleCorrectAnswers = True

    elif problemNumber == 10:
        functionName = "createASimpleDictionary"
        theFunction = createASimpleDictionary
        argumentsList = [[]]
        expectedOutputList = [{"key": "value"}]

    elif problemNumber == 11:
        functionName = "dictionaryKeysList"
        theFunction = dictionaryKeysList
        argumentsList = [[{"name": "Colin", "age": 21, "college": "Asbury University", "degree": "Marketing/Latin"}], [{"race": "latino", "weight": "170lbs", "gender": "male"}]]
        expectedOutputList = [["name", "age", "college", "degree"], ["race", "weight", "gender"]]

    elif problemNumber == 12:
        functionName = "dictionaryValuesList"
        theFunction = dictionaryValuesList
        argumentsList = [[{"name": "Colin", "age": 21, "college": "Asbury University", "degree": "Marketing/Latin"}], [{"race": "latino", "weight": "170lbs", "gender": "male"}]]
        expectedOutputList = [["Colin", 21, "Asbury University", "Marketing/Latin"], ["latino", "170lbs", "male"]]

    elif problemNumber == 13:
        functionName = "storeNumOccurrencesOfUniqueItems"
        theFunction = storeNumOccurrencesOfUniqueItems
        argumentsList = [[[1,1,1,2,2,2,2,2,2,3]], [[2.3, True, True]]]
        expectedOutputList = [[{1:3, 2:6, 3:1}, {1:3, 3:1, 2:6}, {2:6, 1:3, 3:1}, {2:6, 3:1, 1:3}, {3:1, 1:3, 2:6}, {3:1, 2:6, 1:3}], [{2.3:1, True:2}, {True:2, 2.3:1}]]
        multipleCorrectAnswers = True
    
    else:
        print("Bro, give this function a valid problem number!")
        return 0, 0, 0, 0, 0
    return functionName, argumentsList, expectedOutputList, multipleCorrectAnswers, theFunction


def runProblems():
    print("-----------------------------------------------")
    problemNumber = input("Enter a problem number => ")
    try:
        problemNumber = int(problemNumber)
    except:
        problemNumber = -1
    allCorrect = True
    functionName, argumentsList, expectedOutputList, multipleCorrectAnswers, theFunction = lookUpProblemInfo(problemNumber)
    if (functionName != 0):
        allCorrect = iterateOverArguments(problemNumber, functionName, argumentsList, expectedOutputList, multipleCorrectAnswers, allCorrect, theFunction)
        printOverallMessage(allCorrect)
    print("\n\n\n")
    runProblems()
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------














#Exercises begin below

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  #Python exercises: simple functions

  #In large programs, functions like these can actually be quite useful.
  #They're called helper functions, and they simplify various tasks.
  #But you don't really need to know that...

  #These should hopefully reinforce your use of basic coding structures.
  #Fill in these function bodies and have fun!




#----------------------Problem 1-------------------------
  #Simple function that should return true if the value passed in it is one,
  # and false otherwise.
def isThisValueOne(value):
    return "Remove me and add this function's body"





#----------------------Problem 2-------------------------
  #Return true if the two values are the same, false otherwise.
def areTheseTwoValuesTheSame(value1, value2):
    return "Remove me and add this function's body"





#----------------------Problem 3-------------------------
  #Return true if the three values are the same, false otherwise.
def areTheseThreeValuesTheSame(value1, value2, value3):
    return "Remove me and add this function's body"






#----------------------Problem 4-------------------------
  #Return true if the first value is divisible by the second,
  # false otherwise. Hint: remember the operator that does remainder?
def isValue1DivisibleByValue2(value1, value2):
    return "Remove me and add this function's body"






#----------------------Problem 5-------------------------
  #Return the largest number of the three given numbers.
def whichIsGreatest(value1, value2, value3):
    return "Remove me and add this function's body"






#----------------------Problem 6-------------------------
  #Return true/false depending on if the given string contains
  # one or all of the letters "r" or "R" or "a" or "A".
  #Many ways to do it. Just know that you can iterate over
  # characters in a string just like items in a list.
def doesThisStringContainRorA(aString):
    return "Remove me and add this function's body"





#----------------------Problem 7-------------------------
  #Given an integer age and either "male" or "female", return
  # the customer's insurance payment. Here's what to return:
  #For ages 15 and below, return the string "Invalid".
  #Ages 16 - 22 have to pay $950 per month.
  #Ages 23 - 55 have to pay $350 per month.
  #Ages 56+ have to pay $150 per month.
  #However, males always have to pay an additional $50.
  #Return integers (no need for dollar sign).
def calculateInsuranceRate(age, gender):
    return "Remove me and add this function's body"







#----------------------Problem 8-------------------------
  #Return the sum of a list of numbers. For example, for
  # a list [1,2,3,4] the sum would be 10.
def sumList(aList):
    return "Remove me and add this function's body"







#----------------------Problem 9-------------------------
  #Given two lists, return a single list that contains
  # only the values that both of the given lists share.
def combineTwoLists(list1, list2):
    return "Remove me and add this function's body"







#----------------------Problem 10------------------------
  #Intro to dictionaries. Create a dictionary with one
  # key/value pair, where the key is the string "key" and
  # its corresponding value is the string "value".
def createASimpleDictionary():
    return "Remove me and add this function's body"








#----------------------Problem 11------------------------
  #Return a list of the provided dictionary's keys.
  #Your list should contain the keys in the order they appear in the
  # provided dictionary.
def dictionaryKeysList(aDictionary):
    return "Remove me and add this function's body"









#----------------------Problem 12------------------------
  #Return a list of the provided dictionary's values.
  #Your list should contain the values in the order they appear in the
  # provided dictionary.
def dictionaryValuesList(aDictionary):
    return "Remove me and add this function's body"









#----------------------Problem 13------------------------
  #Return a dictionary containing the number of times each unique
  # entry appears in a given list. For example, one key/value pair
  # would look like uniqueEntry: countOfThisEntry.
def storeNumOccurrencesOfUniqueItems(aList):
    return "Remove me and add this function's body"













#This runs the answer checking code and will prompt you for a problem number.
runProblems()
