class QuickUnion(object):
    def __init__(self,N):
        self.arr=list(range(N)) #N-size array/list [int]

    def qu_root(self,value):
        while(value!=self.arr[value]):  #根存的 是自己 = 自己
            value=self.arr[value]  #向上看 一层
        return value # 找到return根

    def qu_find(self,p,q):
        #看根想不想等
        q_root=self.qu_root(q)
        p_root=self.qu_root(p)
        return (q_root == p_root)  #boolean

    def qu_union(self,p,q):
        p_root=self.qu_root(p)
        q_root=self.qu_root(q)
        self.arr[p_root]=q_root  #改p的根节点 = q的根节点

    def qu_show(self):
        print(self.arr)

print('=====Quick Union=====')
qu=QuickUnion(10)
qu.qu_show()
print(qu.qu_find(1,3))
qu.qu_union(1,3)
print(qu.qu_find(1,3))
qu.qu_union(8,3)
qu.qu_union(5,8)
qu.qu_union(5,2)
print(qu.qu_find(1,2))
print(qu.qu_root(1))
print(qu.qu_root(2))
