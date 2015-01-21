
#Colleen McClain 1-21-15
#Less Easy Option
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
