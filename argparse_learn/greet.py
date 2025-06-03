import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("--polite", action="store_true")

args = parser.parse_args()

if args.polite:
	print(f"Hello, {args.name}. It's a pleasure to meet you.")
else:
	print(f"Hey, {args.name}!")
