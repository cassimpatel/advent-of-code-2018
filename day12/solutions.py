def parse_input(input):
    input = input.replace('initial state: ', '').replace('=> ', '')
    [start, rules] = input.split('\n\n')

    # form rules as a dictionary
    rules = [x.split() for x in rules.split('\n')]
    rules = {rule: res for [rule, res] in rules}

    return start, rules

def run_simulation(state, rules, num_generations):
    # track the previous generations solution, and how many previous cycles we have seen this solution for
    sol_diff = 0
    prev_sol = 0
    prev_cnt = 0

    # track the position of the leftmost pot and generation number
    gen  = 0
    strt = 0
    while gen < num_generations:
        
        # pad the state with empty pots if they're not already there
        if not state.startswith('...'):
            state = '...' + state
            strt -= 3
        if not state.endswith('...'):
            state += '...'
        
        # calculate each new pots value
        nxt_state = ""
        for i in range(2, len(state)-2):
            part = state[i-2:i+3]
            nxt_state += rules.get(part, '.')

        # increase pos to account, update new state and gen number
        strt += 2
        state = nxt_state
        gen += 1

        # if we have normalised: return the estimated result
        cur_sol = sum([strt + i if state[i] == '#' else 0 for i in range(len(state))])
        if cur_sol - prev_sol == sol_diff:
            prev_cnt += 1
        else:
            sol_diff = cur_sol - prev_sol
            prev_cnt = 0
        if prev_cnt == 50:
            gen_left = num_generations - gen
            return cur_sol + sol_diff * gen_left
        prev_sol = cur_sol

    return cur_sol

def day12_part1(input):
    start, rules = parse_input(input)
    res = run_simulation(start, rules, 20)
    return res

def day12_part2(input):
    start, rules = parse_input(input)
    res = run_simulation(start, rules, 50000000000)
    return res

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day12_part1(example_input) ==  325
    print(day12_part1(test_input))

    print(day12_part2(test_input))