pieces = {"red": 12, "green": 13, "blue": 14}
sum_part1 = 0
sum_part2 = 0

with open("input.txt") as f:
    for line in f:
        game, game_data = line.split(":")
        game_num = int(game.split()[1])
        grabs = game_data.split(";")
        fail = False
        fewest = {}
        for grab in grabs:
            print(grab)
            for s in grab.split(","):
                (num, col) = s.strip().split()
                num = int(num)
                col = col.strip()
                if num > pieces[col]:
                    fail = True
                if num > fewest.get(col, 0): # part2
                    fewest[col] = num
        if not fail:
            sum_part1 += game_num
        power = 1 # part 2
        for i in fewest.values():
            power *= i
        sum_part2 += power

print("part1", sum_part1)
print("part2", sum_part2)