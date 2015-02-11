#Colleen McClain 2-11-15
#Exercise 2 Final V2
#Edits for Exercise 5

#Easy Option

# Python program to find the
# H.C.F of two input number

#print the name of the task
print ("Exercise 2 - Easy")

# define a function to print the highest common factor of x and y
def hcf( x, y ):

    """This function takes two
    integers and returns the H.C.F"""

    # identify which of two numbers is smaller
    if x > y:
    
        smaller = y
    
    else:
    
        smaller = x

    #-- END check to find smaller number --#

    # loop over integers from 1 to the smaller number.
    for i in range( 1, smaller + 1 ):

        # for each integer up to the smaller number, divide into both x and y 
        # Goal: to see if there's a remainder
        # % = modulo operator - remainder part of a division)
        if ( ( x % i == 0 ) and ( y % i == 0 ) ):

            # if the condition above is true, this is a common factor.  
            # Store it, but also continue looping,
            # in case there is a greater one.
            # Store result of last (greatest) common factor found in hcf
            hcf = i

        #-- END check to see if HCF --#

    #-- END loop over integers from 1 to smaller of the two numbers --#

    return hcf

#-- END function hcf() --#

# take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

# enter numbers of interest, then print the HCF returned by the function
num1 = 36
num2 = 18

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

# try another set of numbers
num1 = 125
num2 = 50

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

# and another set of numbers
num1 = 125
num2 = 45

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

#test to see what happened when 0 was included
#num1 = 125
#num2 = 0

# print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )



# Colleen McClain 2-11-15
# Less Easy Option V2

# print the name of the exercise
print ("\nExercise 2 - Less Easy")

# define a list of numbers
some_numbers = [1,2,4,6,8,10]
# print the list
print [some_numbers]

# initialize variables
sum1 = 0;
count1 = 0;

# compute the running sum of elements in some_numbers 
# and count how many there are
for element in some_numbers:
    sum1 = sum1 + element
    count1 = count1 + 1
# end loop through some_numbers

# compute the average of some_numbers
# use float to avoid truncation
average = sum1 / float(count1)

# print the average
# create a string first 
str_average = str(average)
print "The mean of the list is " + str_average

#another way
#couldn't you also do this?
#sum2=sum(numberstry)
#count2=len(numberstry)
#avg2=sum2/float(count2)

#print the average
#print avg2



# Colleen McClain 2-11-15
# Advanced Option V2
# iterative implementation

# print the name of the exercise
print ("\nExercise 2 - Advanced, Iterative Version")

# define the function based on the existing php code
# itsearch is the iterative  implementation

def itsearch(x, some_list):
    # establish left boundary
    left = 0;
    # establish right boundary - number of elements in list - 1
    right = len(some_list) - 1;
    # loop until the boundaries meet
    while left <= right:
        # find the midpoint of the current slice of the list
        mid = (left + right) / 2;
        # check it against the value of x
        if (some_list[mid] == x):
            # if it matches, you've found the number in the list
            return mid
        # otherwise, use the midpoint to create the upper or lower bound of a new slice
        elif (some_list[mid] > x): 
            right = mid - 1
        elif (some_list[mid] < x):
            left = mid + 1

# call function 
# search for numbers in several lists

print("Found at position "+str(itsearch(55,[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])))

print("Found at position "+str(itsearch(3,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))

#last one should be not found

print("Found at position "+str(itsearch(4,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))
