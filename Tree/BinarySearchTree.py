# BST: Binary Search Tree
# lchild.value < rchild.value
# 左孩子节点里的值 < 右孩子节点的值

class BSTNode(object):
    def __init__(self,value):
        self.data=value
        self.lchild=None
        self.rchild=None
        self.parent=None

class BSTree(object):
    def __init__(self,lst=None):
        self.root=None
        if lst:
            for elemnet in lst:
                # 循环插入
                self.insert_No_recur(elemnet)

    # 插在哪个节点
    def insert_recursion(self,node,value):   #递归 需要每次调用自己的节点
        # 空树
        if not node:             # node=None 即 self.root=None
            node=BSTNode(value)  # 节点为空，创建 节点返回  #!!!
        #树的左边  递归  把它插到左边
        elif value<node.data:  #传入的 < 该节点 node存的 node.data
            self.insert_recursion(node.lchild,value)  #插到该几点左孩子
            node.lchild.parent=node  # 把新插的父节点连上  #!!!
        # 树的右边
        elif value>node.data:
            self.insert_recursion(node.rchild,value)
            node.rchild.parent=node
        # else ： 等于 情况 向集合 一样 重复的什么也不做

        return node

    # 一般 不用递归的会快些
    def insert_No_recur(self,value):
        p=self.root
        if not p:  #p(self.root)不为空
            self.root=BSTNode(value)
            return

        while True:
            if value<p.data:
                if p.lchild:  # 有左节点
                    p=p.lchild  # 再往下看，
                else:  #不存在 左孩子，直接插
                    p.lchild=BSTNode(value)
                    p.lchild.parent=p   # 双向指针
                    return  #完成
            # 往右边看
            elif value>p.data:
                if p.rchild:
                    p=p.rchild
                else:
                    p.rchild=BSTNode(value)
                    p.rchild.parent=p
                    return  #完成
            else:  # 相等时，也是什么也不做
                return  # 完成

#------------------ Trasverse-------------------------------#

    def pre_Trasverse(self,root):
        if root:  #root 不为空
           print(root.data,end=',')
           self.pre_Trasverse(root.lchild)
           self.pre_Trasverse(root.rchild)

# 中序遍历 肯定是有序的 因为 按最小  --- 中 -- 最大 放出来
    def middle_Trasverse(self,root):
        if root:  #root 不为空
           self.middle_Trasverse(root.lchild)
           print(root.data,end=',')
           self.middle_Trasverse(root.rchild)

    def post_Trasverse(self,root):
        if root:  #root 不为空
           self.post_Trasverse(root.lchild)
           self.post_Trasverse(root.rchild)
           print(root.data,end=',')

#------------------ Query-------------------------------#
    def query_recursion(self,node,value):   # 必须要传node
        if not node:  # node 为空
            return None
        if value<node.data:
            self.query_recursion(node.lchild,value)
        elif value>node.data:
            self.query_recursion(node.rchild,value)
        else:   # 等于， 直接返回
            return node    # 返回 node

    def query_no_recursion(self,value):
        p=self.root
        if not p:
            return None  # P 为空
        while p:   # p不为空
            if value<p.data:
                p=p.lchild
            elif value>p.data:
                p=p.rchild
            else: #找到了
                return p
        else:
            return None # 执行完 找不到
                    





import random
lst=list(range(10))
random.shuffle(lst)
tree=BSTree(lst)


tree.pre_Trasverse(tree.root)
print('')
tree.middle_Trasverse(tree.root)  #--- Ordered 有序的 先小 --中---大
print('')
tree.post_Trasverse(tree.root)
print('')
print('==============')

lst2=list(range(0,500,2))   # 全是 奇数的树
random.shuffle(lst2)

tree2=BSTree(lst2)
print(tree2.query_no_recursion(4).data)
print(tree2.query_no_recursion(3))
