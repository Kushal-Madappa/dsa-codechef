# CodeChef: Mutated Minions (CHN15A)
# https://www.codechef.com/problems/CHN15A
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for x in a if (x + k) % 7 == 0))
