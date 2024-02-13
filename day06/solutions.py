def parse_input(input):
    points = [[int(y) for y in x.split(', ')] for x in input.split('\n')]

    min_x = min(([x[0] for x in points]))
    min_y = min(([x[1] for x in points]))
    max_x = max(([x[0] for x in points])) + 1
    max_y = max(([x[1] for x in points])) + 1

    return points, min_x, max_x, min_y, max_y

def manhattan(x1, x2, y1, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def dist_to_points(y, x, points):
    return {i:manhattan(x, x1, y, y1) for (i, (x1, y1)) in enumerate(points)}

def day6_part1(input):
    points, min_x, max_x, min_y, max_y = parse_input(input)

    # maintain count of each point 
    cnts = {x: 0 for x in range(len(points))}
    border = set()

    # fill in every point
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            # calc distance to each node, and nodes that have the min distance
            dists = dist_to_points(y, x, points)
            min_dist = min(dists.values())
            dists = [k for k in dists.keys() if dists[k] == min_dist]

            # if only one node has shortest distance add to that nodes area
            if len(dists) != 1: continue
            cnts[dists[0]] += 1

            # if this is a border, add to the set of border types to ignore
            if x == min_x or x == max_x - 1 or y == min_y or y == max_y - 1:
                border.add(dists[0])

    # remove counts of infinite areas
    cnts = {k:cnts[k] for k in cnts if k not in border}

    # get key with max value
    res = max(cnts, key=cnts.get)
    return cnts[res]

def day6_part2(input, max_dist = 10000):
    points, min_x, max_x, min_y, max_y = parse_input(input)

    # count number of points with sum of dists < max_dist
    res = 0
    for y in range(min_y, max_y):
        for x in range(min_x, max_x):
            dists = dist_to_points(y, x, points)
            if sum(dists.values()) < max_dist:
                res += 1
    
    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day6_part1(example_input) ==  17
    print(day6_part1(test_input))

    assert day6_part2(example_input, 32) ==  16
    print(day6_part2(test_input))