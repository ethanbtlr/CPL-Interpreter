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
    #reads in file

    #opens file in read mode
    f = open(input_file,"r")
    contents = f.readlines()


    for line in contents:
        split = line.split()

        for word in split:
            stripped = word.strip()
            print(word)

    f.close()
    return 0
    
    

def output_syntax():
    print("Results: ")

# Pass the user's input file into the scan file function
scan_file(sys.argv[1])



# List of tested files that were given and used
''' 
arduino_ex1.scl
arrayex1.scl
arrayex1b.scl
arrayex4b.scl
bitops1.scl
datablistp.scl
linkedg.scl
welcome.scl
'''