# Stack
# use list to implement Stack
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def get_top(self):    # 查看stack
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return  None # or Raise Error
    def isempty(self):
        return len(self.stack) ==0


# 括号匹配问题  1234 4321 [{()}]
'''
让每个 左括号 压栈，  每个匹配到的右括号， 出栈一次
直达 最里层 eg. ）-->（ 一层层出
看最后stack是不是空的 
'''
def Brackets_Match(string):
    stack_string= Stack()
    bracket_dict={')':'(',']':'[','}':'{'}   # 对应的字典
    for chr in string:
        if chr in {'(','{','{'}:  #set 集合
            stack_string.push(chr)
        elif chr in {')','}','}'}:  #set 集合
            if stack_string.isempty():
                return False  # ) 不可以先有 )
            elif stack_string.get_top() ==bracket_dict[chr]:
                stack_string.pop()
            else:  #stack_string.get_top() !=bracket_dict[chr]:
                return False
        else:  # 其他字符 啥也不干
            continue
    #最后再看 stack 是否为空empty
    if stack_string.isempty():
        return True
    else:
        return False

def Test():
    print(Brackets_Match('()'))
    print(Brackets_Match('( 2 3 )'))
    print(Brackets_Match('{[(2+5)*8-7]/6}'))
    print(Brackets_Match(')('))
    print(Brackets_Match('()[]{}(){{}}'))
    print(Brackets_Match('(][}'))
Test()