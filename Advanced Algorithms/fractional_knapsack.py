goods=[(60,10),(100,20),(120,30)]
goods.sort(key=lambda x: x[0]/x[1],reverse=True) #按key排

def Fractional_Knapsack(goods,W_limit):
    res=[0 for _ in range(len(goods))]  # 每类拿多少
    total_value=0   # 最后拿的总价值
    for idx, (price,weight) in enumerate(goods):
        #res[idx]=1 if W_limit>= weight else weight/W_limit
        # 包每满 就全拿走 满了 再拿别的
        if weight<=W_limit:
            res[idx]=1
            # 更新 那完 额外 空间,, 更新拿走的值
            total_value+=price
            W_limit-=weight
        else:  #没有拿走一部分，能拿多少拿多少 将包塞满
            res[idx]=W_limit/weight  #剩的 / 这份有的总量
            total_value+=(W_limit/weight)*price
            W_limit=0  # 没东西 可以break了
            break
    return res,total_value

print(Fractional_Knapsack(goods,50))