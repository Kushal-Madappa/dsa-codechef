# CodeChef: Closing the Tweets (TWTCLOSE)
# https://www.codechef.com/problems/TWTCLOSE
n, k = map(int, input().split())
open_set = set()
for _ in range(k):
    line = input().split()
    if line[0] == 'CLOSEALL':
        open_set.clear()
    else:
        x = int(line[1])
        if x in open_set:
            open_set.remove(x)
        else:
            open_set.add(x)
    print(len(open_set))
