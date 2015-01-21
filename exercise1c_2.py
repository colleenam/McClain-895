#Colleen McClain 1-21-15
#Advanced Option
#iterative implementation

#define the function

def itsearch(x, uselist):
	left = 0;
	right = len(uselist)-1;
	while left <= right:
		mid = (left + right)/2;
		if (uselist[mid] == x):
			return mid
		elif (uselist[mid] > x): 
			right = mid - 1
		elif (uselist[mid] < x):
			left = mid + 1

#search for numbers in several lists
print("Found at position "+str(itsearch(55,[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])))

print("Found at position "+str(itsearch(3,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))

print("Found at position "+str(itsearch(4,[0, 1, 1, 2, 3, 5, 9, 13, 21, 34, 42, 89, 144])))
