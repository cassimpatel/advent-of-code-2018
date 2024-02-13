class Node:
    def __init__(self, val, prv = None, nxt = None):
        self.val = val
        self.nxt = nxt
        self.prv = prv

        if nxt:
            self.nxt.prv = self
        if prv:
            self.prv.nxt = self

    def delete(self):
        prv, nxt = self.prv, self.nxt
        prv.nxt = nxt
        nxt.prv = prv

def parse_input(input):
    pts = input.split(' ')

    # return num players, final marble worth
    return int(pts[0]), int(pts[6])

def get_as_array(node):
    cur = node.nxt
    res = [node.val]
    
    while cur != node:
        res.append(cur.val)
        cur = cur.nxt

    return res

def get_max_score(num_players, final_marble):
    # initialise single element and scores
    node   = Node(0)
    node.nxt = node
    node.prv = node
    scores = [0] * num_players

    for i in range(1, final_marble + 1):
        # add to list as usual
        if i % 23 != 0:
            node = Node(i, node.nxt, node.nxt.nxt)
            continue

        # deal with 23 logic
        for _ in range(7):
            node = node.prv
        scores[(i % num_players) - 1] += node.val + i
        node = node.nxt
        node.prv.delete()

    return max(scores)

def day8_part1(input):
    num_players, final_marble = parse_input(input)
    return get_max_score(num_players, final_marble)
    
def day8_part2(input):
    num_players, final_marble = parse_input(input)
    return get_max_score(num_players, final_marble * 100)

if __name__ == "__main__":
    example_input_0 = "9 players; last marble is worth 25 points"
    example_input_1 = "10 players; last marble is worth 1618 points"
    example_input_2 = "13 players; last marble is worth 7999 points"
    example_input_3 = "17 players; last marble is worth 1104 points"
    example_input_4 = "21 players; last marble is worth 6111 points"
    example_input_5 = "30 players; last marble is worth 5807 points"
    test_input      = open('input.txt', 'r').read()

    assert day8_part1(example_input_0) == 32
    assert day8_part1(example_input_1) == 8317
    assert day8_part1(example_input_2) == 146373
    assert day8_part1(example_input_3) == 2764
    assert day8_part1(example_input_4) == 54718
    assert day8_part1(example_input_5) == 37305
    print(day8_part1(test_input))

    print(day8_part2(test_input))