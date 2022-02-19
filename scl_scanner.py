import sys
import json




# Symbol Table
# Keywords
KEYWORDS = [
    "import",
    "implementation",
    "function",
    "is",
    "variables",
    "define",
    "of",
    "type",
    "integer",
    "double",
    "begin",
    "endfun",
    "display",
    "set",
    "input",
    "if",
    "then",
    "elseif",
    "else",
    "endif",
    "return",
    "exit",
]

# Identifiers

# Operators
ASSIGNMENT_OP = ["="]
ARITHMETIC_OP = ["+", "-", "*", "/"]
RELATIONAL_OP = ["==", "!=", "<", ">", "<=", ">="]

# Constants
# Special Characters
DELIMITER_CHARS = [" ", ",", "\t", '"']


# Scan the contents of the input file
def scan_file(input_file):

    # Retrieve the info from the file
    with open(inputFile) as f:
        print(f.read())

def output_syntax():
    print("Results: ")

# Pass the user's input file into the scan file function
scan_file(sys.argv[1])