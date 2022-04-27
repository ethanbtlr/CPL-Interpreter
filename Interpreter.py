import scanner
import parser

try:
    # Pass the user's input file into the scan file function
    input = "welcome.scl"

    # Scanner exports the expressions into a text file
    scanner.scan_file(input)

    # Build a parse tree with the parser using the file of expressions
    parser = parser.Parser("Text_export.txt")
    parser.begin()

    # The parse tree will be traversed using a preorder traversal
    # Each expression in the tree will converted into Python syntax and saved in the file Python_from_Scl_.py

    # The Python code will then be passed as file input and ran with the exec() function
    exec("Python_From_Scl.py")


except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))
