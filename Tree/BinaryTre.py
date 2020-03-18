# Refer to BinaryTree.png

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

print(root.lchild.rchild.lchild.data)
print(root.rchild.lchild)
