# encoding:utf-8
# 结合：同种运算符，先计算左边的
# 优先：异类运算符，乘除法优先

#
# precedence level  associativity  operators
#       1              left          +，-
#       2              left          *，/


# 对每一个级别的运算定义个非终止符。产生体中应包括当前级别的算术符号，以及更高优先级的非终止符
# 创建一个额外的非终止符，来处理基本表达式单元（integer）
# 1.expr:term((PLUS|MINUS)term)*
# 2.term:factor((MUL|DIV)factor)*
# 3.factor:INTEGER
# 4.INTEGER:
# 乘除会优先运算，在加减运算中，整体会被看成一个结果
INTEGER, PLUS, MINUS, MUL, DIV, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'
)


class Token(object):
    """
    Token类，用于生成基本的token，其有两个属性：type和value
    """
    def __init__(self, token_type, token_value):
        self.type = token_type
        self.value = token_value


class Lexer(object):
    """
    词法分析器，用于读入文本，分析出token
    其有三个属性：文本，指针位置，当前字符
    初始化时，先导入文本，再将解析指针拨到0，当前字符设为指针所指字符
    """
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        """
        自然会遇到无法解析的字符，提前定好报错策略
        :return:
        """
        raise Exception('Invalid character.')

    def advance(self):
        """
        向前拨动指针的方法，要解析整个文本，自然要遍历文本
        遍历的方法便是依次向下分析
        如果指针位置超出末尾，则分析结束，将当前字符设置为None（EOF）
        """
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """
        文本中允许出现空格，因此也要准备跳过空格的方法
        如果没有超出文本，又是空格，则将指针向前拨动一下
        """
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """
        以下都是识别token的方法
        integer单独放在一个方法中，因为它是进行运算的基本元素
        如果当前字符没有超出文本，又是数字，则继续向下解析，这是为了解析出多位整数
        初始值result是字符串格式，可以直接在其后续上数字
        最后记得要转为整型将值传出
        """
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_current_token(self):
        """
        将文本分解为具体的token
        如果既没超出文本长度，而又不是任何token，则报错
        已超出句末，则返回EOF
        :return: a single token
        """
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
                return Token(MUL, '*')
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            self.error()
        return Token(EOF, None)


class Interpreter(object):
    """
    解释器，真正地开始操作token，实现预定的计算规则，完成各类运算
    初始化时要载入词法解释器，先告诉解释器如何从文本中分析出token
    通过解释器才能知道一系列的token组合到底说了生命
    """
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_current_token()

    def error(self):
        """
        在这一步出错就是类似自然语言中的语法错误了，
        词法分析中的错误类似拼写错误
        :return:
        """
        raise Exception('Invalid syntax.')

    def eat(self, token_type):
        """
        如果token的类型和传入的类型一致，则吃下当下token
        :param token_type:
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_current_token()
        else:
            self.error()

    def factor(self):
        """
        factor: INTEGER
        :return:
        """
        token = self.current_token
        self.eat(INTEGER)
