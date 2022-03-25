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
DELIMITER_CHARS = [" ", ",", "\t", "\n", ":", ";", "(", ")"]

ALL_CHARS__OPS = ASSIGNMENT_OP + ARITHMETIC_OP + RELATIONAL_OP + DELIMITER_CHARS


# Scan the contents of the input file
def scan_file(input_file):
    tokens = []

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

                # Gets each word in each line and adds it to the token array
                for word in line.split(" "):

                    # If the word has special character or operator in it, split the tokens up and add them both to the array
                    hasSpecialChar = False
                    for i in ALL_CHARS__OPS:

                        # If a special character is found
                        position = word.find(i)
                        if position != -1:
                            lengthOfWord = len(line)
                            lengthOfChar = len(i)

                            # Say a special character has been found
                            hasSpecialChar = True

                            # If special character is at the beginning
                            if position == 0:
                                # Append the special character
                                tokens.append(i)

                                # Append everything after the special character
                                word = word[lengthOfChar:lengthOfWord]
                                tokens.append(word)

                            # If special character is at the end
                            elif position == (lengthOfWord - 1):
                                # Append everything before the special character
                                word = word[0:position]
                                tokens.append(word)

                                # Append the special character
                                tokens.append(i)

                            # If a special character is in the middle
                            else:
                                # Append everything before the special character
                                wordOne = word[0:position]
                                tokens.append(wordOne)

                                # Append the special character
                                tokens.append(i)

                                # Append everything after the special character
                                wordTwo = word[(position + lengthOfChar) : lengthOfWord]

                                # See if another special character is in the rest of the list
                                hasAnotherSpecialChar = False
                                for j in ALL_CHARS__OPS:
                                    position = line.find(j)
                                    if j != -1:
                                        word = wordTwo
                                        hasAnotherSpecialChar = True
                                # If there isn't another special character just add the rest of the word to the token list
                                if hasAnotherSpecialChar == False:
                                    tokens.append(wordTwo)

                    # If a special character isn't found
                    if hasSpecialChar == False:
                        tokens.append(word)

    JSON_export(tokens)


def JSON_export(tokens_list):

    # Removes all empty tokens
    for i in tokens_list:
        try:
            tokens_list.remove("")
        except ValueError:
            break

    tokens = {"Tokens": tokens_list}

    # Prints the tokens
    dump = json.dumps(tokens)
    print(dump)

    # Encodes the tokens into a JSON format
    encode = json.JSONEncoder().encode(tokens)

    # Write the encoded tokens to a file
    with open("JSON_export.json", "w") as f:
        f.write(encode)


# Pass the user's input file into the scan file function
# Commented this out to prevent it from being called when imported in another file
''' 
try:
    scan_file(sys.argv[1])

except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))

'''


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
