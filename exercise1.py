#Colleen McClain 1-21-15
#Exercise 1 

#Easy Option

# Python program to find the
# H.C.F of two input number

# define a function
print ("Exercise 1 - Easy")

def hcf( x, y ):

    """This function takes two
    integers and returns the H.C.F"""

    # choose the smaller number
    if x > y:
    
        smaller = y
    
    else:
    
        smaller = x

    #-- END check to find smaller number --#

    # loop over integers from 1 to the smaller number.
    for i in range( 1, smaller + 1 ):

        # see if each divided by the other results in no remainder (% = modulo operator - remainder part of a division)
        if ( ( x % i == 0 ) and ( y % i == 0 ) ):

            # this is a common factor.  Store it, but also keep looking,
            #    in case there is a greater one.
            hcf = i

        #-- END check to see if HCF --#

    #-- END loop over integers from 1 to smaller of the two numbers --#

    return hcf

#-- END function hcf() --#

# take input from the user
#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))

# OR just enter the numbers you want here
num1 = 36
num2 = 18

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

num1 = 125
num2 = 50

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

num1 = 125
num2 = 45

print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )

#num1 = 125
#num2 = 0

#print( "The H.C.F. of " + str( num1 ) + " and " + str( num2 ) + " is " + str( hcf( num1, num2 ) ) )



#Colleen McClain 1-21-15
#Less Easy Option

print ("Exercise 1 - Less Easy")

numberstry = [1,2,4,6,8,10]
#print the list
print [numberstry]

#initialize variables
sum1=0;
count1=0;

#compute the running sum and count
for element in numberstry:
    sum1=sum1+element
    count1=count1+1

#compute the average
average=sum1/float(count1)

#print the average
#create a string first 
str_average=str(average)
print "The mean of the list is "+str_average

#another way
#couldn't you also do this?
#sum2=sum(numberstry)
#count2=len(numberstry)
#avg2=sum2/float(count2)

#print the average
#print avg2



#Colleen McClain 1-21-15
#Advanced Option
#iterative implementation

#first tried to recreate the code entirely from the description, which was causing me too many problems (this is the reference to 'exercise1c' vs 'exercise1c_2' in the log)

print ("Exercise 1 - Advanced, Iterative Version")

#define the function based on the existing php code

def itsearch(x, uselist):
    left = 0;
    right = len(uselist)-1;
    while left <= right:
        #find the midpoint
        mid = (left + right)/2;
        #check it against the value of x
        if (uselist[mid] == x):
            #if it matches, this is the found position
            return mid
        #otherwise, use the midpoint to create the upper or lower bound of a new interval
        elif (uselist[mid] > x): 
            right = mid - 1
        elif (uselist[mid] < x):
            left = mid + 1

#search for numbers in several lists
print("Found at position "+str(itsearch(55,[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])))

print("Found at position "+str(itsearch(3,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))
#last one should be not found
print("Found at position "+str(itsearch(4,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))
