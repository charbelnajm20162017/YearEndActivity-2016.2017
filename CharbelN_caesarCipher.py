## C. Najm 
## Block C

import sys
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
         '1', '2', '3', '4', '5','6', '7', '8', '9', '0', ' ']
out = []
x = set([]) ## We use a set to prevent duplicates

## We need these 2 files to build a wordlist to use in brute forcing.
## Any words used in option 1 (encrypt) or 2 (decrypt) will be added
## to this list.

## The wordlist is populated from scratch to keep it realistically sized.

def writeWords():
    with open("learnedWords.txt", "a") as words:
        for w in m1.lower().split():
            x.add(w)
        for i in x:
            words.write(i + "\n")

def loadWords():
    try:
        with open("learnedWords.txt") as words:
            for w in words.readlines():
                x.add(w.strip("\n"))
            return list(x)
    except FileNotFoundError:
        writeWords()
        loadWords()

def encrypt():
    out = []
    writeWords()
    for l in m1.lower().strip():
        encShift = alpha.index(l)+int(m)
        out.append(alpha[encShift%len(alpha)].upper())
    return out

def decrypt(key):
    out = []
    for l in m1.lower().strip():
        encShift = alpha.index(l)+(len(alpha)-int(key))
        out.append(alpha[encShift%len(alpha)].upper())
    return out

def brute():
    x = loadWords()
    matches = []

    ## Just like above except this uses all keys in range 0 to length of the char list
    
    for a in range(0,len(alpha)):
        for l in m1.lower().strip():    
            encShift = alpha.index(l)+(len(alpha)-int(a))
            out.append(alpha[encShift%len(alpha)].lower())   
    
    for word in x:

        ## Search the word list for any match(es) and find its(their) key(s)
        
        if word in "".join(out).replace(" ",""):
            key = "".join(out).find(word)
            matches.append("FOUND MATCH @ KEY "+ str(int(key/len(m1))) + ":" + word)
    print(*decrypt(str(int(key/len(m1)))), sep="")
    return matches 


## Main Program Loop

while True:

    out = []
    x = set([])    
    
    start = input("\n[1]Encrypt\n[2]Decrypt\n[3]BruteForce\n")
    if not start.isdigit() or int(start) > 3:
        continue
    try:
        
        ##Added this "try" error-catching to prevent errors from interupting
        ##the main program loop.
        
        if start == "1" or start == "2":
            m = input("KEY?")
        m1 = input("MSG?")
        if start == "1":
            print(*encrypt(),sep="")
        elif start == "2":
            print(*decrypt(m),sep="")
        elif start == "3":
            print(*brute(),sep="\n")
            
    except UnboundLocalError:
        print("No match was found: \nPlease populate the wordlist by using option 1 to ecrypt your message first then paste the encrypted string into the bruteforcer again.")
    except:
        print("Something unexpected happened, please restrict your inputs to alphanumeric characters and whitespace only. Error Caught: ", sys.exc_info()[0])