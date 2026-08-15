# CodeChef: Snake Procession (SNAKPROC)
# https://www.codechef.com/problems/SNAKPROC
t = int(input())
for _ in range(t):
    l = int(input())
    s = input().strip()
    inside = False
    valid = True
    for c in s:
        if c == 'H':
            if inside:
                valid = False
                break
            inside = True
        elif c == 'T':
            if not inside:
                valid = False
                break
            inside = False
    if inside:
        valid = False
    print("Valid" if valid else "Invalid")
