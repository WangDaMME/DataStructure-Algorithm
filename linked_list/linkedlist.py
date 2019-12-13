# 节点类
class Node(object):
    def __init__(self, value=None, next=None):   # 两个值value,next
        self.value, self.next= value, next

# 链表类
class Linkedlist(object):
    # data
    def __init__(self,maxsize=None):   # 最大容量
        self.root=Node()   # 是一个节点实例
        self.maxsize=maxsize
        self.length=0  #长度为0
        self.tailnode=None

    # method
    def __len__(self):
        return self.length

    def append(self,value):
        if self.maxsize is not None and len(self)>self.maxsize:
            raise Exception('the linked list is full')
        new_node=Node(value)   # 传入 一个 5,67...让它变成node 串进来
        tailnode=self.tailnode  # 取一下当前的tailnode
        if tailnode is None:
            self.root.next=new_node
        else:
            tailnode.next =new_node
        # Update new tail
        self.tailnode=new_node
        self.length+=1

    def leftappend(self,value):
        headnode=self.root.next #头结点 下一个节点
        new_node=Node(value)
        self.root.next=new_node
        new_node.next=headnode
        self.length+=1

    def iter_node(self):   #遍历
        current_node=self.root.next
        while current_node is not self.tailnode:
            yield current_node
            current_node=current_node.next  #更新节点
        yield current_node  # 遍历 到 最后tailnode 的节点

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self,value):   #O(n)
        prev_node=self.root
        curr_node=self.root.next
        for curr_node in self.iter_node():
            if curr_node.value==value:
                prev_node.next=curr_node.next  # 之前节点尾元素 指向下一个
                #删除的是尾节点
                if curr_node is self.tailnode:
                    self.tailnode=prev_node   #更新 尾节点 为 之前的节点
                del curr_node
                self.length-=1
                return 1 #表明删除成功
            else:
                prev_node=curr_node
        return -1  #删除失败

    def find(self,value):  # O(n)
        index=0
        for node in self.iter_node():
            if node.value == value:
                return index
            index+=1
        return -1  # 如果没有找到， 返回-1 作为标识

    def popleft(self):  # O(1)
        if self.root.next is None:
            raise Exception('Pop from empty linked list')
        headnode = self.root.next
        self.root.next=headnode.next
        value=headnode.value
        self.length-=1
        del headnode
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.length=0
        self.root.next=None
