'''
要求：实现一个解释器，能够完成形如 a+b形式的加法
思考：假设输入为3+4，要进行解析。
      先要读入文本，作为text。
      读取第一个字符，判断是否是整数,是则读入到result中
      读取第二个字符，判断是否是加号，是则追加到result中
      读取第三个字符，判断是否是整数，是则追加到result中
      判断是否已经读取到字符结尾，是则读取结束，进行计算，否则直接报错

      将一段python输入解析为算式进行计算，包含了语义解析和执行的过程。这和语言中的翻译和解释很类似，也就是通过语法解析分出源语言的语义块（包含词语和逻辑），再用目标语言将语义块翻译为目标语言。对应解释器就是，解释器读入后，解析完成，吐出结果
'''
'''
语义块：token
解释器：interpreter
预期结果：
'''


#又该定义这个程序中有哪些语义块了
INTEGER, PLUS, EOF, MINUS = 'INTEGER', 'PLUS', 'EOF', 'MINUS' #将字符串表示的token绑定到变量上，以后可直接调用，无需当作字符串类型（抽象了一层）

class Token(object):
    #该定义语义块了
    def __init__(self, type, value):
        self.type = type
        self.value = value

class Interpreter(object):
    #读入数据时，初始化一个解释器对象
	def __init__(self, text):
        self.text = text  #对象添加一个属性text，将text传入
        self.pos = 0     #从开头依次向后解析，因此初始化解析位置为0
        self.current_token = None #解析出的结果是语义块，对每次解析出的语义块进行标识，以便翻译以及继续解析

	#还不知道该有哪些方法，不过解析过程中一定有用户输入不合规范的字符串，先定个错误生成方法再说
	def error(self):
		raise Exception #管它三七二十一，直接报错就行

	#接下躲不了了，该想怎么解析出语义块了
	#如果是一个人去解析，一定是拿到字符串后，从第一个开始不断看下一个，
	#那就先定义一个不断看下一个的方法吧，看得出这是不断重复的部分
	def get_next_token(self):
		text = self.text #想开始解析总得先读入文本吧。记得文本保存在.text属性里
		#以终为始、未虑胜先虑败，还没开始先想好什么时候结束吧，毕竟每次要解析出下一个语义块总得确定还有东西可以解析吧
		#要是到了最后，就不用管了，那就先来个判断
		if self.pos > len(text) - 1: #还记得pos属性，就是为解析时定位做的准备，每次解析总得知道上次解析到那儿了吧
			return Token(EOF,None) #都解析到最后了，那就是句末语义块了，让解释器知道到这儿这句就完了
								   #所以就用语义块对象生成个句末符号吧，类型就是EOF，值没有

		#前提准备也弄好了，该开始解析了。
		#首先得拿到解析的原材料，就是当前位置的字符
		current_char = text[self.pos]

		#也拿到字符，该看看字符是不是我们期待的语义块了
		#其实目前也就两种，要么是数字，要么是加号
		#是数字的话
		if current_char.isdigit():
			token = Token(INTEGER, int(current_char)) #那就初始化个语义块赶紧捕获过来，写上介绍，类型是INTEGER，值就是对字符整型化后的数字
			#这个语义块也定好，把解析指针向后挪个位置，吐出当前解析好的语义块，这次解析就好了。可是说好的一次只解析一个
			self.pos += 1
			return token

		#不是数字，就该是加号了吧。也没什么得用的方法了，就直接上字符串比较吧
		if current_char == '+':
			token = Token(PLUS,current_char) #初始化一个语义块，把加号捕捉到，类型是PLUS，值就是个'+'
			self.pos += 1
			return token #老规矩了，解析指针向后挪个位置，再吐出解析好的语义块
		elif current_char == '-':
			token = Token(MINUS,current_char)
		#两个都不是？那就抱歉了，除了抛个错误，我也无能为力
		self.error()

	#解析的方法也写好了，不过只是个静态的方法，还不能动起来，得想办法把方法一个个串联起来
	#再加点动力，就像在各个零件间（一个个具体的get_next_token方法）加上齿轮（eat方法）
	def eat(self, token_type): #这样吧，算式格式也是固定的，就是‘a+b'，就看看拿到的token是不是哦我们想要的吧，不是就再无情地抛出错误
		if self.current_token == token_type: #要是当前的语义块是想要的，那就该解析下一个，自然也要赋值给current_token,也就是向后推一个
			self.current_token = self.get_next_token()
		else:
			self.error() #不是期待的语义块？干脆报错吧

	#想想好像该写的都写了，工具也准备好了，那就开始正式的解析吧
	def expr(self):
		self.current_token = self.get_next_token() #指针在0位上，开始运作吧

		#这是方法传出的该是个数字
		left = self.current_token
		#传到齿轮里，看看是否匹配，匹配就往传导到下一个同样的部件
		self.eat(INTEGER) #是的话，这回就从1位继续开始解析，要是中途无误，那current_token就该被设置为PLUS了

		op = self.current_token #再把current_token绑定到变量上
		#再传到齿轮里，这会该是个+，要是匹配就传导到下一个同样的部件
		self.eat(PLUS) #是的话，这回就从2位继续开始解析，要是中途无误，那current_token就该被设置为INTEGER了

		right = self.current_token #再把current_token绑定到变量上
		self.eat(INTER) #这回该到末尾了，current_token也该被置为EOF了

		#至此解析完毕，该把语义块翻译成python语，产生结果
		if op.value == '+':
			result = left.value + right.value
		else:
			result = left.value - right.value
		return result #大功告成，该吐出结果了

