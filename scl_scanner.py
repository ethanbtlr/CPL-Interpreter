from lib2to3.pgen2 import token
import sys
import json
import string


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
    tokens = []

    # Opens file
    with open(input_file) as f:

        contents = f.readlines()

        # Gets each line in the file
        for line in contents:

            # Checks to see if the line contains a single-line comment
            if '//' in line:

                # Skips a line if it is a just a comment
                if line.startswith("//"):
                    continue
                
                # If there is a single line comment in the line, but not at the beginning
                else:
                    # Find where the comment starts
                    position = line.find("//")
                    
                    # Slice the string to remove the comment
                    line = line[0:position]
                    

                
                
            # Gets each word in each line and adds it to the token array
            for word in line.split(" "):

                if word != "":
                    tokens.append(word)

    print(tokens)


# Pass the user's input file into the scan file function

# scan_file(sys.argv[1])
scan_file("test.scl")

# List of tested files that were given and used
""" 
arduino_ex1.scl
arrayex1.scl
arrayex1b.scl
arrayex4b.scl
bitops1.scl
datablistp.scl
linkedg.scl
welcome.scl
"""
