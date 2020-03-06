import random
from helper import *

lst1=[random.randint(0,10) for i in range(0,10)]
lst2=[random.randint(0,1000) for i in range(0,1000)]


'''--------- Searching ------------'''
# 1. Linear Search O(n)
@cal_time
def Linear_Search1(lst,val):    #slowest, has the process for decompostion of list
    for idx, value in enumerate(lst):
        if val is value:
            return idx
    return -1

@cal_time
def Linear_Search2(lst,val):
    for idx in range(len(lst)):
        if lst[idx] is val:
            return idx
    return -1
'''
arr=range(0,9)
print(Linear_Search2(arr,5))
print(Linear_Search2(arr,10))
'''


# 2. Binary Search O(log2n)  # Amazing -- !Need to be sorted list
@cal_time
def Binary_Search(sorted_lst,val):
    left=0
    right=len(sorted_lst)-1
    while (left<=right): #!!!Caution Equal!!!
        mid = (left+right)//2 # quotient
        if val == mid:
            return mid
        elif sorted_lst[mid]> val:
            right=mid-1
        else:
            left=mid+1
    else:
        return -1

#print(Binary_Search(arr,5))

print("Linear 1 : ", Linear_Search1(lst2,500))  #slowest
print("Linear 2 : ", Linear_Search2(lst2,500))
print("Binary : ", Binary_Search(lst2,500))



'''--------- Sorting ------------'''
# 2.1 Low Quality [3]
# 2.1 Bubble Sort
@cal_time
def Bubble_Sort(lst):
    for i in range(0,len(lst)-1): #Bubblr epoch only 0~n-1 times, last time drop automatically
        for j in range(0,len(lst)-1-i): # len(lst)-1  the right index - j
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
#print(Bubble_Sort(lst2))
#Improved


# 2.2 Selection Sort
''' Select the Min. from the list every time '''
'''
# 2.2.A Lowest  - Take Double Space,Not in-place sort O(N^2)
def Selection_Sort(lst):
    new_lst=[]
    for i in range(0,len(lst)):
        min_value=min(lst)
        new_lst.append(min_value)
        lst.remove(min_value)
    return new_lst
'''

# 2.2.B In-Place Selection Sort
@cal_time
def Selection_Sort(lst):
# 分有序区，无序区  有序子在前， 在无序区里找最小 和当前的i 换位置
    for i in range(0,len(lst)-1):  # like Bubble Sort, n-1 times
        min_loc = i  # Begining, assume 1st place minimum
        for j in range(i+1,len(lst)): # i 是自己， i+1下一位开始
            if lst[j]<lst[min_loc]:
                min_loc=j            # 更新最小的 min_loc
        lst[min_loc],lst[i]=lst[i],lst[min_loc]
    return lst

#print(Selection_Sort(lst2))

# 2.3 Insertion_Sort
def InsertionSort(lst):
    for i in range(1,len(lst)):  # 拿一张牌
        temp=lst[i]  # 拿这个牌 看它前面有序区比较，看插在哪
        j=i-1 # 剩的有序区的牌, 有序区域最大值 从右往左看
        while lst[j]>temp and j>=0:  # 比 lst[i]牌大的都往后挪
            lst[j+1]=lst[j] # 往后串 直到 发现比他小的
            j-=1
        lst[j+1]=temp   # 写回差到j+1下一位
    return lst

# 2.B 牛逼三人组：快速，堆排序， 归并
# 时间复杂度： N*Log(N) 【一般】   -- 最坏情况 碰到 倒叙列表: N^2
'''
# 思想：扔进一个数，归到自己应在的位置， 让左边都比 它小 右边都比它大，
# 整个列表 不停左右拆分，直达 left<right ie.有两个or两个以上的数，--》明确的递归条件
# 想象左坑  有坑的关系
'''
def Partition(lst,left,right):
    temp=lst[left]  # 刚开始，从左边拿第一个数, （temp赋值相当于拿了，你要动left了）
    while left< right: # 左坑标 ！=又坑标
        # 右坑里挑小的 扔左边，碰到小的--跳出循环
        while left<right and lst[right]>=temp:  # 咋有坑找 一个 小于 现有左坑的
                                 # 有一种情况， 右边全比左边大，找回自己了，想让它跳出循环 不想让他再减了 -- left<right再检测一下
            right-=1
        lst[left]=lst[right]
        # 左坑里挑大的 扔右边  碰到大的--跳出循环
        while lst[left]<=temp and left<right:  # left<right 监测，防止 右边一个小的没有
            left+=1
        lst[right]=lst[left]  # 左坑扔到右坑
    lst[left]=temp  #结束left<right 实际 left和right 重叠，这个坑写谁都行  -- 【temp 归位置】
    return left

