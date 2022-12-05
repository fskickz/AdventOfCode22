score = 0
for line in open('input.txt'):
    x = line.strip()
    f, s = x[:len(x)//2], x[len(x)//2:]
    for a in f:
        if a in s:
            if 'a' <= a <= 'z':
                score += ord(a) - ord('a') + 1
            else:
                score += ord(a) - ord('A') + 27
            break

print(score)

# part 2
score = 0
i = 0
X = [l.strip() for l in open('input.txt')]
while i < len(X):
    for a in X[i]:
        if a in X[i+1] and a in X[i+2]:
            if 'a' <= a <= 'z':
                score += ord(a) - ord('a') + 1
            else:
                score += ord(a) - ord('A') + 27
            break
    i += 3

print(score)
