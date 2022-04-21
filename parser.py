from xml.dom.minidom import Identified
import scl_scanner
import sys
import json

class Parser:
    
    def __init__(self, input):

        # Create variables for the class
        self.input = input
        self.current_location = 0
        self.read_file = "JSON_export.json"
        self.file_object = open("JSON_export.json", "r")
        self.loaded_file = json.load(self.file_object)
        self.length = len(self.loaded_file["Tokens"]) # Amount of tokens found
        self.identifiers = []
        self.values = []


    # Private start function
    def _start(self):
        print("Starting")
        self.getNextToken()                        

    # Get next token function
    def getNextToken(self):

        # If there are more tokens to parse
        if self.current_location < self.length:
            nextToken = self.loaded_file["Tokens"][self.current_location]
            
            # If the next token is a keyword which precedes identifiers, add the token after that to the list of identifiers
            if nextToken == "define" or nextToken == "function" or nextToken == "set":
                self.identifiers.append(self.loaded_file["Tokens"][self.current_location+1])
            # If the next token is =, add the token after that to the list of values
            if nextToken == "=":
                self.values.append(self.loaded_file["Tokens"][self.current_location+1])
            
            # Print the next token. repr gets the string representation which allows special characters like \n and \t to be printed
            print("Next token is: " + repr(nextToken))
            self.current_location += 1

            # Call the identiferExists function
            self.identifierExists(nextToken)
            


    # Identifier exists function
    def identifierExists(self, identifier):

        # If the token is an operator
        if identifier in scl_scanner.ALL_CHARS_OPS:
            print(repr(identifier) + " is an operator")
            self.getNextToken()

        # If the token is a keyword
        elif identifier in scl_scanner.KEYWORDS:
            print(identifier + " is a keyword")
            self.getNextToken()

        # If the token is an identifier
        elif identifier in self.identifiers:
            print(identifier + " is an identifier" )
            self.getNextToken()
            
        # If the token is a value
        elif identifier in self.values:
            print(identifier + " is a value" )
            self.getNextToken()

        # If there is a string wrapped in quotes
        elif str(identifier).startswith('"') and str(identifier).endswith('"'):
            print(identifier + " is a string" )
            self.getNextToken()

        # Syntax error
        else:
            print("Syntax error")


    # Begin function
    def begin(self):
        self._start()
        
    



# Pass the user's input file into the scan file function
try:
    input = sys.argv[1]
    parser = Parser(input)
    scl_scanner.scan_file(input)
    parser.begin()

except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))