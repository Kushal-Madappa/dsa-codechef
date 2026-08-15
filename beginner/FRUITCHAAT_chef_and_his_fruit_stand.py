# CodeChef: Chef and His Fruit Stand (FRUITCHAAT)
# https://www.codechef.com/problems/FRUITCHAAT
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    print(min(x // 2, y))
