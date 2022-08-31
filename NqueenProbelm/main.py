## define boundingFN function
def boundingFN(colsDone, configuration):
    xDelta = 0
    yDelta = 0
    #compare = 0
    print("This is configuration ", configuration)
    for col in range(1,colsDone-1):
        for compare in range(col+1,colsDone):
        #for compare in range(colsDone):
            if configuration[col] == configuration[compare]:
                return False
        xDelta = (compare - col)
        yDelta = abs(configuration[compare]-configuration[col])
        if (xDelta==yDelta):
            return False
    return True
# import time module
import time

## define boundingFN function
def boundingFN(colsDone, configuration):
    xDelta = 0
    yDelta = 0
    compare = 0
    #print("This is configuration ", configuration)
    for col in range(1,(colsDone-1)):
        for compare in range((col+1),colsDone):
        #for compare in range(colsDone):
            if configuration[col] == configuration[compare]:
                return False
            xDelta = (compare - col)
            yDelta = abs(configuration[compare]-configuration[col])
            if (xDelta==yDelta):
                return False
    return True

## define solutionShow function
## define solutionShow function
def solutionShow(configuration):
    print(configuration[1:side_length+1], " Solution")
    print('\n')

## define NQbacktrack  function ##

def NQbacktrack(colsDone, configuration):
    if colsDone == side_length:
        solutionShow(configuration)
    else:
        colsDone = colsDone + 1
        for row in range(1,side_length+1):
            configuration[colsDone] = row
            if boundingFN(colsDone,configuration)==True:
                NQbacktrack(colsDone, configuration)


# an input is requested and stored in a variable
side_length = input("Enter a number: ")

# Converts the string into an integer
side_length = int(side_length)

# Print in the console the variable requested if the value of side_length is not correct
if (side_length<=0):
    print("Usage: java nQueen n")
    print(f"where n is the side length of the chessboard ")

#start_time
start_time = time.time()

# actual work being done
configuration = [0] * (side_length+1)
colsDone = 0

NQbacktrack (colsDone, configuration)
print('--- %3.8f miliseconds ---' % ((time.time() - start_time)*1000))