'''
程序可计算形如a+b格式的算式（不能有空格）:
思路：用户输入的是a+b格式的string，将其解析为解释器可以理解的元素--token，转换成python算式
进行计算，输出结果
结构：Token类：指定基本元素的种类和值
      Interpreter类：读入用户输入的算式并解析
'''
# encoding:utf-8
# token types
# EOF is used to indeicate that there is no more for lexical analysis
INTEGER, PLUS, EOF, MINUS = 'INTEGER','PLUS','EOF', 'MINUS'


class Token(object):
    def __init__(self, type, value):
        # token type:INTEGER, PLUS, EOF
        self.type = type
        # token value:0,1,2,3,4,5,6,7,8,9,+ or None
        self.value = value

    def __str__(self):
        '''
        string reprsentation of the class instance
        Examples:
            Token(INTEGER, 3)
            Token(PLUS,'+')
        '''
        return 'Token({type},{value})'.format(
            type=self.type,
            # repr:python friendly,easier for eval use
            # str:user friendly, easier to read
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self,text):
        # client string input: e.g. "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None

    def error(self):
        raise Exception

    def get_next_token(self):
        '''
        Lexical analyzer(also known as scanner or tokenizer)
        This method is responsible for breaking a sentence apart into tokens,
        one token at a time.
        '''
        text = self.text
        '''
        Is self.pos index past the end of the self.text?
        If so, then return EOF token because there is no more?
        input left to convert into tokens
        '''
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        '''
        Get a character at the position self.pos and decide
        what token to use based on the single cahracter'''
        current_char = text[self.pos]

        '''
        if the character is a digit then convert it to integer,
        create an INTEGER token, increment self.pos index to point 
        to the next character after the digit, and return the INTEGER token
        '''
        if current_char.isdigit():
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(MINUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        '''
        compare the current token type with the passed token type,
        if they match then eat the current token and assign the next token to
        self.current_token,otherwise raise an exception
        '''
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''
        expr:integer plus integer
        '''
        # set the current token to the first toeken from the input
        self.current_token = self.get_next_token()

        # we expect the first token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # we expect the second token to be '+'
        op = self.current_token
        if op.value == '+':
            self.eat(PLUS)
        elif op.value == '-':
            self.eat(MINUS)

        # we expect the third token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the current token is set to EOF token

        '''at this point INTEGER PLUS INTEGER sequence has been successfully
        found and the method cna just return the result of adding two integers
        thus effectively interpreting client input
        '''
        if op.value == '+':
            result = left.value + right.value
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
        '''
        假设输入为3+4
        1.实例化一个Interpreter对象           
        self.text = '3+4'
        self.pos = 0
        self.current_token = None
        2.嗲用interpreter.expr()方法后：
        self.current_token = self.get_next_token() $ = token
            text = self.text #3+4
            self.pos < len(text) - 1 #pos=0
            current_char = text[self.pos] # current_char = text[0] = '3'
            current_char is digit:
            token = Token(INTEGER, int(current_char))
                        self.type = INTEGER    #token.type
                        self.value = 3         #token.value
            self.pos += 1  #pos=1
            return token
            
        left = self.current_token # left = token type-INTEGER,value-3
        self.eat(INTEGER)
            token.type == INTEGER:
            self.current_token = self.get_next_token
                 text = self.text #3+4
                 self.pos < len(text) - 1 #pos=1
                 current_char = text[self.pos] # current_char = text[1] = '+'
                 current_char is '+':
                 token = Token(PLUS, current_char)
                    self.type = PLUS       #token.type
                    self.value = '+'       #token.value
                self.pos += 1    #pos=2
                return token #current_token = '+'
                
        op = self.current_token #op = "+'
        self.eat(PLUS)
            ···
            
        right = self.current_token
        self.eat(INTEGER)            
            ···    #current_toekn = Token(EOF,None)
        
        reulst = left.value + right.value # 3+4
        return result  # 7 
        '''
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()

