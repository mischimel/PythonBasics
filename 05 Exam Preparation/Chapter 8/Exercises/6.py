"""
6. Average Number of Words
If you have downloaded the source code from the Computer Science Portal you
will find a file named text.txt in the Chapter 08 folder. The text that is in the file is stored
as one sentence per line. Write a program that reads the file’s contents
and calculates the average number of words per sentence.
"""
def main():
    file = open("text.txt", "r")

    # create a list with all the sentences each as seperate element
    sentences = file.readlines()

    # get the number of sentences
    sentences_num = len(sentences)

    # get the total number of words (create sublist words, and add length to total)
    total_words = 0
    for item in sentences:
        words = item.split()
        total_words += len(words)

    # calculate average
    average = total_words / sentences_num

    print(average)

if __name__ == '__main__':
    main()