# Import argparse
import argparse

# Create parser object
parser = argparse.ArgumentParser()

# Add an optional argument with a default value
parser.add_argument('--age', type=int, default=18, help='Your age')

# Parse args
args = parser.parse_args()

# Print the age
print(f"Age is {args.age}")
