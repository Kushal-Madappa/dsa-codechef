# CodeChef: Racing Horses (HORSES)
# https://www.codechef.com/problems/HORSES

t = int(input())
for _ in range(t):
    n = int(input())
    s = sorted(map(int, input().split()))
    print(min(s[i+1] - s[i] for i in range(n-1)))
