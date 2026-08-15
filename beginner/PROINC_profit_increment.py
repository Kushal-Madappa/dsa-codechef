# CodeChef: Profit Increment (PROINC)
# https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PROINC
for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y + x // 10)
