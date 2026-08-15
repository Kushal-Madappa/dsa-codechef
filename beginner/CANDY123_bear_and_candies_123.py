# CodeChef: Bear and Candies 123 (CANDY123)
# https://www.codechef.com/problems/CANDY123
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    limak, bob, turn = 0, 0, 1
    while True:
        if turn % 2 == 1:
            if limak + turn > a:
                print("Bob"); break
            limak += turn
        else:
            if bob + turn > b:
                print("Limak"); break
            bob += turn
        turn += 1
