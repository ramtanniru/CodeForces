def solve():
    n,x = map(int,input().split())
    arr = [int(i) for i in input().split()]

    def isPossibble(n):
        prev = 0
        for gasStations in arr:
            if n<gasStations-prev:
                return False
            prev = gasStations
        return n>=2*(x-prev)

    l,r = 0,2*x
    ans = -1
    while l<=r:
        mid = (l+r)//2
        if isPossibble(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    print(ans)

for _ in range(int(input())):
    solve()