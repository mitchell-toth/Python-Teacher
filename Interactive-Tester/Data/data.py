import random

FILES = ["warmups.py", "challenges.py"]
DATA = {}
for file in FILES:
    DATA[file] = {}
    DATA[file]["inputs"] = {}
    DATA[file]["hints"] = {}

#Some helpful variables
ALPHABET_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPER = ALPHABET_LOWER.upper()
BOOLEANS = [True, False]

#warmups.py
#---------------------------------------------------------------
functions = ["W1_isNegativeThree",
             "W2_isSixCharactersLong",
             "W3_howExpensive",
             "W4_howExpensive2",
             "W5_toBuyOrNotToBuy",
             "W6_lastElement",
             "W7_isItemInArray",
             "W8_sumTheContents",
             "W9_stringGreeting",
             "W10_buildArray"
             ]

inputs = {}
for func in functions:
    inputs[func] = []


#isNegativeThree
for i in range(-10,10):
    inputs[functions[0]].append([i])
inputs[functions[0]].append([-33])
inputs[functions[0]].append([-333])


#isSixCharactersLong
for i in range(100):
    wordSize = random.randint(0,10)
    word = ""
    for j in range(wordSize):
        letterIndex = random.randint(0,25)
        word += ALPHABET_LOWER[letterIndex]
    inputs[functions[1]].append([word])
inputs[functions[1]].append([""])
inputs[functions[1]].append(["phrase"])
inputs[functions[1]].append(["123456"])
inputs[functions[1]].append(["trees"])
inputs[functions[1]].append(["laptops"])


#howExpensive
for i in range(-100,400):
    inputs[functions[2]].append([i])


#howExpensive2
for i in range(-100,400):
    inputs[functions[3]].append([i])


#toBuyOrNotToBuy
for i in range(-50,50):
    inputs[functions[4]].append([i,False])
for i in range(-50,50):
    inputs[functions[4]].append([i,True])


#lastElement
for i in range(100):
    arr_size = (i % 10) + 1
    container = []
    arr = []
    for j in range(arr_size):
        num = random.randint(-100,100)
        arr.append(num)
    container.append(arr)
    inputs[functions[5]].append(container)


#isItemInArray
for i in range(50):
    container = []
    arr = []
    for j in range(6):
        num = random.randint(0,30)
        arr.append(num)
    if i > 20:
        item = arr[random.randint(0,5)]
    else:
        item = random.randint(31,60)
    container.append(arr)
    container.append(item)
    inputs[functions[6]].append(container)


#sumTheContents
for i in range(100):
    length = random.randint(0,10)
    container = []
    arr = []
    for j in range(length):
        num = random.randint(-1000,1000)
        arr.append(num)
    container.append(arr)
    inputs[functions[7]].append(container)


#stringGreeting
inputs[functions[8]].append(["Bob","John"])
inputs[functions[8]].append(["John","Bob"])
inputs[functions[8]].append(["Emily","Sienna"])
inputs[functions[8]].append(["Colin","Savannah"])
inputs[functions[8]].append(["Tim","Will"])
inputs[functions[8]].append(["Aaron","Moses"])
inputs[functions[8]].append(["Eve","Adam"])
inputs[functions[8]].append(["Bonnie","Clyde"])


#buildArray
for i in range(100):
    args = []
    for j in range(3):
        q = random.randint(0,1)
        if q:
            p = random.randint(0,25)
            args.append(ALPHABET_UPPER[p])
        else:
            p = random.randint(-100,100)
            args.append(p)
    inputs[functions[9]].append(args)





hints = {functions[0]:
         ["Recall that the equality operator is '=='."
            ],
         functions[1]:
         ["Use the len() function to get the length of the string.",
          "In this case, the syntax would look like 'len(word)'."
             ],
         functions[2]:
         ["Use an if/else statement for this along with the '>' operator."
             ],
         functions[3]:
         ["Use if/else statements to cover the edge cases of 200 and 0."
             ],
         functions[4]:
         ["If 'essential' is True, then no further consideration is needed.",
          "Otherwise, the 'cost' needs to be considered."
             ],
         functions[5]:
         ["Recall that indexing into an array has the form 'arr[index]'.",
          "Consider how the length of an array relates to its indices."
             ],
         functions[6]:
         ["Try out a for loop that compares each array element against 'item'."
             ],
         functions[7]:
         ["Make a variable to keep track of the sum so far, starting at 0.",
          "Then iteratively add to that sum using a for loop."
             ],
         functions[8]:
         ["The addition operator '+' can also do string concatenation.",
             ],
         functions[9]:
         ["Try starting with an empty array 'arr', then use 'arr.append()'.",
             ]
        }

