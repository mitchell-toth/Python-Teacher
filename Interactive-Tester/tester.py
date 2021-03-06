#--------------------------------SETUP-----------------------------------

from Solutions import solutions
from Data import data
import inspect
import importlib
import copy

#Catch any syntax errors in user's code
try:
    from Problems import warmups, challenges
except Exception as e:
    print("ERROR: " + str(e))
    print("Please fix your code before re-running 'tester.py'.\n")
    exit()

#Import as normal if everything is alright
from Problems import warmups, challenges

DATA = data.DATA
FILES = ["warmups.py", "challenges.py"]
CHOSEN_FILE = ""



#--------------------------------TESTER----------------------------------



def printHints(file, problems_functions):
    print("Hints:\n")
    for i in range(len(problems_functions)):
        funcName = problems_functions[i][0]
        endOfPrefix = (problems_functions[i][0]).find("_")+1
        print(" ", funcName[endOfPrefix:]+":")
        for hint in DATA[file]["hints"][funcName]:
            print("    ", hint)
        print()


def askIfTestAgain():
    goAgain = input("Do some more testing? y/n => ")
    if (goAgain.upper() == "Y"):
        print("_"*50)
        return True
    return False


def convertToDictionary(listOfTuples):
    dictionary = {}
    for tp in listOfTuples:
        dictionary[tp[0]] = tp[1]
    return dictionary


def putInNumericalOrder(problems_functions):
    problemNumbers = []
    problems = {}
    for tup in problems_functions:
        pn = int(tup[0][1 : tup[0].find("_")])
        problemNumbers.append(pn)
        problems[pn] = tup
    problemNumbers.sort()
    problems_functions = []
    for pn in problemNumbers:
        problems_functions.append(problems[pn])
    return problems_functions


def get_file():
    print("Files to choose from:\n")
    print("   ", 1, " ------- ", FILES[0])
    print("   ", 2, " ------- ", FILES[1])
    print("\nPlease specify the number of the file you would like to use.")
    file_to_test = input(" => ")
    print()
    return file_to_test


def get_tests(problems_functions, solutions_functions, file):
    global CHOSEN_FILE
    print("Challenges To Test: (" + file + ")")
    for i in range(len(problems_functions)):
        endOfPrefix = (problems_functions[i][0]).find("_")+1
        print("    %2d -------  %s" % (i+1, problems_functions[i][0][endOfPrefix:]))
    print("\nPlease specify the numbers of the challenges you would like to test, separating each by a comma.")
    print("Input nothing to activate all the tests.")
    print('Type "F" to change test files.')
    print('Type "R" to recompile.')
    print('Type "Hints" to receive helpful hints.')
    problems_to_test = str(input(" => ")).upper()
    print()
    return problems_to_test.split(",")


def run_tests():
    global CHOSEN_FILE
    testAgain = True
    print("\n"*40)
    while(testAgain):
        try:
            importlib.reload(solutions)
            importlib.reload(warmups)
            importlib.reload(challenges)
        except Exception as e:
            print("ERROR: " + str(e))
            print("You must fix your code before you can continue testing.\n")
            testAgain = askIfTestAgain()
            if testAgain:
                print("\n"*40)
            continue
            
        warmups_functions = inspect.getmembers(warmups, inspect.isfunction)
        challenges_functions = inspect.getmembers(challenges, inspect.isfunction)
        solutions_functions = convertToDictionary(inspect.getmembers(solutions, inspect.isfunction))

        if CHOSEN_FILE == "":
            CHOSEN_FILE = get_file()
        if CHOSEN_FILE == "1":
            problems_functions = warmups_functions
            file = FILES[0]
        elif CHOSEN_FILE == "2":
            problems_functions = challenges_functions
            file = FILES[1]
        else:
            CHOSEN_FILE = ""
            continue

        problems_functions = putInNumericalOrder(problems_functions)
        problems_to_test = get_tests(problems_functions, solutions_functions, file)
        header = "  Results:"
        if problems_to_test == [""]:
            problems_to_test = list(range(1, len(problems_functions)+1))
        elif problems_to_test == ["HINTS"]:
            printHints(file, problems_functions)
            problems_to_test = []
            header = ""
        elif problems_to_test == ["F"]:
            CHOSEN_FILE = ""
            continue
        elif problems_to_test == ["R"]:
            continue
            
        print(header)
        for testIndex in problems_to_test:
            try:
                testIndex = int(testIndex)-1
                key = problems_functions[testIndex][0]
            except:
                print("     Invalid problem!\n\n")
                continue
            attempt_funct = problems_functions[testIndex][1]
            solution_funct = solutions_functions[key]

            successFail = "SUCCESS --"
            arguments = ""
            message = "All tests passed for '" + key + "'!"
            for test_arguments in DATA[file]["inputs"][key]:
                try:
                    test_arguments_copy = copy.deepcopy(test_arguments)
                    correctResults = solution_funct(*test_arguments_copy)
                    test_arguments_copy = copy.deepcopy(test_arguments)
                    attemptResults = attempt_funct(*test_arguments_copy)
                except Exception as e:
                    successFail = "FAILURE --"
                    message = "ERROR: " + str(e)
                    break
                if attemptResults != correctResults:
                    successFail = "FAILURE --"
                    arguments = ""
                    for i in range(len(test_arguments)):
                        if i == (len(test_arguments)-1):
                            arguments += str(test_arguments[i])
                        else:
                            arguments += str(test_arguments[i]) + ", "
                    arguments = key + "(" + arguments + ") --"
                    message = " Expected " + str(correctResults) + ", got " + str(attemptResults)
                    break
            print("    ", successFail, arguments + message, "\n")
        testAgain = askIfTestAgain()
        if testAgain:
            print("\n"*40)


run_tests()
