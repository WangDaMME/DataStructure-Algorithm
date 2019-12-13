#import linkedlist as ll
class Node(object):
    def __init__(self,value=None,next=None):  #默认为None
        self.value=value
        self.next=next

class LinkedList(object):
    def __init__(self,maxsize=None):
        self.maxsize=maxsize
        self.root=Node()
        self.length=0
        self.tailnode=None  #可能没有

    # method
    def __len__(self):
        return self.length
    def append(self,value):
        if self.maxsize is not None and len(self)>=self.maxsize:
            raise Exception("Linked List is full!")
        new_node=Node(value)
        if self.tailnode is None:
            self.root.next=new_node
        else:
            self.tailnode.next = new_node
        #更新尾 -- 不管咋的，尾节点都是new_node
        self.tailnode=new_node
        self.length+=1

    def popleft(self):
        if self.root is self.root.next:  #Empty
            raise Exception('Empty List!')
        head_node=self.root.next # gonna delete
        self.root.next=head_node.next
        value = head_node.value
        del head_node
        self.length-=1
        return value

    def iter_node(self):
        cur_node=self.root.next
        while cur_node is not self.tailnode:
            yield cur_node
            cure_node=cur_node.next
        yield cur_node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

class EmptyError(Exception):
    pass

class Queue(object):
    def __init__(self,q_maxsize=None):
        self.q_maxsize=q_maxsize
        self.q_linked_list = LinkedList()   # 初始化一个linkedlist

    #method
    def __len__(self):
        return len(self.q_linked_list)

    def Push(self,value):
        if self.q_maxsize is not None and len(self)>=self.q_maxsize:
            raise Exception("Queue is full, No more space!")
        return self.q_linked_list.append(value)

    def Pop(self):
        if len(self)<=0:   #empty
            raise EmptyError('The queue is empty!')
        return self.q_linked_list.popleft()

# Single Test
def test_queue():
    q=Queue()

    q.Push(1)
    q.Push(2)
    q.Push(3)
    assert len(q) is 3

    assert q.Pop() is 1
    assert q.Pop() is 2
    assert q.Pop() is 3

    import pytest
    with pytest.raises(EmptyError) as excinfo:
        q.Pop() # raise Empty Error
    assert 'empty' in str(excinfo.value)

test_queue()