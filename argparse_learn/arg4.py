# Import argparse
import argparse

# Create parser object
parser = argparse.ArgumentParser()

# Add an argument with limited choices
parser.add_argument('--color', choices=['red', 'green', 'blue'], help='Pick a color')

# Parse args
args = parser.parse_args()

# Print chosen color
print(f"Selected color: {args.color}")
