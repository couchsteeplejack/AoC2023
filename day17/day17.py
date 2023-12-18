map = []
with open("input.example1.txt") as f:
    for line in f:
        map.append( [ int(i) for i in line.strip() ])

xmax = len(map[0])
ymax = len(map)

def walk(x, y, heatloss, hist):
    # if dest: return total heatloss
    if (x,y) == (xmax-1, ymax-1):
        return heatloss + map[y][x]
    
    # which next steps (exclude hist)?
    neighbors = [(x+i, y+j) for i, j in [(1,0), (-1,0), (0,1), (0,-1)]]
    for i in neighbors:
        if i in hist:
            neighbors.remove(i)
    
    # recursive call
    results = [walk(i[0], i[1], heatloss+map[i[1]][i[0]], hist[:]+[(i[0],i[1])]) for i in neighbors]

    # return minimum loss of recurive calls
    return min(results)

print(walk(0,0,0,[]))