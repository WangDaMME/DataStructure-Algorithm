'''动态规划 DP'''
# DP 思想 = 递推式（最优子结构） + 重复子问题

# 递归方法下的递归 ---》子问题的重复计算 Repeat calculation of Subproblems
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

#fib(100)
'''
fib(100) -- 很慢 是因为
fib(6)=fib(5)+fib(4)
fib(5)=fib(4)+fib(3)
fib(4)=fib(3)+fib(2)
fib(3)=fib(2)+fib(1)
fib(6), fib(5)都需要用到fib(4)--fib(4)都需要用到fib(3) --重复计算了很多遍
'''

#非递归方法 避免了子问题的重复计算
# 算好的子结果  都 存到了列表里
def fib_no_recur(n):
    f=[0,1,1]  #加个0 让下标相等
    if n>2:
        for i in range(n-2):   # n-2次 ie. 第三位 fib(3) 需要算一次  fib(4）需要先算fib(3)-->再算fib(4) 两次
            num=f[-1]+f[-2] #最后一项和倒数第二项
            f.append(num)
    return f[n]

print(fib_no_recur(100))
