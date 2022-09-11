# Benjamin Poag
# Tool for calculating one-term power derivatives

# Obtain user input term
userTerm = input('Please input a term to derive: ')

# Set booleans
tCycle = False
isX = False
frontC = False

# Find term length
tLen = len(userTerm)

# Set counter variables
c1 = 0

# Calculate derivative
while tCycle == False:
    if userTerm[c1] == 'x':
        if userTerm[c1+1] == '^':
            if tLen <= 3:
                newC = userTerm[2]
            else:
                newC = userTerm[c1+2:tLen]
            print(newC + 'x^' + str(int(newC)-1))
        else:
            print(str(1))
        tCycle = True
    elif 'x' not in userTerm:
        print(str(0))
        tCycle = True
    elif '^' not in userTerm:
        xPos = userTerm.find('x')
        print(userTerm[0:xPos])
        tCycle = True
    else:
        while isX == False:
            if userTerm[c1] == 'x':
                if userTerm[c1+1] == '^':
                    if tLen <= 3:
                        newC = userTerm[2]
                    else:
                        newC = userTerm[c1+2:tLen]
                print(str(int(newC)*int(coeff)) + 'x^' + str(int(newC)-1))
                isX = True
                tCycle = True
            else:
                while frontC == False:
                    if userTerm[c1] == 'x':
                        frontC = True
                    else:
                        coeff = userTerm[0:c1+1]
                        c1 += 1
