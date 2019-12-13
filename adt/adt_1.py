class Bag(object):
    def __init__(self,maxsize=10):  #init
        self.maxsize=maxsize
        self._items=list()   # array
    def add(self,item):
        if len(self)>self.maxsize:
            raise Exception('Bag is Full')    # 抛出异常
        self._items.append(item)
    def remove(self,item):
        self._items.remove(item)
    def __len__(self):
        return len(self._items)
    def __iter__(self):    # 定义迭代器
        for item in self._items:
            yield item   # 迭代


def Test_bag():
    bag=Bag()   #创建对象

    bag.add(1)
    bag.add(2)
    bag.add(3)

    assert len(bag)==3  # 断定为3，不是3 就会出错

    bag.remove(2)
    assert len(bag)==2  # 断定只有两个元素

    for i in bag:
        print(i)

Test_bag()