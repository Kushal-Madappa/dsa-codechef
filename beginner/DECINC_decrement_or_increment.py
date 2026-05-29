# CodeChef: Decrement OR Increment (DECINC)
# https://www.codechef.com/problems/DECINC
n = int(input())
print(n + 1 if n % 4 == 0 else n - 1)
