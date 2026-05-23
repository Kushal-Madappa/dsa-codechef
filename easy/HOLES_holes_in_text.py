# CodeChef: Holes in the text (HOLES)
# https://www.codechef.com/problems/HOLES
H = {'A': 1, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1, 'B': 2}
t = int(input())
for _ in range(t):
    s = input()
    print(sum(H.get(c, 0) for c in s))
