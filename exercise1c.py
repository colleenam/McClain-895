#Colleen McClain 1-21-15
#Advanced Option

list1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
testval=8

#get the midpoint of list1
length=len(list1)
print length

#if an odd number of elements, the midpoint will be retrieved by moving one extra step backwards;
midposition=(length/2+1)

print midposition

#return the midpoint value 
print(list1[-(midposition)])

#convert to a string for later
str_midpos=str(midposition)

test1=(list1[-(midposition)])
print test1

#either return the position, or subset a new list
if testval==testval:
	print("Found at "+str_midpos)
elif testval<test1:
	list2=list1[length/2:]
elif testval>test1:
	list2=list1[:midposition]

print list2