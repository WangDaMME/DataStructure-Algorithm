
# === 队列  BFS 广度优先 =====
# 规定搜索方向： 上右下左：遇到分岔路，寻找接下来所有可能的路
from collections import deque

maze=[
   [1,1,1,1,1,1,1,1,1,1],
   [1,0,0,1,0,0,0,1,0,1],
   [1,0,0,1,0,0,0,1,0,1],
   [1,0,0,0,0,1,1,0,0,1],
   [1,0,1,1,1,0,0,0,0,1],
   [1,0,0,0,1,0,0,0,0,1],
   [1,0,1,0,0,0,1,0,0,1],
   [1,0,1,1,1,0,1,1,0,1],
   [1,1,0,0,0,0,0,0,0,1],
   [1,1,1,1,1,1,1,1,1,1]
]

dirs=[
   lambda x,y: (x,y-1),  # 上
   lambda x,y: (x+1,y),  # 右
   lambda x,y: (x,y+1),  # 下
   lambda x,y: (x-1,y),  # 左
 ]

#在一个path里挑选打印
def FPrint_path(path):
  curnode=path[-1]
  real_path=[]
  ''' 打不到(1,1)起点
  while curnode[2]!=-1:    # curnode 节点为-1 就是 到了 起点 x1,y1领进门的-1
    real_path.append(curnode[0:2]) #前包后不包，只挑出坐标存一下
    curnode=path[curnode[2]]  # 更新为 谁领进来的
  # 反转一下
  #real_path.append((x1,y1))
  '''
  i=len(path)-1
  while i>=0:
    real_path.append(path[i][0:2])  # (x,y)坐标
    i=path[i][2]   # parent node

  real_path.reverse()
  for node in real_path:
    print(node) 

def BFS_SeekPath(x1,y1,x2,y2):
  queue=deque()
  queue.append((x1,y1,-1))  # rear进队，-1：parent node 谁带他进来的
  maze[x1][y1]=2 # 该点已经遍历过
  path=[]
  while (len(queue)>0):
    curnode=queue.popleft()  # 队首出队 (pop 为 右侧队尾出队)
    path.append(curnode)
    # 找到了终点
    if curnode[0]==x2 and curnode[1]==y2:
      print('The path is found!')
      FPrint_path(path)
      return True
  

    for direction in dirs:
      nextnode=direction(curnode[0],curnode[1])
      if maze[nextnode[0]][nextnode[1]]==0:
        queue.append((nextnode[0],nextnode[1],len(path)-1))  # len(path)-1 当前谁领他进来的
        maze[nextnode[0]][nextnode[1]]=2  # 该点已经遍历
      
  else:
    print('No path exists!')
    return False

BFS_SeekPath(1,1,8,8)