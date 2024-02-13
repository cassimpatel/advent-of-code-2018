def parse_input(input):
    cart_to_track = {'<': '-', '>': '-', '^':'|', 'v':'|'}
    dirs = {'<':(0,-1), '>':(0,1), '^':(-1,0), 'v':(1,0)}

    # split into grid of characters
    grid = [[y for y in x] for x in input.split('\n')]

    # extract carts, overwrite map to be only tracks
    carts = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in '<>v^': continue
            dy, dx = dirs[grid[y][x]]
            carts.append((y, x, dy, dx, 0))
            grid[y][x] = cart_to_track[grid[y][x]]

    return carts, grid

def turn(dy, dx, dir):
    if dir == 'l':
        return (-dx, dy)
    elif dir == 'r':
        return (dx, -dy)

def handle_move(cart, grid):
    y, x, dy, dx, turn_cnt = cart
    y += dy
    x += dx

    # simple, move one on if on a normal track
    if grid[y][x] in '|-':
        return (y, x, dy, dx, turn_cnt)

    # handle turns
    if grid[y][x] in '/\\':
        if grid[y][x] == '/':
            dy, dx = turn(dy, dx, 'l') if dx else turn(dy, dx, 'r')
        else:
            dy, dx = turn(dy, dx, 'r') if dx else turn(dy, dx, 'l')
        return (y, x, dy, dx, turn_cnt)

    # handle intersection
    if turn_cnt == 0:
        dy, dx = turn(dy, dx, 'l')
    elif turn_cnt == 2:
        dy, dx = turn(dy, dx, 'r')
    turn_cnt = (turn_cnt + 1) % 3
    return (y, x, dy, dx, turn_cnt)

def grid_to_str(grid, carts):
    grid = [x.copy() for x in grid]
    dirs = {(0,-1):'<', (0,1):'>', (-1,0):'^', (1,0):'v'}

    for (y, x, dy, dx, _) in carts:
        grid[y][x] = dirs[(dy, dx)]

    return '\n'.join([''.join(x) for x in grid])

def run_carts(grid, carts, part_2 = False):
    while True:

        # sort carts by location, keep list of carts that have crashed this tick
        carts.sort(key = lambda x: (x[0], x[1]))
        crashed = set()
        for i, cart in enumerate(carts):

            # if this cart has crashed, continue, otherwise handle move and move cart
            if i in crashed: continue
            n_cart = handle_move(cart, grid)
            carts[i] = n_cart
            (y, x, _, _, _) = n_cart

            # find indices of other carts crashed into
            crashed_carts = [j for j, cart2 in enumerate(carts) if i != j and (cart2[0], cart2[1]) == (y, x)]
            if len(crashed_carts) == 0: continue

            # if part one, return first crash location, otherwise update list of crashed carts
            if not part_2:
                return f'{x},{y}'
            crashed.add(i)
            crashed.update(crashed_carts)
        
        # remove crashed carts from list, if only one cart left return its location
        carts = [carts[i] for i in range(len(carts)) if i not in crashed]
        if len(carts) == 1:
            return f'{carts[0][1]},{carts[0][0]}'
            
def day13_part1(input):
    carts, grid = parse_input(input)
    return run_carts(grid, carts)

def day13_part2(input):
    carts, grid = parse_input(input)
    return run_carts(grid, carts, True)

if __name__ == "__main__":
    example_input_1 = open('example_1.txt', 'r').read()
    example_input_2 = open('example_2.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day13_part1(example_input_1) ==  '7,3'
    print(day13_part1(test_input))

    assert day13_part2(example_input_2) ==  '6,4'
    print(day13_part2(test_input))