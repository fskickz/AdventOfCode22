X = [r.strip() for r in open('4/input.txt')]
p1 = 0
p2 = 0
for x in X:
    f, s = x.split(',')
    f = f.split('-')
    s = s.split('-')
    first = [i for i in range(int(f[0]), int(f[-1])+1)]
    second = [i for i in range(int(s[0]), int(s[-1])+1)]
    # Part 1
    if all([i in first for i in second]) or all([i in second for i in first]):
        p1 += 1
    # Part 2
    if any([i in first for i in second]) or any([i in second for i in first]):
        p2 += 1

print(p1)
print(p2)
