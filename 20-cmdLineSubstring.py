import sys

if len(sys.argv) != 3:
    print("Please provide exactly two arguments: a main string and a substring.")
    sys.exit(1)

main_string = sys.argv[1]
substring = sys.argv[2]

if substring in main_string:
    print(f"'{substring}' is found in '{main_string}'")
else:
    print(f"'{substring}' is not found in '{main_string}'")
