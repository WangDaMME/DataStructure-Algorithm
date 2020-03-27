activities=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]  # si,fi:开始时间，结束时间
activities.sort(key=lambda x: x[1]) # 按结束时间排列

def Activities_Selection(activities):
  # 最先结束的活动 一定是 最优解的一部分
  res=[activities[0]]
  for i in range(1,len(activities)):
    # 不冲突 就添加到结果种
    # 不冲突： 活动开始时间  要 晚于 res最后一个活动中的结束时间
    if activities[i][0]>=res[-1][1]:
      res.append(activities[i])
  return res

print(Activities_Selection(activities))