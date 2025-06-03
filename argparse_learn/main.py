import argparse

parser = argparse.ArgumentParser()

parser.add_argument("num1", type=int, help="First number to add.")
parser.add_argument("num2", type=int, help="Second number to add.")

args = parser.parse_args()

result = args.num1 + args.num2
print(f"The sum is = {result}.")
