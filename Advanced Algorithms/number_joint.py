lst=[32,94,128,1286,6,71]

from functools import cmp_to_key
'''

def xy_cmp(x,y):
    if x+y<y+x:   # 1286x+128y <128+1286
        return 1  # 128+1286  不换
    if x+y> y+x:
        return -1
    else:
        return 0
def Num_joint(lst):
    str_lst=list(map(str,lst))  # 数字转成字符串
    str_lst.sort(key=cmp_to_key(xy_cmp))  # 按升序 比较 把两个比较的值 返回为key
    return "".join(str_lst)
'''

def Num_joint(lst):
    str_lst=list(map(str,lst))  # 数字转成字符串
    # 冒泡排序
    for i in range(len(str_lst)-1):
        for j in range(len(str_lst)-i-1):
            if str_lst[j]+str_lst[j+1]<str_lst[j+1]+str_lst[j]:
                str_lst[j],str_lst[j+1]=str_lst[j+1],str_lst[j]
    return "".join(str_lst)

print(Num_joint(lst))