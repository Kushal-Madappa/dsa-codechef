# CodeChef: Uncle Johny (JOHNY)
# https://www.codechef.com/problems/JOHNY
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    target = a[k - 1]
    print(sorted(a).index(target) + 1)
