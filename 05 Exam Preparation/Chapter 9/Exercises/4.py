"""
4. Unique Words
Write a program that opens a specified text file then displays a list of all the unique words found in the file.
Hint: Store each word as an element of a set
"""
def main():

    userinput = input("enter name of file? ")

    file = open(userinput,"r")
    text = file.read()

    # Remove punctuation
    all_punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for element in text:
        if element in all_punct:
            text = text.replace(element, "")

    words = text.split() # get all the words and make them lowercase
    words = [word.lower() for word in words]

    # create set of unique words
    unique_words = set(words)
    unique_words = sorted(unique_words)

    file.close()

    # print result
    print(unique_words)
    for word in unique_words:
        print(word)

if __name__ == '__main__':
    main()