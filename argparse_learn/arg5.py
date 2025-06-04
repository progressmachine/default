# Import argparse
import argparse

# Create parser object
parser = argparse.ArgumentParser()

# Add argument that accepts multiple integers
parser.add_argument('--nums', nargs='+', type=int, help='List of numbers')

# Parse args
args = parser.parse_args()

# Print the list and its sum
print(f"Numbers: {args.nums}, Sum: {sum(args.nums)}")
