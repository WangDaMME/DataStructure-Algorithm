import random

# 小根堆 Small Root Heap

def sift(li,low,high): #li是指列表，low是指根节点位置，high是指最后一个元素位置
    i=low    #最开始跟节点的位置
    j=2*i+1  #左边下一层孩子节点
    tmp=li[low]  #把堆顶元素存下来
    while j<=high:  #只要j位置有节点，有数字便可以一直循环
        if j+1<=high and li[j+1]<li[j]:  #右边孩子有并且右边更大
            j=j+1   #把j指向j+1，右边孩子大于左边，指向右边
        if li[j]<tmp:
            li[i]=li[j]
            i=j       #往下看一层
            j=2*j+1
        else:  #tmp更大的情况，把tmp放上来
            li[i]=tmp   #把tmp放到某一级领导的位置上
            break
    else:
        li[i]=tmp      #把tmp放在叶子节点上去



def topk(lst,k):
  #1. 取前k 个元素 建立 小根堆
  heap=lst[0:k]
  for i in range((k-1)//2,-1,-1):
    sift(heap,i,k-1)
  #2. 遍历 看是否有更大的元素 可以进堆
  for i in range(k,len(lst)):
      if lst[i]>heap[0]:
        heap[0]=lst[i]
        sift(heap,0,k-1)

  # 输出
  for i in range(k-1,-1,-1):
    heap[0],heap[i]=heap[i],heap[0]
    sift(heap,0,i-1)

  return heap

lst_topk=list(range(20))
random.shuffle(lst_topk)
print(lst_topk)

print('Selecting Top K ... ')
lst_topk=topk(lst_topk,8)
print(lst_topk)