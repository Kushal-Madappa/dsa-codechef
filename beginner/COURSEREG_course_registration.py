# CodeChef: Course Registration (COURSEREG)
# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/COURSEREG
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    print("Yes" if m - k >= n else "No")
