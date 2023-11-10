1.
def read_and_display_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
read_and_display_text_file(file_path)
2.
import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                print(f"The file {file_path} is empty.")
            else:
                random_line = random.choice(lines)
                print("Random Line:", random_line.strip())
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
read_random_line(file_path)
3.
def count_uppercase_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            return uppercase_count
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
uppercase_count = count_uppercase_characters(file_path)

if uppercase_count is not None:
    print(f"Number of Uppercase Characters: {uppercase_count}")
4.
def count_lines_not_starting_with_D(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lines_not_starting_with_D = [line for line in lines if not line.strip().startswith('D')]
            count = len(lines_not_starting_with_D)
            return count
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
line_count = count_lines_not_starting_with_D(file_path)

if line_count is not None:
    print(f"Number of lines not starting with 'D': {line_count}")
5.
def count_words_ending_with_F(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            words_ending_with_F = [word for word in words if word.endswith('F') or word.endswith('f')]
            count = len(words_ending_with_F)
            return count
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
word_count = count_words_ending_with_F(file_path)

if word_count is not None:
    print(f"Number of words ending with 'F': {word_count}")

6.
def count_all_and_none_words(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            
            count_all = words.count("all") + words.count("All")
            count_none = words.count("none") + words.count("None")
            
            return count_all, count_none
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
count_all, count_none = count_all_and_none_words(file_path)

if count_all is not None and count_none is not None:
    print(f"Number of 'all' words: {count_all}")
    print(f"Number of 'none' words: {count_none}")

7.
from collections import Counter
import string

def count_word_frequency(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            translator = str.maketrans("", "", string.punctuation)
            content = content.translate(translator)
            words = content.split()

            word_frequency = Counter(words)
            return word_frequency
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
word_frequency = count_word_frequency(file_path)

if word_frequency is not None:
    print("Word Frequency:")
    for word, count in word_frequency.items():
        print(f"{word}: {count}")
8.
import string

def find_longest_word(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read().lower()
            translator = str.maketrans("", "", string.punctuation)
            content = content.translate(translator)
            words = content.split()

            longest_word = max(words, key=len)
            return longest_word
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
longest_word = find_longest_word(file_path)

if longest_word is not None:
    print(f"The longest word in the file is: {longest_word}")
9.
def replace_and_display(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            corrected_content = content.replace('B', 'J')
            print(corrected_content)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
replace_and_display(file_path)
10.
def count_occurrences_A_and_B(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            count_A = content.lower().count('a')
            count_B = content.lower().count('b')

            print(f"Occurrences of 'A' and 'a': {count_A}")
            print(f"Occurrences of 'B' and 'b': {count_B}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = "text1.txt"
count_occurrences_A_and_B(file_path)
