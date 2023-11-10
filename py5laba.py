1.
a = input("Enter a string: ")
lowercase = a.lower()
word = lowercase.split()
word = a.replace(" ", "")
tuple = tuple(word)
print("Tuple: ", tuple)
2.
from collections import Counter

def count_symbols_frequency(symbol_list):
    symbol_count = Counter(symbol_list)
    frequency_list = list(symbol_count.items())
    return frequency_list

user_input = input("Enter a string: ")
lowercase_input = user_input.lower()
symbol_list = list(lowercase_input)

frequency_result = count_symbols_frequency(symbol_list)

for symbol, count in frequency_result:
    print(f"{symbol},{count}")
3.
def categorize_symbols(symbol_list):
    list_vow = []
    list_cons = []
    list_symb = []

    for symbol in symbol_list:
        if symbol.isalpha():
            if symbol in 'aeiouy':
                list_vow.append(symbol)
            else:
                list_cons.append(symbol)
        else:
            list_symb.append(symbol)

    return list_vow, list_cons, list_symb

user_input = input("Enter a string: ")
lowercase_input = user_input.lower()
symbol_list = list(lowercase_input)

list_vow, list_cons, list_symb = categorize_symbols(symbol_list)

print("Vowels:", list_vow)
print("Consonants:", list_cons)
print("Symbols:", list_symb)
4.
def divide_into_quartiles(list_A):
    sorted_list = sorted(list_A)
    length = len(sorted_list)

    q1 = sorted_list[:length // 4]
    q2 = sorted_list[length // 4: 2 * length // 4]
    q3 = sorted_list[2 * length // 4: 3 * length // 4]
    q4 = sorted_list[3 * length // 4:]

    if length % 4 == 1:
        q1.append(0)

    return q1, q2, q3, q4

list_A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
q1, q2, q3, q4 = divide_into_quartiles(list_A)

print("Original List:", list_A)
print("Quartile 1 (Q1):", q1)
print("Quartile 2 (Q2):", q2)
print("Quartile 3 (Q3):", q3)
print("Quartile 4 (Q4):", q4)
5.
def create_student_dictionary(name, assignments_scores, labs_scores, tests_scores):
    student_dict = {
        'Name': name,
        'Assignments': assignments_scores,
        'Labs': labs_scores,
        'Tests': tests_scores
    }
    return student_dict

student_name = input("name: ")
assignments_scores = [float(x) for x in input("scores for assignments: ").split(',')]
labs_scores = [float(x) for x in input("Labs: ").split(',')]
tests_scores = [float(x) for x in input("tests: ").split(',')]

student_info = create_student_dictionary(student_name, assignments_scores, labs_scores, tests_scores)

print("Student Information:")
for key, value in student_info.items():
    print(f"{key}: {value}")
