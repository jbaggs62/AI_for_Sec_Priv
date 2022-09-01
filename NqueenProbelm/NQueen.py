import time # import time module
import sys #import sys module

## define boundingFN function
def boundingFN(colsDone, configuration):
    xDelta = 0
    yDelta = 0
    #compare = 0
    #print("This is configuration ", configuration)
    for col in range(1,(colsDone)):
        for compare in range((col+1),colsDone+1):
            if configuration[col] == configuration[compare]:
                return False
            xDelta = (compare - col)
            yDelta = abs(configuration[compare]-configuration[col])
            if (xDelta==yDelta):
                return False
    return True # if we get here we haven't found any clashes

## define solutionShow function
def solutionShow(configuration):
    print(configuration[1:side_length+1], " Solution")
   # print('\n')

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
#side_length = input("Enter a number: ")

# Converts the string into an integer
#side_length = int(side_length)


# Get input from the command line
if (len(sys.argv) > 1):
  side_length = int(sys.argv[1])
else:
  print("Usage: python NQueen.py n")
  print("   where n is the side length of the chessboard")
  sys.exit(0) #terminate program

#start_time
start_time = time.time()

# actual work being done
configuration = [0] * (side_length+1)
colsDone = 0 # no colsDone yet, just starting

NQbacktrack (colsDone, configuration) # recursive function finds all solutions for NQueen problem of side_length n
print('--- elapsed time = %3.8f milliseconds ---' % ((time.time() - start_time)*1000))
