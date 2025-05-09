# Create a list of squares from 0 to 4 using list comprehension
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]

# Convert a list of uppercase words to lowercase
words = ["HELLO", "WORLD", "PYTHON"]
lowercase_words = [word.lower() for word in words]
print(lowercase_words)  # Output: ['hello', 'world', 'python']

# Multiply each number from 1 to 5 by 10
tens = [x * 10 for x in range(1, 6)]
print(tens)  # Output: [10, 20, 30, 40, 50]

# Extract the first letter from each word
words = ["apple", "banana", "cherry"]
first_letters = [word[0] for word in words]
print(first_letters)  # Output: ['a', 'b', 'c']

# Flatten a nested list into a single list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # Output: [1, 2, 3, 4, 5, 6]

# Get the length of each word
words = ["hello", "world", "python", "rocks"]
lengths = [len(word) for word in words]
print(lengths)  # Output: [5, 5, 6, 5]

# Replace vowels in a word with '*'
word = "education"
vowels = "aeiou"
replaced = ['*' if char in vowels else char for char in word]
print("".join(replaced))  # Output: '*d*c*t**n'

# Square only the odd numbers from 0 to 9
squares_of_odds = [x**2 for x in range(10) if x % 2 != 0]
print(squares_of_odds)  # Output: [1, 9, 25, 49, 81]

# Pull out all digits from a string
text = "Room 42 is on floor 7."
digits = [char for char in text if char.isdigit()]
print(digits)  # Output: ['4', '2', '7']

# Reverse each word in a list
words = ["apple", "banana", "cherry"]
reversed_words = [word[::-1] for word in words]
print(reversed_words)  # Output: ['elppa', 'ananab', 'yrrehc']

# Convert all words to uppercase
words = ["hello", "world", "python"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']














