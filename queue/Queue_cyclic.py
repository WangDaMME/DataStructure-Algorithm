class Queue(object):
    def __init__(self,Maxsize=12):   # 定长
        self.size=Maxsize
        self.queue= [0 for _ in range(Maxsize)]
        self.rear=0  #队尾，进队端
        self.front=0 #队尾， 出队端

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return self.rear==self.front

    def is_full(self):
        return (self.rear+1)%self.size == self.front

    def push(self,element):    # 放到队尾
        if not self.is_full(): #不满
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=element
        else:
            raise IndexError("Queue is full!")

    def pop(self):
        if not self.is_empty():  # 不空，有可pop的
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise  IndexError("Queue is empty!")



def Test():
    q=Queue(5)
    print(q.is_empty())
    for i in range(4):  # 牺牲一块空间 区别 空 与满， 所以只能存 4次
        q.push(i)
    # FIFO
    print(q.pop())
    print(q.push(100))
    for i in range(len(q)-1):
        print(q.pop())
    print(q.is_full())

Test()

print('========== Built-in Modules ==========')
# 内置模块 Built-in modules
from collections import deque  # collections 包含一些数据结构域
q=deque([1,2,3],5)
# 单向队列
print("单向队列")
q.append(1) # rear进队
print(q.append(2))
print(q.popleft()) # front队首出队  res---1

# 双向队列
print("双向队列")
print(q.appendleft(100)) # 队首 进队
print(q.pop()) #队尾 出队 rear


q2=deque([1,2,3,4,5],5)
q2.append(6)
print('结果为2 因为1 已经被6挤走',q2.popleft())  # 结果为2 因为1 已经被6挤走

print('========== Linux Tail 命令 ==========')
def Tail(n): # n看几个
    with open('test.txt','r') as f:
        q=deque(f,n)
        return q

#print(Tail(5))
for line in Tail(5):
    print(line,end='')