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

# Operators
ASSIGNMENT_OP = ["="]
ARITHMETIC_OP = ["+", "-", "*", "/"]
RELATIONAL_OP = ["==", "!=", "<", ">", "<=", ">="]

# Special Characters
DELIMITER_CHARS = [" ", ",", "\t", '"']


# Scan the contents of the input file
def scan_file(input_file):
    tokens = []

    # Opens file
    with open(input_file) as f:

        contents = f.readlines()
        isMultilineComment = False

        # Gets each line in the file
        for line in contents:

            # Skip if the line is the start of a multiline comment
            if line.strip() == "description":
                isMultilineComment = True
                continue

            # Skip if the line is the end of a multiline comment
            elif line.strip() == "*/":
                isMultilineComment = False
                continue

            # If the line isn't part of a multiline comment
            elif isMultilineComment == False:

                # Checks to see if the line contains a single-line comment
                if "//" in line:

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

    JSON_export(tokens)


def JSON_export(tokens_list):

    # Prints the tokens
    print(json.dumps({"Tokens": tokens_list}, indent=2))

    # Encodes the tokens into a JSON format
    encode = json.JSONEncoder().encode({"Tokens": tokens_list})

    # Write the encoded tokens to a file
    with open("JSON_export.json", "w") as f:
        f.write(encode)





# Pass the user's input file into the scan file function
scan_file(sys.argv[1])
# scan_file("test.scl")

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
