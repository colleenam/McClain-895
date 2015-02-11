# Exercise 4 V2
# Colleen A. McClain
# 2-11-15

print("Exercise 4")

# Implementation goals:
# Count and output the total number of lines, words, and characters 
# Implement for  this specific Romeo and Juliet file
# Make a dictionary that maps words to word counts
# Loop over the dictionary once it is built 
# Output each word that appears in the text and its word count

# romeo and juliet file name: pg1513.txt
# test file also used throughout code development: testfile.txt
# both located at /Users/Colleen/Documents/Code/McClain-895/Exercises

# Create a function that counts lines, characters, and words in text file

def text_counts (rawfile):

    '''

    This function reads in a text file and outputs the total number of lines,
    words, cleaned words (stripped of case and punctuation), and a dictionary
    containing word counts for unique cleaned words in the file.  To do so, it 
    loops over lines and then over words within a line.  In printing the results,
    it loops over the dictionary entries to print each word together with its 
    count.

    Before running this function on a new text file, consider how words should be 
    cleaned of punctuation; for example, "--" and "}" are  considered to separate
    two unique words in the Romeo and Juliet file after a review of its structure.

    Note: 
    Line count includes blank lines
    Character count includes spaces on lines that have at least one word
    Word count (overall and by word) is run on words cleaned for case and punctuation
    Commented code includes the same analysis run on raw (non-cleaned) words

    '''

    # initialize each variable to zero
    lines = 0;
    characters = 0;
    words = 0;
    words_clean = 0;

    # create the null dictionary
    wordcount_clean = {}

    # START WORDCOUNT LOOP
    for current_line in rawfile:

        # for each line, increment counter by 1
        lines += 1;
    
        # get the length of the line (number of characters)
        # add it to the running total
        # include punctuation in the character count
        char_line = len(current_line)
        characters += char_line

        # remove all punctuation for word count
        # http://stackoverflow.com/questions/265960/
        # best-way-to-strip-punctuation-from-a-string-in-python
        # info on functions at https://docs.python.org/2/library/string.html
 
        # pass a null translation table in to remove (not translate) all punctuation
        # since str.punctuation doesn't work, insert punctuation string
        # source code is at https://hg.python.org/cpython/file/2.7/Lib/string.py
        
        # first, replace "--" and "}" with a space 
        # they often denote two separate words (not separated by spaces) in the file
        clean_line1 = current_line.replace("--"," ")
        clean_line2 = clean_line1.replace("}"," ")

        # also, get rid of differences in uppercase/lowercase that will affect word count
        # for example, "o" and "O" are not counted as same word without this change
        clean_line3 = clean_line2.lower()

        # punctuation taken from source code above
        clean_line = clean_line3.translate(None, """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")

        # split each line into words, with punctuation included 
        # words_line=current_line.split()

        # split each line into words, with punctuation excluded 
        words_clean_line = clean_line.split()

        # some checks

        # print(words_line)
        # print(words_clean_line)

        # take the length of the list to get the count of words
        # then add that number to the running total
    
        # count words, punctuation included
        # words += len(words_line)

        # count words, punctuation excluded
        words_clean += len(words_clean_line)

        # use the cleaned words to build the dictionary
        # increment the wordcount when each is found

        # START DICTIONARY LOOP
    
        # loop through each word in the line
        for word in words_clean_line:

            # if the word is already there, increment its count by 1
            if (word in wordcount_clean):
                wordcount_clean[word] += 1;
            # if the word is not already there, initialize its count to 1
            if (word not in wordcount_clean):
                wordcount_clean[word] = 1;

        # END DICTIONARY LOOP

        # some checks
    
        # print(len(words_clean_line))

    # END WORD COUNT LOOP

    # Print the results
    print("\nThere are " + str(lines) + " lines in the file")
    print("There are " + str(characters) + " characters in the file")
    #print("There are " +str(words)+" words in the file")
    print("There are " + str(words_clean) + " words (cleaned for case and punctuation) in the file")

    print("Word counts, using words cleaned for case and punctuation")

    # loop through dictionary and print out each word name and count
    for name, count in wordcount_clean.items():
        print("word = \"" + str(name) + "\"; count in text = "+ str(count))



# call the function using the romeo and juliet file
text_counts(open("pg1513.txt","r"))

# alternatively, call using the text file
# text_counts(open("testfile.txt","r"))




#final text from test file, to test out punctuation removal and word counting
#This is a test file
#
#I want to see what will happen with blank lines. and a hyphenated-word test
#
#Thanks test test!!!


