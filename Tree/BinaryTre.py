class BinaryTreeNode(object):
    def __init__(self,data,Lchild=None,Rchild=None):
        self.data=data
        self.lchild=Lchild
        self.rchild = Rchild


a=BinaryTreeNode("A")
b=BinaryTreeNode("B")
c=BinaryTreeNode("C")
d=BinaryTreeNode("D")
e=BinaryTreeNode("E")
f=BinaryTreeNode("F")
g=BinaryTreeNode("G")

root=e
e.lchild=a
e.rchild=g
g.rchild=f
a.rchild=c
c.lchild=b
c.rchild=d

'''
print(root.lchild.rchild.lchild.data)
print(root.rchild.lchild)
'''

# 4 种遍历
#1. 前序遍历 [根 左 右]
#2. 中序遍历 [左 根 右]
#3. 右序遍历 [左 右 根]
#4. 层次遍历  每层遍历 需要用到 队列

def pre_order(root):
    if root:  #如果右节点  再遍历
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def middle_order(root):
    if root:
        middle_order(root.lchild)
        print(root.data,end=',')
        middle_order(root.rchild)

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

#4 层次遍历
from collections import deque

def layer_order(root):
    queue=deque()
    queue.append(root)
    while (len(queue)>0):  # 队列不为空 常用语句
        node=queue.popleft()
        print(node.data,end=',')
        if node.lchild:  # 如果有 左孩子节点
            queue.append(node.lchild)
        if node.rchild:  # 如果有 右孩子节点
            queue.append(node.rchild)


pre_order(e)  #E,A,C,B,D,G,F,
print('\n')
middle_order(e) #A,B,C,D,E,G,F,
print('\n')
post_order(e) #B,D,C,A,F,G,E,
print('\n')
print('层次')
layer_order(e)

