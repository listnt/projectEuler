def all_joins(arr):
    if not arr:
        return [[]] 

    result = []
    for i in range(1, len(arr)+1):
        joined = ''.join(map(str, arr[:i]))
        for rest in all_joins(arr[i:]):
            result.append([joined] + rest)
    return result

def add(x,y):
    return int(x)+int(y)

def mult(x,y):
    return int(x)*int(y)

def sub(x,y):
    return int(x)-int(y)

def div(x,y):
    return int(x)/int(y)

arr=[1,2,3,4,5,6,7,8,9]
ops = [add,mult,sub,div]

joins = all_joins(arr)
joins = [join for join in joins if len(join) > 1]
