#!/usr/bin/env python
import sys

# PROBLEM STATEMENT: WRITE LINUX PROGRAM THAT TAKES GIVEN NAME AND RETURNS SOUNDEX
# APPROACH: TACKLE EACH WORD OF GIVEN NAME ONE BY ONE, FOR READABILITY AND ABSTRACTION

# This first block of code creates a dictionary for storing letter/number pairs for Soundex
# Step 1: create key and value pairs
letters = list("BFPVCGJKQSXZDTLMNR")
replacements = ["1"]*4+["2"]*8+["3"]*2+["4"]+["5"]*2+["6"]
after_first_letter_dict = {}
# Step 2: create the dictionary
for letter, replacement in zip(letters,replacements):
    after_first_letter_dict[letter] = replacement


def word_to_soundex(word):
# This function takes input names and returs in Soundex form
    # Step 0: Keep some details about the word that will be used later
    first_letter = word[0].upper() # keep first letter of word and the number form
    first_letter_number = ""
    if first_letter in after_first_letter_dict:
        first_letter_number = after_first_letter_dict[first_letter]
    new_word = list(word.upper()) # transform word into a list to be manipulated in this function
    previous_letter = first_letter_number # we use this to see if the next letter is the same as previous
    new_word = [letter for letter in new_word[1:] if letter not in list('HW')] # remove all hw after first letter
    # Step 1: Initial Loop through manipulation
    for i in range(0, len(new_word)): # loop through each character in the word
        # Change all vowels to '0' to work with conditionals later
        if new_word[i] in list('AEIOUY'):
            new_word[i] = '0' # change all vowels and hw into 0
        # Change each non-vowel into digit based on dictionary
        elif new_word[i] in after_first_letter_dict:
            new_word[i] = after_first_letter_dict[new_word[i]]
        # If the current letter is the same as the one before then make it a hashtag (we remove later)
        if previous_letter == new_word[i]:
            new_word[i] = "#"
        # Otherwise, we need a new "previous letter"
        else:
            previous_letter = new_word[i]

    # Step 2: Remove all vowel placeholders and duplicates! (0 and #)
    new_word[:] = [first_letter] + [letter for letter in new_word if letter not in list('0#')]
    # Step 3: Shorten or increase in length if needed
    new_word = new_word[0:4] + ["0"] * (4 - len(new_word))
    # Step 4: Make into string and return
    return ''.join(new_word)

def main(argv):
# This main function is responsible for turning each argument (word of name)
# provided into the soundex form and printing each.
    for i in range(1, len(argv)):
        # This loop goes through each word in the name and convert it to soundex
        sys.stdout.write(word_to_soundex(argv[i]))
        # If it is the last word, do new line. Otherwise, space in between.
        if i != len(argv) -1:
            sys.stdout.write(" ")
        else:
            sys.stdout.write("\n")

if __name__ == '__main__':
    main(sys.argv)

# BELOW THIS LINE USED FOR MY OWN TESTING
# ---------------------------------------

# import unittest

# class TestWords(unittest.TestCase):
#     def test(self):
#         self.assertEqual(word_to_soundex("ddfggggggd"), "D123")
#         self.assertEqual(word_to_soundex("James"), "J520")
#         self.assertEqual(word_to_soundex("Tiberius"), "T162")
#         self.assertEqual(word_to_soundex("Kirk"), "K620")
#         self.assertEqual(word_to_soundex("addfggggggd"), "A312")
#         self.assertEqual(word_to_soundex("rrfdhsj"), "R132")
#         self.assertEqual(word_to_soundex("Rafi"), "R100")
#         self.assertEqual(word_to_soundex("Khaled"), "K430")
#         self.assertEqual(word_to_soundex("Brightgate"), "B623")
#         self.assertEqual(word_to_soundex("Fiona"), "F500")
#         self.assertEqual(word_to_soundex("Artiaga"), "A632")
#         self.assertEqual(word_to_soundex("aaaaaaaaaaaaaaaaaa"), "A000")
#         self.assertEqual(word_to_soundex("daaaaaaaaasssdsfds"), "D232")
#         self.assertEqual(word_to_soundex("hwhfwhejfhj"), "H121")
#         self.assertEqual(word_to_soundex("abc"), "A120")
#         self.assertEqual(word_to_soundex("ac"), "A200")
#         self.assertEqual(word_to_soundex("a"), "A000")
#         self.assertEqual(word_to_soundex("aaaaac"), "A200")


# if __name__ == '__main__':
#     main()
#     sys.argv[1:] = []
#     unittest.main()
    

