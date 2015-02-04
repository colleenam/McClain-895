#Exercise 4
#Colleen A. McClain
# 2-4-15

#Implementation goals:
#Count and output the total number of lines, words, and characters in this specific Romeo and Juliet file
#Make a dictionary that maps words to word counts
#Loop over the dictionary once it is built to output each word that appears in the text and its word count

#romeo and juliet file name: pg1513.txt
#test file also used throughout code development (final text at end of file): testfile.txt
#located at /Users/Colleen/Documents/Code/McClain-895/Exercises

#open the file
rawfile = open("pg1513.txt","r")

#alternatively, try the test file
#rawfile= open("testfile.txt","r")

#initialize each variable to zero
lines=0;
characters=0;
words=0;
words_clean=0;

#create the null dictionary
wordcount_clean={}

#START WORDCOUNT LOOP
for current_line in rawfile:

    #for each line, increment counter by 1
    lines +=1;
    
    #get the length of the line (number of characters) and add it to the running total
    #include punctuation in the character count
    char_line=len(current_line)
    characters +=char_line

    #remove all punctuation for word count
    #from http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
    #info on string functions at https://docs.python.org/2/library/string.html
 
    #pass a null translation table in to remove (not translate) all punctuation
    #since str.punctuation doesn't work, use the punctuation from the source code at https://hg.python.org/cpython/file/2.7/Lib/string.py)
    #but first, replace "--" and "}" with a space because they often denote two separate words (not separated by spaces) in the file

    clean_line1=current_line.replace("--"," ")
    clean_line2=clean_line1.replace("}"," ")

    #also get rid of differences in uppercase/lowercase that will affect word count; for example "o" and "O" are not counted as same word without this change
    clean_line3=clean_line2.lower()

    #punctuation taken from source code above
    clean_line=clean_line3.translate(None, """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")

    #split each line into words, with punctuation included 
    #words_line=current_line.split()

    #split each line into words, with punctuation excluded 
    words_clean_line=clean_line.split()

    #some checks
    #print(words_line)
    #print(words_clean_line)

    #take the length of the list to get the count of words, then add that number to the running total
    #words += len(words_line)
    words_clean += len(words_clean_line)

    #use the cleaned words to build the dictionary
    #increment the wordcount when each is found

    #START DICTIONARY LOOP

    for word in words_clean_line:
        if (word in wordcount_clean):
            wordcount_clean[word] +=1;
        if (word not in wordcount_clean):
            wordcount_clean[word] = 1;

    #END DICTIONARY LOOP

    #some checks
    #print(len(words_clean_line))

#END WORD COUNT LOOP

print("There are "+str(lines)+" lines in the file")
print("There are "+str(characters)+" characters in the file")
#print("There are " +str(words)+" words in the file")
print("There are " +str(words_clean)+" words (cleaned for case and punctuation) in the file - used in dictionary")

print("Word counts, using words cleaned for case and punctuation")
# loop through dictionary and print out each word name and count
for name, count in wordcount_clean.items():
    print("word = \"" + str(name) + "\"; count in text = "+ str(count))




#final text from test file, to test out punctuation removal and word counting
#This is a test file
#
#I want to see what will happen with blank lines. and a hyphenated-word test
#
#Thanks test test!!!


