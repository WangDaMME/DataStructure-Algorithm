# 1. 找零问题

currency=[100,50,20,10,5,2,1]

def Exchange_Money(Amount,currency):
    bills=[0 for i in range(len(currency))]
    for index, value in enumerate(currency):  #value 表示面值
        bills[index]=Amount//value
        Amount=Amount%value
    return bills, 'Remaining:'+str(Amount)

print(Exchange_Money(147.5,currency))