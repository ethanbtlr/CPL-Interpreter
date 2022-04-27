import sys
import json

# Symbol Table
# Keywords
KEYWORDS = [
    "import",
    "implementations",
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
DELIMITER_CHARS = [" ", ",", "\t", "\n", ":", ";", "(", ")"]

ALL_CHARS_OPS = ASSIGNMENT_OP + ARITHMETIC_OP + RELATIONAL_OP + DELIMITER_CHARS

# Scan the contents of the input file into a list of expressions
def scan_file(input_file):

    # Change to expressions
    expressions = []

    # Opens file
    with open(input_file) as f:

        contents = f.readlines()
        isMultilineComment = False

        # Gets each line in the file
        for line in contents:

            # Remove leading and trailing spaces from the line
            line = line.strip(" ")

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

                        # Add newline character to the line since it was removed with the comment
                        line = line + "\n"

                expressions.append(line)

    Text_Export(expressions)


def Text_Export(expressions_list):

    # Removes all empty expressions
    for i in expressions_list:
        try:
            expressions_list.remove("")
        except ValueError:
            break

    expressions = {"expressions": expressions_list}


    # Write the encoded expressions to a file
    with open("Text_Export.txt", "w") as f:
        for expression in expressions_list:
            f.write(expression)


# Pass the user's input file into the scan file function
# Commented this out to prevent it from being called when imported in another file
''' 
try:
    scan_file(sys.argv[1])

except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))

'''

