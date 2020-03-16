import random
from helper import *

# 3. 其他排序方法
#1. Shell Sort 基于 insert插入排序-- 是分组的插入排序
def InsertionSort_Base(lst,gap):
    for i in range(gap,len(lst)):
        temp=lst[i]
        j=i-gap   # j 手里的牌的下标
        while temp<lst[j] and j>=0:  # i 从gap开始 , j=i-gap>=0
            lst[j+gap]=lst[j]
            j-=gap
        lst[j+gap]=temp

def ShellSort(lst):
    d=len(lst)//2 # distance of grouping 整除
    while d>=1:
        InsertionSort_Base(lst,d)
        d //=2  #整除等

#2.Counting Sort 计数排序
# 需要已知列表中的最大值
def Counting_Sort(lst,max_count=100): #默认max=100
    #生成一个全0列表
    count=[0 for _ in range(max_count+1)] # 前包后不包,  [exp in iteration]
    # count 是 从 0~max下标的列表，∴ 与lst 中元素对应
    # 找到一个 0+=1
    for element in lst:
        count[element]+=1
    lst.clear()  #列表清空
    for index,value in enumerate(count):
        for i in range(value):   # count中的value代表 有多少个该元素
            lst.append(index)

#3.Bucket Sort/Bin Sort 桶排序
def BucketSort(lst, n_buckets=100, max_count=1000):
    buckets = [[] for _ in range(n_buckets)]
    for element in lst:
        bucket_id = min(element // (max_count // n_buckets), n_buckets - 1)  # max_count//n_buckets 代表间隔
        # 取min
        # 10000 不会分到0~99 桶里，  取100 和 99 最小归纳到99桶里
        buckets[bucket_id].append(element)

        # 边防边排序
        for j in range(len(buckets[bucket_id]) - 1, 0, -1):
            # 该桶的前一位,append到后面了，能省则省， 倒着看-1 直到0位置
            if buckets[bucket_id][j - 1] > buckets[bucket_id][j]:
                buckets[bucket_id][j - 1], buckets[bucket_id][j] = buckets[bucket_id][j], buckets[bucket_id][j - 1]
            else:
                break

    # 每桶汇总
    bucket_tot_list = []
    for buc in buckets:
        bucket_tot_list.extend(buc)

    return bucket_tot_list


import random

lst1 = [random.randint(0, 1000) for _ in range(0, 1000)]
lst1 = BucketSort(lst1)
#print(lst1)


#4.Radix Sort 基数排序
def RadixSort(lst):
    max_num=max(lst)  # 最iteration 0-->1  888-->3  10000->5次
    it=0
    while 10**it<=max_num:
        buckets = [[] for _ in range(10)]  # 0~9 前包后不报
        for element in lst:
            id=(element//10**it)%10  # 个 --- 十位 --百千万
            buckets[id].append(element)
        #分桶完成，重新写会桶
        lst.clear()
        for buc in buckets:
            lst.extend(buc)
        it+=1

lst_radix=list(range(10001))
random.shuffle(lst_radix)
RadixSort(lst_radix)
print(lst_radix)

lst_Count=[random.randint(0,100) for _ in range(0,50)]
random.shuffle(lst_Count)
Counting_Sort(lst_Count)
print(lst_Count)