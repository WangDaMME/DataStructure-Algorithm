''' AVL Tree'''
from BST import  BSTNode, BSTree

class AVLNode(BSTNode):     #继承BSTNode
    def __init__(self,data):
        # 初始化 父类构造
        BSTNode.__init__(self,data)  # 把要赋的值data传进来
        self.bf=0                    # 多一个balance factor

class AVLTree(BSTree):
    def __init__(self,lst):
        BSTree.__init__(self,lst)

    #1. 左旋  - 右孩子 右子树
    def Rotate_Left(self,p,c):  # p,c 节点
        #s1,s3不用动
        s2=c.lchild
        p.rchild=s2  # p,c 裂开
        if s2:   # s2 不为空
            s2.parent=p
        c.lchild=p
        p.parent=c
        # 别忘了 更新 Balance Factor
        p.bf=0
        c.bf=0

    #2. 右旋  - 左孩子 左子树
    def Rotate_Right(self,p,c):  # p,c 节点
        #s1,s3不用动
        s2=c.rchild
        p.lchild=s2  # p,c 裂开
        if s2:   # s2 不为空
            s2.parent=p
        c.rchild=p
        p.parent=c
        # 别忘了 更新 Balance Factor
        p.bf=0
        c.bf=0

    #3. 右旋_左旋  - 右孩子的左子树
    def Rotate_Right_Left(self,p,c):  # p,c 节点
        # 定义g节点
        g=c.lchild
        #s1,s4 不会动， 只有 g的两个节点 归属 会发生变化(s2,s3)
        s3=g.rchild
        c.lchild=s3
        if s3:  #s3 不为空
            s3.parent=c
        g.rchild = c
        c.parent = g

        s2=g.lchild
        p.rchild=s2
        if s2:        #s2不为空
            s2.parent=p
        g.lchild=p
        p.parent=g

        # 更新 Balance Factor
        # 最后的bf与 key 插在 g 中哪个节点有关系
        if g.bf>0:   #ie. 即g.bf=1 插在了s3 右边沉
            p.bf=-1 # 左边沉 s1（h）>s2（h-1）
            c.bf=0
        elif g.bf<0:      # 插在了s2
            p.bf=0
            c.bf=1   # 左边沉 s3（h-1）<s4（h）
        else:  # 特殊情况  s1~s4 全为 None   --- 插的是 g 节点自己
            p.bf=0
            c.bf=0
        g.bf=0 # 最后g 平衡

        # 4. 左旋_右旋  - 左孩子的右子树  【3.镜面 s1s2s3s4 <--->s4 s3s2s1,  left right 互换 1，-1互换]
    def Rotate_Left_Right(self, p, c):  # p,c 节点
        # 定义g节点
        g = c.rchild
        # s1,s4 不会动， 只有 g的两个节点 归属 会发生变化(s2,s3)
        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新 Balance Factor
        # 最后的bf与 key 插在 g 中哪个节点有关系
        if g.bf < 0:  # ie. 即g.bf=-1 插在了s2 左边沉
            p.bf = 1  # 右左边沉 s3（h-1）<s4（h）
            c.bf = 0
        elif g.bf > 0:  # 插在了s2
            p.bf = 0
            c.bf = -1
        else:  # 特殊情况  s1~s4 全为 None   --- 插的是 g 节点自己
            p.bf = 0
            c.bf = 0
        g.bf = 0  # 最后g 平衡


    # 子类的插入 -- 把父类覆盖
    def insert_No_recur(self,value):
        pass