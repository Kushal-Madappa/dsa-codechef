# CodeChef: Mahasena (AMR15A)
# https://www.codechef.com/problems/AMR15A

n = int(input())
arr = list(map(int, input().split()))
evens = sum(1 for x in arr if x % 2 == 0)
print("READY FOR BATTLE" if evens > n - evens else "NOT READY")
