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

            # Remove leading and trailing whitespace from the line
            line = line.strip()

            # Skip if the line is the start of a multiline comment
            if line == "description":
                isMultilineComment = True
                continue

            # Skip if the line is the end of a multiline comment
            elif line == "*/":
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

                        # Add newline character to the line since it was removed with the comment
                        line = line + "\n"

                # Gets each word in each line and adds it to the token array
                for word in line.split(" "):

                    # If the word has newline token in it, split it up and add them both to the array
                    position = word.find("\n")
                    if position != -1:
                        if word != "":
                            word = word[0:position]
                            tokens.append(word)
                        tokens.append("\n")
                    elif word != "":
                        tokens.append(word)


    JSON_export(tokens)


def JSON_export(tokens_list):

    # Create a dictionary of tokens
    tokens = {"Tokens": tokens_list}

    # Prints the tokens
    dump = json.dumps(tokens, indent=3)
    print(dump)

    # Encodes the tokens into a JSON format
    encode = json.JSONEncoder().encode(tokens)

    # Write the encoded tokens to a file
    with open("JSON_export.json", "w") as f:
        f.write(encode)


# Pass the user's input file into the scan file function
try:
    scan_file(sys.argv[1])
except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))

# scan_file("welcome.scl")

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
