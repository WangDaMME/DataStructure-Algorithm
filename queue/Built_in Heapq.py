import heapq
# heapq 可以实现 优先队列 priority queue
# ie. 队列中大的 先出or 小的先出

import random
lst=list(range(20))
random.shuffle(lst)
print(lst)

heapq.heapify(lst) # 建堆
print('Consturcted Heapify',lst)  #小根堆

heapq.heappush(lst,22)  # 添加元素
for i in range(5):
  print(heapq.heappop(lst))

print('======================')
for i in range(len(lst)):
  print(heapq.heappop(lst))