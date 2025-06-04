# Import the argparse module
import argparse

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Add a required positional argument called 'name'
parser.add_argument('name')

# Parse the command-line arguments
args = parser.parse_args()

# Print the value of the 'name' argument
print(f"Hello, {args.name}!")
