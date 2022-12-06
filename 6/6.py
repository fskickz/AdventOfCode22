line = ''.join([l.strip() for l in open('6/input.txt')])

# Part 1
for i, _ in enumerate(line):
    unique = set(line[i - 4: i])
    if len(unique) == 4:
        print(i)
        break

# Part 2
for i, _ in enumerate(line):
    unique = set(line[i - 14: i])
    if len(unique) == 14:
        print(i)
        break
