# CodeChef: Chef and Steps (CHEFSTEP)
# https://www.codechef.com/problems/CHEFSTEP
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(''.join('1' if x % k == 0 else '0' for x in arr))
