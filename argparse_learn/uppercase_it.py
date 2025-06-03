import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file")

args = parser.parse_args()

with open(args.file, "r") as f:
	content = f.read()

print("\nThis is the updated content of the file.")
print("\n" + content.upper())

with open(args.file, "w") as f:
	f.write(content.upper())
