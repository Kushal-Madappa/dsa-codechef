# CodeChef: Devu and friendship testing (CFRTEST)
# https://www.codechef.com/problems/CFRTEST
t = int(input())
for _ in range(t):
    n = int(input())
    days = input().split()
    print(len(set(days)))
