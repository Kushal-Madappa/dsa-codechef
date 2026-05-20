# CodeChef: Primality Test (PRB01)
# https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PRB01

def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    print("yes" if is_prime(n) else "no")
