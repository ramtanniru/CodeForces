def solve():
    n, k = map(int, input().split())
    a = [int(i) for i in input().split()]

    if k == 1:
        is_sorted = all(a[i] <= a[i+1] for i in range(n-1))
        if is_sorted:
            print("YES")
        else:
            print("NO")
        return
    print("YES")
    
t = int(input())
for _ in range(t):
    solve()