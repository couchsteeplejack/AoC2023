import re

with open("input.txt") as f:
    route = f.readline().strip()
    whitespace = f.readline()
    network = {node: {"L": left, "R": right} for node, left, right in
               re.findall(r"(\w+).+\((\w+), (\w+)", f.read(), re.MULTILINE)}

cnt = 0
node = 'AAA'
while node != 'ZZZ':
    node = network[node][route[cnt%len(route)]]
    cnt += 1
print("Part 1:", cnt)

points = list(filter(lambda x: x[-1]=='A', network.keys()))
cnts = []
for node in points:
    cnt = 0
    while node[-1] != 'Z':
        node = network[node][route[cnt%len(route)]]
        cnt += 1
    cnts.append(cnt)
from math import lcm
print("Part 2:", lcm(*cnts))

# Part 2: failed brute force
# while len(points) != len(list(filter(lambda x: x[-1]=='Z', points))):
#     for i, p in enumerate(points):
#         points[i] = network[p][route[cnt%len(route)]]
#     if(cnt%1000000 == 0):
#         print(points, cnt, route[cnt%len(route)])
#     cnt += 1