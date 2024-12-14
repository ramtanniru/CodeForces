def solve():
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    newArr = [(x%k,i) if x%k else (k,i) for i,x in enumerate(arr)]
    util = sorted(newArr,key = lambda x:(-x[0],x[1]))
    res = [x[1]+1 for x in util]
    return res
for _ in range(int(input())):
    print(*solve())