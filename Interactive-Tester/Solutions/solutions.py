#Mitchell Toth
#3/19/2020

#Solution document for "simplePythonChallenges".
#Below you will find examples of functions that solve the challenges.
#The functions in this document should be in parallel with the ones
#    in the given challenge files.


#--------------------------CHALLENGES--------------------------

def C1_returnTheLarger(a,b):
    if a > b: return a
    if a < b: return b
    return a-b  #could also return 0 here



def C2_reverseArray(arr):
    #Easiest way is to use the slicing operator
    return arr[::-1]

    #Alternatively, iterate and swap 2 values at a time
    for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    return arr



def C3_isPalindrome(word):
    #Easiest solution:
    return word == word[::-1]

    #Iterative solution
    for i in range(len(word)//2):
        if word[i] != word[len(word)-1-i]:
            return False
    return True

    #Recursive solution
    if len(word) < 2:  #the word is a palindrome by default if small enough
        return True
    if word[0] == word[-1]:  #check first and last letters
        return C3_isPalindrome(word[1:len(word)-1])  #"chop up" the word
    else:
        return False



def C4_addAllOdds(number):
    #Iterative solution
    number = str(number)
    odds_sum = 0
    for i in range(1,len(number),2):
        odds_sum += int(number[i])
    return odds_sum

    #Recursive solution
    number = str(number)
    if len(number) < 2:
        return 0
    return int(number[1]) + C4_addAllOdds(number[2:])



def C5_rockPaperScissors(p1, p2):
    moves=["paper","rock","scissors"]
    if p1 not in moves or p2 not in moves:
        return "Invalid player!"
    elif (p1 == moves[0] and p2 == moves[1]) or (p1 == moves[1] and p2 == moves[2]) or (p1 == moves[2] and p2 == moves[0]):
        return p1+" beats "+p2+"!"
    elif (p2 == moves[0] and p1 == moves[1]) or (p2 == moves[1] and p1 == moves[2]) or (p2 == moves[2] and p1 == moves[0]):
        return p2+" beats "+p1+"!"
    elif p1 == p2:
        return "Tie game!"

    #Another, more fleshed out way
    tie = False
    error = False
    winner = ""

    if p1 == "rock":
        if p2 == "scissors":
            winner = p1
        elif p2 == "paper":
            winner = p2
        elif p2 == "rock":
            tie = True
        else:
            error = True
    elif p1 == "paper":
        if p2 == "rock":
            winner = p1
        elif p2 == "scissors":
            winner = p2
        elif p2 == "paper":
            tie = True
        else:
            error = True
    elif p1 == "scissors":
        if p2 == "paper":
            winner = p1
        elif p2 == "rock":
            winner = p2
        elif p2 == "scissors":
            tie = True
        else:
            error = True
    else:
        error = True

    if error:
        return "Invalid player!"
    if tie:
        return "Tie game!"
    if winner == p1:
        loser = p2
    else:
        loser = p1
    return winner + " beats " + loser + "!"



def C6_countCode(string):
    #Iterative solution
    total = 0
    for i in range(len(string)-3):
        fourChars = string[i:i+4]
        if fourChars[0:2] == "co":
            if fourChars[3] == "e":
                total += 1
    return total

    #Recursive solution
    if len(string) < 4:
        return 0
    if string[0:2] == "co" and string[3] == "e":
        return 1 + C6_countCode(string[1:])
    else:
        return 0 + C6_countCode(string[1:])



#--------------------------WARMUPS--------------------------

def W1_isNegativeThree(num):
    return num == -3


def W2_isSixCharactersLong(word):
    return len(word) == 6


def W3_howExpensive(cost):
    if cost > 200:
        return "That's expensive!"
    return "That's dirt cheap!"


def W4_howExpensive2(cost):
    if cost > 200:
        return "That's expensive!"
    elif cost == 200:
        return "That's a fair price!"
    elif cost < 0:
        return "That's a steal!"
    else:
        return "That's dirt cheap!"

    #Another way to look at it
    if cost < 0:
        return "That's a steal!"
    elif cost >= 0 and cost < 200:
        return "That's dirt cheap!"
    elif cost == 200:
        return "That's a fair price!"
    else:
        return "That's expensive!"
    

def W5_toBuyOrNotToBuy(cost, essential):
    return (essential or cost <= 4)

    #Another solution
    if essential:
        return True
    return cost <= 4


def W6_lastElement(arr):
    return arr[len(arr)-1]

    #Can also use negative indices
    return arr[-1]


def W7_isItemInArray(arr, item):
    for a in arr:
        if a == item:
            return True
    return False


def W8_sumTheContents(arr):
    total = 0
    for num in arr:
        total += num
    return total


def W9_stringGreeting(myName, yourName):
    return "Hello " + yourName + "! My name is " + myName + "."

    #Could also build a 'greeting' variable
    greeting = ""
    greeting += "Hello " + yourName + "!"
    greeting += " My name is " + myName + "."
    return greeting


def W10_buildArray(a, b, c):
    #Simplest way is to make a literal array
    return [a,b,c]

    #Alternatively, you can build an array with .append()
    array = []
    array.append(a)
    array.append(b)
    array.append(c)
    return array


