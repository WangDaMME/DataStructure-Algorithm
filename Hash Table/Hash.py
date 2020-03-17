# 实现 哈希 需要一个链表类
class Linkedlist(object):
    # 函数里面套函数是一样的, ll的 实例instance . 这个node
    class Node(object):
        def __init__(self,element):
            self.item=element
            self.pnext=None

    # 迭代器类 ∵next
    class LinkedListIterator(object):
        def __init__(self,node):
            self.node=node   # 传进来都是node
        def __next__(self):    # 调用 把head 头结点传进来
            if self.node:   # 有值
                cur_node=self.node
                self.node=cur_node.pnext
                return cur_node.item
            else:              # node 为空
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self,iterable=None):  #iterable 可迭代对象 eg 列表
        self.head=None
        self.tail=None
        if iterable: # 传入了iterable
            self.extend(iterable)   #把列表整个 加到尾部

    def append(self,obj):
        append_node=self.Node(obj)    # 创建一个node 用self 调用
        if not self.head:      # 链表head为空，head=None not--> 变为True了
            self.head=append_node
            self.tail=append_node
        else:
            self.tail.pnext=append_node #连到表尾
            self.tail=append_node  # 更新node

    def extend(self,iterable):
        for obj in iterable:
            self.append(obj)

    def find(self,obj):
        for n in self:  # 列表里查找 for 循环查 for i in list[1,2,3...]， 同理 是迭代器，就在自己这里查
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):  # 让链表 支持迭代，支持for循环 iterator
        return self.LinkedListIterator(self.head)  # 把头节点传进去

    def __repr__(self):  # 让对象以字符串的形式表现出来
        return "<<"+','.join(map(str,self))+'>>'

lk=Linkedlist([1,2,3,4,5])
# 可迭代 -- 可以打印了
'''
for element in lk:
    print(element,end=',')
'''
#print(lk)

class HashTable(object):
    def __init__(self,size=101):
        self.size=size
        self.T=[Linkedlist() for i in range(self.size)]  #direct addressing table 直接寻址表      self.size那么多 链表

    def H(self,k):   # 哈希函数
        return  k%self.size

    def insert(self,element):
        i=self.H(element)  # i: hash_key 哈希函数值
        if self.find(element):
            print('The element is existing in Hash')
        else:
            self.T[i].append(element)


    def find(self,element):
        i=self.H(element)
        return self.T[i].find(element)   # 再对应链表里找

ht=HashTable() # 默认101
ht.insert(1)
ht.insert(5)
ht.insert(3)
ht.insert(102)

print("<<"+','.join(map(str,ht.T))+'>>')
print(ht.find(1))
print(ht.find(102))
print(ht.find(2))
