def cell_value(x, y, serial):
    rack_id = x + 10
    power = (rack_id * y + serial) * rack_id
    power = (power % 1000) // 100
    return power - 5

def get_max_area(serial, part_2 = False):
    # fill grid of cell values
    cells = [[0 for _ in range(301)].copy() for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            cells[y][x] = cell_value(x, y, serial)

    # fill grid with partial sums
    for y in range(1, 301):
        for x in range(1, 301):
            up      = cells[y-1][x]
            left    = cells[y][x-1]
            up_left = cells[y-1][x-1]
            cells[y][x] += left + up - up_left

    res   = ''
    mx    = 0
    sizes = range(1, 301) if part_2 else [3]

    # iterate over and find max area using partial sums
    for size in sizes:
        for y in range(1, 300 - size + 1):
            for x in range(1, 300 - size + 1):
                cur     = cells[y + size - 1][x + size - 1]
                up      = cells[y - 1][x + size - 1]
                left    = cells[y + size - 1][x - 1]
                up_left = cells[y - 1][x - 1]
                area    = cur - up - left + up_left
                if area > mx:
                    mx = area
                    res = f'{x},{y},{size}'

    if part_2:
        return res
    return ','.join(res.split(',')[:-1])

def day8_part1(input):
    return get_max_area(input)
    
def day8_part2(input):
    return get_max_area(input, True)

if __name__ == "__main__":
    test_input = 6878

    assert cell_value(3  , 5  , 8 ) ==  4
    assert cell_value(122, 79 , 57) == -5
    assert cell_value(217, 196, 39) ==  0
    assert cell_value(101, 153, 71) ==  4

    assert day8_part1(18) == '33,45'
    assert day8_part1(42) == '21,61'
    print(day8_part1(test_input))

    assert day8_part2(18) == '90,269,16'
    assert day8_part2(42) == '232,251,12'
    print(day8_part2(test_input))