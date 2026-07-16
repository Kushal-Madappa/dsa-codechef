# CodeChef: Magic Set (MGCSET)
# https://www.codechef.com/problems/MGCSET
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    k = sum(1 for x in a if x % m == 0)
    print(2**k - 1)
