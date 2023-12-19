
# for each y value maintain min and max x value
xmin = {0: 0}
xmax = {0: 0}

sign = {"D": -1, "L":-1, "U": 1, "R": 1}
curx = 0
cury = 0

def record(y, x): # for y record min and min x value
    if x < xmin[cury]:
        xmin[cury] = x  # can be empty?
    if x > xmax[cury]:
        xmax[cury] = x

def execute(dir, steps):
    if dir in ["L", "R"]:
        curx += sign[dir] * steps
        record(cury, curx)
    else: # "U" or "D"
        pass

with open("example1.input.txt") as f:
    for line in f:
        dir, steps, color = line.strip().split()
        execute(dir, steps)

