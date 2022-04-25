import scanner
import sys
import json
import anytree
class Parser:
    
    def __init__(self, input):

        # Create variables for the class
        self.input = input
        self.current_location = 0
        self.read_file = "Text_Export.txt"
        self.length = len(self.read_file) # Amount of expressions found
        self.identifiers = []
        self.values = []


    # Private start function
    def _start(self):
        print("Parsing")
        self.getNextToken()          


                  

    # Get next token function
    def getNextToken(self):
        pass

       





    # Identifier exists function
    def identifierExists(self, identifier):



    # Begin function
    def begin(self):
        self._start()
        
    



# Pass the user's input file into the scan file function
try:
    # input = sys.argv[1] UPDATE THIS
    input = "welcome.scl"
    parser = Parser(input)
    scanner.scan_file(input)
    parser.begin()

except IndexError as err:
    print("A file wasn't passed as an argument. Error: {0}".format(err))