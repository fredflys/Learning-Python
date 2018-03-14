#在不参考源代码（其实看了两眼，就两眼）的情况下，重新写完了代码，没有bug
#这才是学习代码的好办法呀
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

    def error(self):
        raise Exception

    def get_next_token(self):
        text = self.text
        if self.pos > len(text) -1:
            return Token(EOF, None)
        current_char = text[self.pos]
        if current_char.isdigit():
            self.pos += 1
            return Token(INTEGER, int(current_char))
        if current_char == '+':
            self.pos += 1
            return Token(PLUS, current_char)
        if current_char == '-':
            self.pos += 1
            return Token(MINUS, current_char)
        self.error()

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
        if op.value == '+':
            self.eat(PLUS)
        elif op.value == '-':
            self.eat(MINUS)
        right = self.current_token
        self.eat(INTEGER)
        if op.value == '+':
            result = left.value + right.value
            return result
        elif op.value == '-':
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
