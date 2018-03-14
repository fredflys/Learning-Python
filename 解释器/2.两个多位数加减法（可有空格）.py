'''token types
EOF token is used to indicate that there is no more for lexical analysis
'''
'''
Token:INTEGER, PLUS, MINUS, EOF
lexme:词位，可形成一个token的字符序列
expr方法：找出记号流的结构，解释算术表达式，产生结果 parsing and interpreting
parsing-发布信息分析:辨识出记号流中短语

'''
INTEGER, PLUS, MINUS, EOF, MULTI, DIVI = 'INTEGER', "PLUS", 'MINUS', 'EOF', 'MULTI', 'DIVI'

class Token:
    def __init__(self, type, value):
        #token types:INTEGER, PLUS, MINUS, EOF
        self.type = type
        #token value:non-negative integer value, '+' , '-', or None
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    #Interpreter初始化
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    #解析错误
    def error(self):
        raise Exception('Error parsing input.')

    #读取下一位
    def advance(self):
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    #跳过空格
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    #读取多位数字
    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULTI, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVI, '/')


            self.error()

        return Token(EOF,None)

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        elif op.type == MINUS:
            self.eat(MINUS)
        elif op.type == MULTI:
            self.eat(MULTI)
        elif op.type == DIVI:
            self.eat(DIVI)

        right = self.current_token
        self.eat(INTEGER)

        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result


def main():
    while True:
        try:
            text = input('calc >')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()

