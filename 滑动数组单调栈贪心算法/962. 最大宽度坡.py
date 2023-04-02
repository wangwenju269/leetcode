'''
arr = [6,0,8,2,1,5]
return 4
'''
def process(arr):
    temp = [(i,num) for i ,num in enumerate(arr)]
    temp.sort(key = lambda x:x[1])
    res = [x for x,y in temp]
    n = len(res)
    alongmax = 0
    amin = res[0]
    for i in range(1,n):
        if res[i] > amin:
           alongmax = max(alongmax,res[i] -amin)
        else:
           amin = res[i]
    return alongmax


arr = [6,0,8,2,1,5]
print(process(arr))