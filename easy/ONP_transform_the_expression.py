# CodeChef: Transform the Expression (ONP)
# https://www.codechef.com/problems/ONP
for _ in range(int(input())):
    out = []
    stack = []
    for ch in input():
        if ch.isalpha():
            out.append(ch)
        elif ch == '(':
            pass
        elif ch == ')':
            out.append(stack.pop())
        else:
            stack.append(ch)
    print(''.join(out))
