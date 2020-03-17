class Node(object):
    def __init__(self,item):
        self.item = item
        self.next=None


a=Node(1)
b=Node(2)
c=Node(3)

a.next=b
b.next=c

print(a.next.item)
print(a.next.next.item)

# 创建链表 2 种方法
# 1. 头插法  只需要知道头
def Creat_LinkedList_Front(lst):
    head=Node(lst[0])
    for element in lst[1:]:  # 从1 到最后
        node=Node(element)    #创建node
        node.next=head
        head=node
    return head


def Creat_LinkedList_Tail(lst):
    head=Node(lst[0])
    tail=head
    for element in lst[1:]:  # 从1 到最后
        node=Node(element)    #创建node
        tail.next=node      # 连接节点
        tail=node         # 更新tail
    return head

def Travese(linked_list):   # 进来为return的头结点
    while linked_list:  #链表不为空
        print(linked_list.item, end=',')
        linked_list=linked_list.next

print('===========头插法===========')
lk_front=Creat_LinkedList_Front([1,2,3])
Travese(lk_front)

print('\n')
print('===========尾插法===========')
lk_Tail=Creat_LinkedList_Tail([1,2,3])
Travese(lk_Tail)

