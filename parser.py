import scl_scanner
import sys
import json

class Parser:
    
    def __init__(self, input):
        self.input = input
        self.current_location = 0
        self.read_file = "JSON_export.json"
        self.nextToken = None

    # Private start function
    def _start(self):
        print("Starting")
        self.getNextToken()                        

    def getNextToken(self):
        print("getting next token")
        json.load(self.read_file)

    # Identifier exists function
    def identifierExists(identifier):
        print("Identifier exists")

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