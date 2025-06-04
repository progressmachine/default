# Import argparse
import argparse

# Create parser object
parser = argparse.ArgumentParser()

# Add a flag that sets debug to True if used
parser.add_argument('--debug', action='store_true', help='Enable debug mode')

# Parse args
args = parser.parse_args()

# Check and print debug status
if args.debug:
    print("Debug mode is ON")
else:
    print("Debug mode is OFF")
