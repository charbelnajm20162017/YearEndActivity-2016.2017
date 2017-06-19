#Charbel Najm
#Block C
#10/17/2016
#
#This program contains the labs for all the chapters completed in class
#
#
#1-->1.5: Printing, maths, comments, assignment operators:
x = "hello"
y = "\"WORLD\""
print(x.upper() + " " + y.lower())

#Everything else:

#Initialising functions and class definitions below. Scroll to end for exec code
#main event loop
def mainPrompt():
    global mainInp
    mainInp = ""      
    while (not mainInp.isdigit()):
        mainInp = str(input("■ Perform basic arithmetics [1]\n■ Convert fahrenheit to celcius [2]\n■ Find the area of a trapezoid [3]\n■ Complete a quiz [4]\n\n"))

class MyMaths:# a class because, why not.

    #initialize the number variables
    def __init__(self, a, b):
        self.a, self.b = int(a), int(b)

    #START arithmetic operations START
    def add_(self):
        return self.a + self.b
    def subt(self):
        return self.a - self.b
    def mult(self):
        return self.a * self.b
    def divi(self):
        try:
            f = self.a / self.b
        except ZeroDivisionError:
            return "You can't divide by 0"
        else:
            return f
    def expo(self):
        return self.a ** self.b
    def mod_(self):
        try:
            f = self.a % self.b
        except ZeroDivisionError:
            return "You can't divide by 0"
        else:
            return f
    #END arithmetic operations END
    
    #Calculates the spacing for the display table. Offset for blank spaces is
    #added to the variables instead of being calculated here.
    def calculateSpacing(maxLVariable, arithName, arithFunc):
        return maxLVariable-(len(arithName)+len(str(arithFunc())))
        
        
#get 2 numbers from user
def getNumbers():
    inp, inp2 = "",""
    while(not inp.isdigit()):
        inp = str(input("\nPlease input a whole number: "))
    while(not inp2.isdigit()):
        inp2 = str(input("Please input another whole number: "))
    return(inp, inp2)

#Compares the 3 vars and returns longest one, function definition moved here for clarity
def getMaxLength(mult, divi, expo):
    return max(len("Multiplication:  " + str(mult)), len("Division:  " + str(divi)), len("Power/Exponent:  " + str(expo)))

#Checks if var is a float and returns result
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

#This handles the quiz option
def quizAsk(index, question, answer):
    quizAns = str(input("{}. {}".format(index, question)))
    if quizAns.lower() == answer:
        print("■ That's right!\n")
        return 1
    else:
        print("■ Not quite right\n")
        return 0
    
#ProgramExecution code:
while True:
    #loop the user prompt
    mainPrompt()

    #evaluate answers to user prompt

    #if arithmetic operations
    if mainInp == "1":
        h, k = getNumbers()
        foo = MyMaths(h, k)
        maxL  = getMaxLength(foo.mult(), foo.divi(), foo.expo())
        #Display results for arithmetic operations 
        maxL +=1 #+1 to offset
        separator="═"*maxL    
        print("\n╔", separator, "╗", sep="")
        print("║ Using {} and {}:".format(h, k), " " * (maxL -1- len(" Using "+str(h)+" and "+str(k)+": ")),"║")
        print("╠", separator, "╣", sep="")
        print("║ Addition: " , foo.add_()," "*(MyMaths.calculateSpacing(maxL, " Addition: ", foo.add_)),"║",sep="")
        print("║ Subtraction: " , foo.subt()," "*(MyMaths.calculateSpacing(maxL, " Subtraction: ", foo.subt)),"║",sep="")
        print("║ Multiplication: " , foo.mult()," "*(MyMaths.calculateSpacing(maxL, " Multiplication: ", foo.mult)),"║",sep="")
        print("║ Division: " , foo.divi()," "*(MyMaths.calculateSpacing(maxL, " Division: ", foo.divi)),"║",sep="")
        print("║ Power/Exponent: " , foo.expo()," "*(MyMaths.calculateSpacing(maxL, " Power/Exponent: ", foo.expo)),"║",sep="")
        print("║ Modulus: " , foo.mod_()," "*(MyMaths.calculateSpacing(maxL, " Modulus: ", foo.mod_)),"║",sep="")
        print("╚",separator,"╝","\n",sep="")
        continue

    #if convert to celcius
    elif mainInp == "2":
        inp = ""
        while(not isFloat(inp)):
            inp = str(input("\nPlease input your temperature: "))
        inp = (float(inp)-32)*(5/9)
        print("\n  ■ Your temperature in celcius: {0:.3f}°\n".format(inp), sep="")
        continue

    #if area of trapezoid
    elif mainInp =="3":
        inpTop, inpBot, inpHeight = "", "", ""
        
        while(not isFloat(inpTop)):
            inpTop = str(input("\nPlease input the length of the top base: "))
        
        while(not isFloat(inpBot)):
            inpBot = str(input("Please input the length of the bottom base: "))
        
        while(not isFloat(inpHeight)):
            inpHeight = str(input("Please input the height of the trapezoid: "))
        
        area = ((float(inpTop) + float(inpBot)) / 2) * float(inpHeight)
        print("\n  ■ It's a tarp! ", area, "\n")
        continue
    
    #if quiz
    elif mainInp =="4":
        quizScore = 0
        #quizQuestions & quizAnswers must be the same length
        #easily scalable data; example: we can import and update the "questions" and "answers" data from an external file without any code modifications
        quizQuestions = ["Solve: 18/2*7:\n",
                         "Who averaged one patent for every three weeks of his life? [type the number]:\n[1] Lars Magnus Ericsson\n[2] Nikolas Tesla\n[3] Charbel Najm\n[4] Thomas Edison\n",
                         "Name the world's largest ocean:\n",
                         "Complete the following: To be or not to ___\n[1] Flee\n[2] Be\n[3] Sleep\n[4] Seize the means of production\n",
                         "What is the square root of 3136?\n",
                         "What was the nickname of Mötorhead\'s late frontman?\n",
                         "Which fact about Charbel is true:\n[1] He sleeps 62 hours in a normal 24 hour day\n[2] He compresses his files by doing a flying round house kick to the harddrive\n[3] When he writes code with bugs, the bugs fix themselves\n[4] All of the above\n"]
        quizAnswers = ["63", "4", "pacific", "2", "56", "lemmy", "4"]
        
        print("\nQuiz:\n\n", end="", sep="")
        #iterate over each question and ask it
        for i in range(0,len(quizQuestions)):
            quizScore += quizAsk(i+1, quizQuestions[i], quizAnswers[i])
        
        print("You answered {score}/{coeff} questions correctly for a total percentage of {percent}%\n".format(score=quizScore, coeff=len(quizQuestions), percent=round((quizScore/len(quizQuestions)*100))))
        continue
        
        '''
        -------------------
        Inefficient Method:
        -------------------
        quizAns = int(input("1. Solve: (18/1)*7\n"))
        if quizAns == 126:
            quizScore += 1
            print("That's right!\n")
        else:
            print("That's wrong!\n")
            
        quizAns = int(input("1. Solve: (18/2)*7\n"))
        if quizAns == 63:
            quizScore += 1
            print("That's right!\n")
        else:
            print("That's wrong!\n")

        quizAns = int(input("1. Solve: (18/3)*7\n"))
        if quizAns == 42:
            quizScore += 1
            print("That's right!\n")
        else:
            print("That's wrong!\n")
        --------------------------------------------------
        '''


    
