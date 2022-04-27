import scanner
import parser

# Pass the user's input file into the scan file function
try:
    input = "welcome.scl"
    scanner.scan_file(input)

    # Parse the scanned file 
    parser = parser.Parser("Text_export.txt")
    parser.begin()

except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))


# Parser identifies what the tokens are in each expression (keyword, constants, etc.) and exports the tokens as a parse tree


# The interpreter takes the parse tree as input


# The parse tree is converted to python syntax 