def _QuickSort(lst,left,right):
    if left< right: #递归条件  left = right ie. 一个 < : 之上2个以上开始排
        mid=Partition(lst,left,right)
        _QuickSort(lst,left,mid-1)   # 左边 排序
        _QuickSort(lst,mid+1,right)  # 右边 排序

import sys
sys.setrecursionlimit(1000000)

# 装饰器 不能加在递归函数，会打印很多次 -- 【加个马甲，再调用】
@cal_time
def QuickSort(lst,left,right):
    _QuickSort(lst,left,right)

'''
#lst11=[5,7,4,6,3,1,2,9,8]
arr1=list(range(10000))
random.shuffle(arr1)
QuickSort(arr1,0,len(arr1)-1)
Bubble_Sort(arr1)
#print(arr1)
'''

# 2.B.3 牛逼三人组：快速，堆排序， 归并
# 归并排序 Merge Sort
'''
# 归并
'''
def _merge(lst,low,mid,high):  # 不从0 开始--是因为后面有递归
    lst_temp=[]
    i=low
    j=mid+1
    while i<=mid and j<=high:
        if lst[i]<lst[j]:
            lst_temp.append(lst[i])
            i+=1
        else:
            lst_temp.append(lst[j])
            j+=1
    # while 执行完， i or j 肯定有一个走到最后的 说明后面的 是有序的 789 再append 进这里面
    while i<=mid:   # 若 i 没走到最后
        lst_temp.append(lst[i])
        i+=1
    while j<=high:
        lst_temp.append(lst[j])
        j+=1
    #把 ltemp 的 值写回lst 切片(顾头不顾尾) -- 不用for 循环依次赋值了
    lst[low:high+1]=lst_temp

'''
# arr3 前后两个都有序
arr3=[2,4,5,7,1,3,6,8]
_merge(arr3,0,(len(arr3)-1)//2,7)
print(arr3)
'''
def MergeSort(lst,low,high):
    if low<high:  # 两个以上的元素 归并
        mid=(low+high)//2
        MergeSort(lst,low,mid)
        MergeSort(lst,mid+1,high)
        _merge(lst,low,mid,high)

arr4=list(range(0,100))
random.shuffle(arr4)
MergeSort(arr4,0,len(arr4)-1)
print(arr4)


# 2.B.3 牛逼三人组：堆排序Heap Sort
# 堆排序 Heap Sort (向下调整函数 + 1. 依次出数)
def sift(lst, low,high):
    # low: 根顶
    # high：根底 最后的叶子节点
    # 假设堆已经建成
    temp=lst[low] # 拿出来 堆顶 看放哪
    i=low      # 从堆顶开始
    j=2*i+1    # i根节点下的左孩子节点
    while j<=high:
        if j+1<=high and lst[j]<lst[j+1]:  # 有  右孩子节点  并且 右孩子比较大
            j=j+1
        if lst[j]>temp:
            lst[i]=lst[j]    # 把下面孩子节点 顶上来
            i=j              # 再往下看
            j=2*i+1
        else:                # temp>lst[j] 因为 堆 下面是有序 放在这就行
            lst[i]=temp      # 把 temp 放到某一级领导位置
            break
    else:
        lst[i]=temp         #  i 走到最后一层，j 再 最后一层的下一层，不会进循环，  还要把temp放到 最后看的那层，
                            # 把 temp 放到叶子节点上


def HeapSort(lst, low, high):
    #1，建立堆
        # 从叶子节点的 父节点开始调整  --【农村包围撑死】
    n=len(lst)
    for i in range(n//2-1,-1,-1):  # 子节点 找父节点 （i-1）//2 末尾 是n-1
        # i 是 当前根的下标
        sift(lst,i,n//2-1)         # high: 不管 i是几 都指整个堆的尾元素
                                   # [要点]： High 的作用是 比较 j 别超了high, 若超了high 就是最后一层,, 7的孩子 肯定不会 跑到 同级左孩子堆里， (这些都小些)
    #2. 得到堆顶元素,堆顶与最后一个元素交换
    for i in range(n-1,-1,-1):   # 让i指向当前堆的最后一个元素, 需要调整n-1次
        lst[0],lst[i]=lst[i],lst[0]  # lst[0]: 堆顶
        sift(lst,0,  i-1)    #当 前面交换完  9 下来  3 上去， 此时i 还没变，还是 指向原来3的位置，所以要调整只要 调整 high 位置i-1,i 的位置由 下来的9 补


