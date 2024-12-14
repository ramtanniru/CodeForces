from collections import defaultdict
def solve():
    n,k = map(int,input().split())
    arr = [int(i) for i in input().split()]
    ans = float('inf')
    if k==4:
        mp = defaultdict(int)
        for i in arr:
            if i%2==0:
                mp['even'] += 1
            else:
                mp['odd'] += 1
        if mp['even']>=2:
            return 0
        elif mp['odd']>0 and mp['even']>0:
            ans = min(ans,1)
        elif mp['odd']>=2:
            ans = min(ans,2)
    for i in arr:
        if i%k==0:
            return 0
        else:
            ans = min(ans,k-(i%k))
    return ans

for _ in range(int(input())):
    print(solve())
