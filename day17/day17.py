map = []
with open("input.example1.txt") as f:
    for line in f:
        map.append( [ int(i) for i in line.strip() ])
print("map00", map[0][0])
map[0][0] = 0
print(map)

xmax = len(map[0])
ymax = len(map)

def walk(x, y, heatloss, hist):
    # print("point", x, y, heatloss, "hist:", hist, "steps:", len(hist))
    # if dest: return total heatloss
    if (x,y) == (xmax-1, ymax-1):
        print("reached and end:", hist)
        return heatloss
    
    # which next steps (exclude hist)?
    neighbors = [(x+i, y+j) for i, j in [(1,0), (0,-1), (0,1), (-1,0)]]
    good_neighbors = []
    for i in neighbors:
        if not (i in hist+[(0,0)] or i[0]<0 or i[1]<0 or i[0]>=xmax or i[1]>=ymax):
            if len(hist)>=2 and ((hist[-1][0] == hist[-2][0] == i[0]) or (hist[-1][1] == hist[-2][1] == i[1])):
                # print("three in a row:", hist)
                continue
            good_neighbors.append(i)
            
    # print("goodneighbors:", good_neighbors)

    # recursive call
    results = [walk(i[0], i[1], heatloss+map[i[1]][i[0]], hist[:]+[(i[0],i[1])]) for i in good_neighbors]

    # return minimum loss of recurive calls
    pos_results = []
    for i in results:
        if i>=0:
            pos_results.append(i)
    if(len(pos_results) == 0):
        return -1
    else:
        return min(pos_results)

print(walk(0,0,0,[]))