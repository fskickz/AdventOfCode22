reinsdyr = []
with open('calories.txt', 'r') as f:
    total = 0
    for line in f:
        line = line.strip().split()
        if len(line) == 0 or line == '':
            reinsdyr.append(total)
            total = 0
            continue
        total += int(line[0])

X = [x for x in f.read().split('\n\n') f = open('calories.txt')]
total = max(sum(int(i) for i in x.split()) for x in X)
liste = [x.split() for x in X]
print(liste)
print(total)
for elf in ('\n'.join(X)).split('\n\n'):
    total = 0
    for line in elf.split('\n'):
        total += int(line)
print(total)

print(total)
reinsdyr.sort(reverse=True)
total = reinsdyr[0] + reinsdyr[1] + reinsdyr[2]
print(total)
