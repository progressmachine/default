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