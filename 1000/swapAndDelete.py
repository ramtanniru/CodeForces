from collections import Counter
def solve():
    s = input()
    mp = Counter(s)
    t = ""
    for i in s:
        key = str(int(i)^1)
        if mp[key]:
            t += key
            mp[key] -= 1
        else:
            break
    print(len(s)-len(t))

for _ in range(int(input())):
    solve()
