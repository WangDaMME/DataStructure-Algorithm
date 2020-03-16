# 栈 和 队列的实际问题
# === 栈  DFS 深度原先/回溯法 =====
# 规定搜索方向： 上右下左：一条到走到底，遇到没路可走，往回返，直到有其他岔路的点 （回溯：也就是 有路压栈，没路 出栈）--最后得的结果： 就是找到一条能走的路
# ！只是能找到路 但是 不是 optimized
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

def Seek_Path(x1,y1,x2,y2): # (x1,y1)：起点 (x2,y2):终点
  stack=[] # 栈可以用队列建立
  stack.append((x1,y1))  # 坐标，按tuple存
  maze[x1][y1]=2  # 已经遍历过了  2 表示遍历

  # 当 栈不为空时 搜索
  dirs=[
    lambda x,y: (x,y-1),  # 上
    lambda x,y: (x+1,y),  # 右
    lambda x,y: (x,y+1),  # 下
    lambda x,y: (x-1,y),  # 左
  ]
  while(len(stack)>0):
    curnode= stack[-1]
    # 最后找到 终点
    if curnode[0]==x2 and curnode[1]==y2:
      print("There exists a path: ")
      for node in stack:
        print(node)
      return True
    # 把下一个节点append 到列表
    for direction in dirs:
      next_node=direction(curnode[0],curnode[1])
      if maze[next_node[0]][next_node[1]]==0:  #maze中该点可以走
        stack.append(next_node)
        maze[next_node[0]][next_node[1]]=2  # 改为已经访问过
        break
    else:
      maze[next_node[0]][next_node[1]]=2  # 也要改为已访问过
      stack.pop()

  else:
    print("No Path exists!")
    return False


Seek_Path(1,1,8,8)