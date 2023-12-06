seeds = []
almanac = []
with open('day5.input.txt') as f:
    seeds = [int(s) for s in f.readline().split(" ")[1:] ]
    f.readline()
    map = []
    while(True):
        line = f.readline()
        if(not line):
            almanac.append(map)
            break
        elif(line == "\n"):
            almanac.append(map)
            map = []
            continue
        else:
            if(line[-2] == ":"):
                continue
            map.append([int(s) for s in line.split(" ")])

# almanac from example would look like:
# [[[50, 98, 2], [52, 50, 48]], [[0, 15, 37], [37, 52, 2], [39, 0, 15]], [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], [[88, 18, 7], [18, 25, 70]], [[45, 77, 23], [81, 45, 19], [68, 64, 13]], [[0, 69, 1], [1, 0, 69]]]
locations = []
print(len(range(seeds[1])))

for seed in [seeds[0]+i for i in range(seeds[1])]:
    print("seed {} ".format(seed))
    for map in almanac:
        for line in map:
            (dest, src, ran) = line
            if seed in range(src, src+ran):
                seed = dest+(seed-src)
                break
        print("mapped to {}".format(seed))
    locations.append(seed)
    print("mapped to {}".format(seed))

print(sorted(locations)[0])