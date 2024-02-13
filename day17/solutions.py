def parse_input(input):
    for repl in ['=', ', ', '..']:
        input = input.replace(repl, ',')
    input = [x.split(',') for x in input.split('\n')]

    rocks = set()
    for [d1, v, d2, l, r] in input:
        points = [(int(v), i) for i in range(int(l), int(r)+1)]
        # swap around to make sure y is first
        if d1 == 'x':
            points = [(a, b) for (b, a) in points]
        rocks.update(points)
    
    return rocks

def day17_part1(input):
    rocks = parse_input(input)
    max_y = max(y for (y, x) in rocks)
    print(rocks)

    def dfs(y, x):
        if y > max_y:
            # indicate we've gone off the grid
            return 0, True
        if (y, x) in rocks:
            return 0, False
        print(f'{y},{x}')
        rocks.add((y, x))

        res = 1
        down, exceeded = dfs(y + 1, x)
        res += down
        if exceeded:
            return res, exceeded

        left, _ = dfs(y, x - 1)
        right, _ = dfs(y, x + 1)

        return res + left + right, True

    filled, _ = dfs(0, 500)
    print(filled)
    return filled

def day17_part2(input):
    return None

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day17_part1(example_input) ==  57
    print(day17_part1(test_input))

    # assert day17_part2(example_input) ==  325
    # print(day17_part2(test_input))