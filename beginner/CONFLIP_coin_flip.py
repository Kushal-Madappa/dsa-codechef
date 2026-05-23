# CodeChef: Coin Flip (CONFLIP)
# https://www.codechef.com/problems/CONFLIP
t = int(input())
for _ in range(t):
    g = int(input())
    for _ in range(g):
        i, n, q = map(int, input().split())
        # Coin k is flipped (N - k + 1) times. Even flips -> initial face,
        # odd flips -> opposite. Even-flip count = N // 2.
        same = n // 2
        opp = n - same
        print(same if i == q else opp)
