import random
import sys

try:
    import pyperclip
except ImportError:
    print("\npyperclip is not installed, output will not auto copy to clipboard!\n\n")


# ADD ARRAYS HERE
special_array = ["!", "@", "#", "$", "%", "^", "&", "*",
                 "(", ")", "-", "_", "=", "+", "[", "{", "]", "}", "\\", "|", ";", ":", "'", '"', "<", ",", ">", ".", "/", "?", "`", "~"]

number_array = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# set amount of words to be generated
amount_of_words = 1000

# set array to which ever array u want to use
array = special_array


def wordFormatter(random_word, function_count):

    # splitting the base word randomly
    random_splice = random.randrange(len(random_word))

    # making splices from random_splice and inserting a random char from array
    combined_word = random_word[0:random_splice] + random.choice(
        array) + random_word[random_splice:len(random_word)-1]

    # recursing function if function_count greater than 1
    if function_count > 1:
        function_count -= 1
        return wordFormatter(combined_word, function_count)
    else:
        return combined_word


with open("wordlist.txt", "r") as file:

    # mapping each word in file to a list
    words_in_file = list(map(str, file.readlines()))

    completed_paragraph = str("")
    for word in range(amount_of_words-1):

        # picks a random word from words_in_file list
        random_word = random.choice(words_in_file).lower()

        # some extra variation of how many times characters get mixed into the word
        match random.randrange(2, 4):
            case 2:
                final_word = wordFormatter(random_word, 2)
            case 3:
                final_word = wordFormatter(random_word, 3)

        completed_paragraph += final_word + " "

    print(completed_paragraph)
    if "pyperclip" in sys.modules:
        pyperclip.copy(completed_paragraph)
