INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]
    ####################################################
    #                  lexer code                      #
    ####################################################
    def error(self):
        raise Exception('Invalid syntax')
    def advance(self):
        self.pos +=1
        if self.pos > len(self.text) - 1:
            return Token(EOF, None)
        else:
            self.current_char = self.text[self.pos]
    def skip_whitespaces(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result = result + self.current_char
            self.advance()
        return int(result)

    ####################################################
    #                     Parser                       #
    ####################################################
    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespaces()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                return Token(PLUS, '+')
            if self.current_char == '-':
                return Token(PLUS, '-')
            self.error()
        return Token(EOF, None)
    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value
    ####################################################
    #                   Interpreter                    #
    ####################################################
    def expr(self):
        self.current_token = self.get_next_token()
        result = self.term()
        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token #把加减号保存下来
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term() #吐出加减号后的值，current_token则置为下一个加减号
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()


