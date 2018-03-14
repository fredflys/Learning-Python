def term(self):
    self.eat(INTEGER)

def expr(self):
    #先认出（解析）出一个term
    self.current_token = self.get_next_token()

    self.term()
    while self.current_token.type in (PLUS, MINUS):
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            self.term()
        elif token.type == MINUS:
            self.eat(MINUS)
            self.term()

'''
改进版
'''
def term(self):
    token = self.current_token
    self.eat(INTEGER)
    return token.value

def expr(self):
    self.current_token = self.get_next_token() #这时current_token = 第一个整数
    result = self.term() #返回当前token的值，即第一个integer。而current_token = 加号或者减号
    while self.current_token.type in (PLUS, MINUS):
        token = self.current_token #这时token = 加号或减号
        if token.type == PLUS:
            self.eat(PLUS) #这是current_token = 第二个整数
            result = result + self.term() #此时返回token，同时会向下解析，应该会得到句末符
        elif token.type == MINUS:
            self.eat(MINUS)
            result = result - self.term()
    return result
