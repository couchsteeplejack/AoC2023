with open('input2.txt') as f:
    times = [int(i) for i in f.readline().split()[1:]]
    dists = [int(i) for i in f.readline().split()[1:]]

wins = []

for i in range(len(times)):
    t, d = times[i], dists[i]
    winning = 0
    for s in range(1, t):
        if s*(t-s) > d:
            winning += 1
    wins.append(winning)

print(wins)

acc = 1
for i in wins:
    acc = acc*i

print(acc)