class QuickFind(object):
    # class variable
    def __init__(self,N=None): #N-size array/list
        self.arr=list(range(N)) #obj variable

    def qf_find(self,p,q):  # external input for querry
        return (self.arr[p] == self.arr[q])

    def qf_union(self,p,q):
        p_value=self.arr[p]
        q_value=self.arr[q]
        for i in range(len(self.arr)):
            if (self.arr[i]==p_value): self.arr[i]=q_value   #Find all values equal to p and Update to q_value

    def qf_show(self):
        print(self.arr)
qf=QuickFind(10)
qf.qf_show()
print(qf.qf_find(1,3))
print(qf.qf_union(1,3))
print(qf.qf_find(1,3))
qf.qf_show()