from tokens import Integer , Float , Operation , Declare , Variable , Boolean , Comparison, Reserved

class Lexer:

    digits = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    operations = "+-*/()="
    declare = ["make"]
    stopwords = [" "]
    boolean = ["and" , "or" , "not"]
    comparisons = [">", "<", ">=", "<=", "?="]
    specialCharacters = "><=?"
    reserved = ["if", "elif", "else", "do", "while"]


    def __init__(self, text):
        self.text = text
        self.idx = 0
        self.tokens = []
        self.char = self.text[self.idx]
        self.token = None
    
    def  tokenize(self):
        while self.idx < len(self.text):
            if self.char in Lexer.digits:
                self.token  = self.extract_num()
            elif self.char in Lexer.operations:
                self.token = Operation(self.char)
                self.move()
            elif self.char in Lexer.stopwords:
                self.move()
                continue
            elif self.char in Lexer.letters:
                word = self.extract_word()
                if word in Lexer.declare:
                    self.token = Declare(word)
                elif word in Lexer.boolean:
                    self.token = Boolean(word)
                elif word in Lexer.reserved:
                    self.token = Reserved(word)
                else: 
                    self.token = Variable(word)

            elif self.char in Lexer.specialCharacters:
                comparisonOperator = ""
                while self.char in Lexer.specialCharacters and self.idx < len(self.text):
                    comparisonOperator += self.char
                    self.move()
                
                self.token = Comparison(comparisonOperator) 

            self.tokens.append(self.token)

        return self.tokens
    
    def extract_num(self):
        num = ""
        isFloat = False
        while (self.char in Lexer.digits or self.char == ".") and (self.idx < len(self.text)):
            if self.char == ".":
                isFloat = True
            num += self.char
            self.move()

        return Integer(num) if not isFloat else Float(num)
    
    def extract_word(self):
        word = ""
        while self.char in Lexer.letters and self.idx < len(self.text):
            word += self.char
            self.move()

        return word

    def move(self):
        self.idx +=1 
        if self.idx < len(self.text):
            self.char = self.text[self.idx] 


