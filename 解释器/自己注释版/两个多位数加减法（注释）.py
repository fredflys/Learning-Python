# encoding:utf-8
# Token types
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
#定义这次要用到的语义块，和上次没什么不同
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token(object):
    #照样的Token对象，包含type和value属性
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS, or EOF
        self.type = type
        # token value: non-negative integer value, '+', '-', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    #早就，这次间current_char提前到实例初始化阶段就指定
    def __init__(self, text):
        # client string input, e.g. "3 + 5", "12 - 5", etc
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        #文章从无   始
        self.current_token = None
        self.current_char = self.text[self.pos]

    #照旧的报错
    def error(self):
        raise Exception('Error parsing input')

    #新东西来了
    #这个方法就是把解析指针向后拨一位，所以上来不管三七二十一，先播拨一下再说
    #要是原来的位置已经是最后一个了，再动一下一下岂不是超过限制？所以先加个判断，毕竟这是继续执行的前提条件
    def advance(self):
        """Advance the 'pos' pointer and set the 'current_char' variable."""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            #要是已经到了最后还往后拨，那就把当前指针值定位None吧，也就是EOF的值
            self.current_char = None  # Indicates end of input
        else:
            #没到最后？那就把当前所值字符顺便替换一下，毕竟是在实例初始化时就定义的属性
            self.current_char = self.text[self.pos]

    #这是为跳过空格做准备了
    def skip_whitespace(self):
        #要是当前字符是EOF了，那也就不用跳过空格了，对吧？
        #所以要确定它既没到句末，也是空格，这时才跳到下一个
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    #也是新方法，为整型另外建立了一个方法
    #这是为了识别出多位整数
    #只识别个位数时，和其它符号一样，放在get_next_token中，加个判断语句就是
    #但遇到多位数，就避免不了要用while循环，只要当前位是整型，就要判断下一位是不是还是整数
    #如此才能将多位数拼接出来（字符串拼接）
    def integer(self):
        """Return a (multidigit) integer consumed from the input."""
        #先把result初始化为0
        result = ''
        #当前字符没到句末，且是数字
        while self.current_char is not None and self.current_char.isdigit():
            #满足条件，就把字符往后续
            result += self.current_char
            #把解析指针挪到下一位，该判断下一个字符是不是数字了，是则重复这个循环
            self.advance()
        #到这儿也判断完了，把最后得到的结果转换为整型，吐出来
        return int(result)

    #又是熟悉的get方法，但已经与上回不同
    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens.
        """
        #所有判断都得在当前字符不是句末的情况下进行
        #我怎么记得上一个文件好像没这个前提判断和循环？
        while self.current_char is not None:
            #先看是不是空格
            if self.current_char.isspace():
                #是就跳过空格，内有advance方法，会自动跳到下一个字符
                self.skip_whitespace()
                continue

            #这里就用到了刚刚定义的integer方法
            #第二个参数是值，而integer()返回的正是一个整数
            #并不是在get_next_token()方法内，循环而得多位数
            #而是在给出实参处，取到多位数
            #值得留心
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            #这里就是判断算式符号
            #是的话，就不废话，指针向后推一下
            #直接返回语义块
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            #同上
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            #一个判断块都没进去？那就报错吧
            self.error()

        #循环外的语句，只有在current_char是None的情况下会执行
        #返回句末符吧
        return Token(EOF, None)

    #上面是部件，这里是齿轮
    #和上回的方法一样，不费舌
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    #这大概可以说是生产线了，怎么安排部件和齿轮
    def expr(self):
        """Parser / Interpreter

        expr -> INTEGER PLUS INTEGER
        expr -> INTEGER MINUS INTEGER
        """
        # set current token to the first token taken from the input
        #自然是从处理第一个字符开始，同上回
        self.current_token = self.get_next_token()

        # we expect the current token to be an integer
        #这里的期望结果是个整数
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be either a '+' or '-'
        #这里期待的是个算式符号
        #这次在get_next_token()的判断中加了skipspace()方法
        #无论是多个空格还是一个空格，都会在每次调用get_next_token()时过滤掉，视若无物，直接处理空格后面的字符
        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        # we expect the current token to be an integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point either the INTEGER PLUS INTEGER or
        # the INTEGER MINUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding or subtracting two integers,
        # thus effectively interpreting client input
        #和我的路数一样，判断算式符号，再执行加减
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        return result

#同上一次一样，不多提
def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
