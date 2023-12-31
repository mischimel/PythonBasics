"""
5. Word Frequency
Write a program that reads the contents of a text file.
The program should create a dictionary in which the keys are the individual words
found in the file and the values are the number of times each word appears.
For example, if the word “the” appears 128 times, the dictionary would contain an element with
'the' as the key and 128 as the value. The program should either display the frequency
of each word or create a second file containing a list of each word and its frequency.
"""
def main():

    file = open("sample.txt","r")

    # create a empty dictionary (dict = {word:occurences}
    unique_words = {}

    # loop through the file line by line
    for line in file:
        line = line.strip() # removes space and newline character
        line = line.lower() # convert all to lowercase
        words = line.split(" ") # split lines into words

        for word in words:
            if word in unique_words: # check if word is already in the dictionary
                unique_words[word] += 1 # if yes, increment count
            else:
                unique_words[word] = 1 # add word with count 1 (1st occurence)

    file.close()

    # print result
    print(unique_words)
    for word, count in unique_words.items():
        print(f"{word} : {count}")

if __name__ == '__main__':
    main()