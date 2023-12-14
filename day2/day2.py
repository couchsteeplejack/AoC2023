games = {}
pieces = {"red": 12, "green": 13, "blue": 14}

with open("input.txt") as f:
    for line in f:
        game, hands = line.split(":")
        game_num = int(game.split()[1])
        grabs = hands.split(";")
        sum = 0
        for grab in grabs:
            # print( [[col, int(num)] for s in grab.split(",") for (col, num) in s.split()] )
            # print( [num for s in grab.split(",") for (num, col) in s.strip().split()] )
            for s in grab.split(","):
                (num, col) = s.strip().split()
                num = int(num)
                if num > pieces[col]:
                    break
                print(num, col)
                
            else:
                continue
            break
        else:
            sum += game_num
            continue

print(sum)