DATA[FILES[0]]["inputs"] = inputs
DATA[FILES[0]]["hints"] = hints


#challenges.py
#---------------------------------------------------------------
functions = ["C1_returnTheLarger",
             "C2_reverseArray",
             "C3_isPalindrome",
             "C4_addAllOdds",
             "C5_rockPaperScissors",
             "C6_countCode"
             ]

inputs = {}
for func in functions:
    inputs[func] = []
    

#returnTheLarger
for i in range(-100,100):
    q = random.randint(0,3)
    inputs[functions[0]].append([i,i+q])
inputs[functions[0]].append([4,4])

#reverseArray
for i in range(100):
    arr_size = random.randint(0,10)
    container = []
    arr = []
    for j in range(arr_size):
        num = random.randint(-100,100)
        arr.append(num)
    container.append(arr)
    inputs[functions[1]].append(container)

#isPalindrome
words = ["racecar", "raerr", "eorjtfmsoe", "qwertewq", "balloon", "four", "santa", "hannah", "radar", "palindrome", "I", "", "AAA", "16", "22", "8535"]
for word in words:
    inputs[functions[2]].append([word])

#addAllOdds
for i in range(100):
    rand = random.randint(0, 400000)
    inputs[functions[3]].append([rand])

#rockPaperScissors
moves = ["rock", "paper", "scissors"]
for p1 in moves:
    for p2 in moves:
        inputs[functions[4]].append([p1, p2])
inputs[functions[4]].append(["gun", "rock"])
inputs[functions[4]].append(["paper", "sword"])
inputs[functions[4]].append(["bomb", "scissors"])
inputs[functions[4]].append(["rocket", "rocket"])
inputs[functions[4]].append(["", ""])

#countCode
inputs[functions[5]].append(["aaacodebbb"])
inputs[functions[5]].append(["codexxcode"])
inputs[functions[5]].append(["cozexxcope"])
inputs[functions[5]].append(["codecodecodecode"])
inputs[functions[5]].append([""])
inputs[functions[5]].append(["xuwmfckqxkcoeela"])
inputs[functions[5]].append(["rkscoperkcooelacooo"])
inputs[functions[5]].append(["coding"])
inputs[functions[5]].append(["coke is delicious"])
inputs[functions[5]].append(["cozey code"])
inputs[functions[5]].append(["elephant"])
inputs[functions[5]].append(["colly dog"])
inputs[functions[5]].append(["c"])
inputs[functions[5]].append(["co"])
inputs[functions[5]].append(["cod"])
inputs[functions[5]].append(["codo"])
inputs[functions[5]].append(["code"])
inputs[functions[5]].append(["cose"])
inputs[functions[5]].append(["coie"])
inputs[functions[5]].append(["coio"])


#hints
hints = {functions[0]:
         ["Try some if/else statements to solve this."
            ],
         functions[1]:
         ["Try to work through how you would do this for a small array, like [1,2,3].",
          "Recall that indexing into an array has the form 'arrayObject[index]'.",
          "Try swapping the first and last elements and moving your way inward."
             ],
         functions[2]:
         ["For a word to be a palindrome, the letters must have a sort of symmetry.",
          "You can index into a string just like an array.",
          "It may help to refer back to how reverseArray was solved."
             ],
         functions[3]:
         ["You may want to cast the number to a string with 'str(number)'.",
          "Then you can index into the odd positions using 'number[index]'.",
          "You may also need to do integer casting with 'int(string)'."
             ],
         functions[4]:
         ["Try to think of all the possible combinations.",
          "Help yourself by making extra variables to keep track of the winner/loser."
             ],
         functions[5]:
         ["Try going 4 letters at a time with the given string, using a loop.",
          "Make a variable that keeps track of the total, then return that variable.",
          "Recall that you can grab parts of a string using the slicing operator.",
          "So the first two letters of a string are given by 'string[0:2]'."
             ]
        }

DATA[FILES[1]]["inputs"] = inputs
DATA[FILES[1]]["hints"] = hints

