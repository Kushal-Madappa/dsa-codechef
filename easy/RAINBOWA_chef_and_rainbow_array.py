# CodeChef: Chef and Rainbow Array (RAINBOWA)
# https://www.codechef.com/problems/RAINBOWA
def is_rainbow(a):
    n = len(a)
    if n < 13:
        return False
    if not all(1 <= x <= 7 for x in a):
        return False
    i, j = 0, n - 1
    for v in range(1, 7):
        cl = 0
        while i <= j and a[i] == v:
            i += 1; cl += 1
        cr = 0
        while j >= i and a[j] == v:
            j -= 1; cr += 1
        if cl == 0 or cl != cr:
            return False
    cnt7 = 0
    while i <= j:
        if a[i] != 7:
            return False
        i += 1; cnt7 += 1
    return cnt7 >= 1

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("yes" if is_rainbow(a) else "no")
