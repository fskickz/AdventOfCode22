with open('5/input.txt', 'r') as f:
    crates, instructions = f.read().split('\n\n')
    stacks = {}
    for line in crates.splitlines():
        for i, index in enumerate(range(1, len(line), 4)):
            if line[index].isdigit():
                continue
            if i+1 not in stacks:
                stacks[i+1] = list()
                stacks[i+1].append(line[index])
            else:
                stacks[i+1].append(line[index])

    for key in stacks:
        stacks[key].reverse()
        while ' ' in stacks[key]:
            stacks[key].remove(' ')

    for instruction in instructions.splitlines():
        amount, fromcrate, tocrate = [
            int(i) for i in instruction.split() if i.isdigit()]

        # part 2
        if amount > 1:
            temp = []
            for i in range(amount):
                temp.append(stacks[fromcrate].pop())
            for i in range(amount):
                stacks[tocrate].append(temp[-i-1])
        else:
            for i in range(amount):
                stacks[tocrate].append(stacks[fromcrate].pop())

        # part 1
        # for i in range(amount):
        #         stacks[tocrate].append(stacks[fromcrate].pop())


output = "".join(x[-1] for x in stacks.values())
print(output)
