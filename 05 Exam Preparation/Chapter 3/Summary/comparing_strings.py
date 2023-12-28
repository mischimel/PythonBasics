# Comparing Strings

# Example of comparing strings

# Case-sensitive string comparison using ==
string1 = "apple"
string2 = "Apple"

if string1 == string2:
    print(f"The strings '{string1}' and '{string2}' are equal.")
else:
    print(f"The strings '{string1}' and '{string2}' are not equal.")

# Case-sensitive string comparison using !=

if string1 != string2:
    print(f"The strings '{string1}' and '{string2}' are not equal.")
else:
    print(f"The strings '{string1}' and '{string2}' are equal.")

# String comparison using >, <, >=, and <=
word1 = "apple"
word2 = "banana"

if word1 < word2:
    print(f"'{word1}' comes before '{word2}' in dictionary order.")
elif word1 > word2:
    print(f"'{word1}' comes after '{word2}' in dictionary order.")
else:
    print(f"The words '{word1}' and '{word2}' are the same.")

# Comparing strings of different lengths
short_word = "cat"
long_word = "caterpillar"

if short_word < long_word:
    print(f"'{short_word}' comes before '{long_word}' in dictionary order.")
elif short_word > long_word:
    print(f"'{short_word}' comes after '{long_word}' in dictionary order.")
else:
    print(f"The words '{short_word}' and '{long_word}' are the same.")
