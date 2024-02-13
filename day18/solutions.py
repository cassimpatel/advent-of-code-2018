def parse_input(input):
    return [[y for y in x] for x in input.split('\n')]

def run_sim(grid, minutes):
    neighs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    h = len(grid)
    w = len(grid[0])

    states = {}
    cycle_fnd = False
    t = 0

    while t < minutes:
        new_grid = [x.copy() for x in grid]

        for y in range(h):
            for x in range(w):
                cnt = {'.':0, '|':0, '#':0}

                for (dy, dx) in neighs:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < h and 0 <= nx < w): continue
                    cnt[grid[ny][nx]] += 1

                if grid[y][x] == '.' and cnt['|'] >= 3:
                    new_grid[y][x] = '|'
                elif grid[y][x] == '|' and cnt['#'] >= 3:
                    new_grid[y][x] = '#'
                elif grid[y][x] == '#' and not (cnt['|'] >= 1 and cnt['#'] >= 1):
                    new_grid[y][x] = '.'
        
        grid = new_grid
        t += 1

        grid_state = '\n'.join([''.join(x) for x in grid])
        if not cycle_fnd and grid_state in states:
            cycle_fnd = True
            cycle_len = t - states[grid_state]
            cycles_left = (minutes - t) // cycle_len
            t += cycles_left * cycle_len
        states[grid_state] = t
    
    acres = sum(x.count('|') for x in grid)
    yards = sum(x.count('#') for x in grid)
    return acres * yards


def day18_part1(input):
    grid = parse_input(input)
    res = run_sim(grid, 10)
    return res

def day18_part2(input):
    grid = parse_input(input)
    res = run_sim(grid, 1000000000)
    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day18_part1(example_input) ==  1147
    print(day18_part1(test_input))

    print(day18_part2(test_input))