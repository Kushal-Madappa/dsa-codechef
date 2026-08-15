# CodeChef: Problems in your to-do list (TODOLIST)
# https://www.codechef.com/problems/TODOLIST
t = int(input())
for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))
    print(sum(1 for x in d if x >= 1000))
