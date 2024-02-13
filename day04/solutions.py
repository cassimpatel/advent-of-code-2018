def parse_input(input):
    # remove nonsense information
    for repl in ['[', '-', ':', ']', 'Guard #', ' begins shift', ' asleep', ' up']:
        input = input.replace(repl, '')

    # turn into [timestamp, event] list sorted by timestamp
    input = [x.split() for x in input.split('\n')]
    input = [[int(x[0] + x[1]), x[2]] for x in input]
    input.sort(key=lambda x: x[0])

    intervals = []
    guard = -1
    sleep = -1
    for [timestamp, event] in input:
        if event == 'falls':
            sleep = timestamp
        elif event == 'wakes':
            intervals.append((sleep, timestamp, guard))
        else:
            guard = int(event)

    return intervals

def day4_part1(input):
    intervals = parse_input(input)

    # find guard with most minutes asleep
    guards = {}
    for (strt, end, guard) in intervals:
        if guard not in guards:
            guards[guard] = 0
        guards[guard] += end - strt
    res_guard = max(guards, key=guards.get)

    # find minute where guard is asleep most
    minutes = {x:0 for x in range(60)}
    for (strt, end, guard) in intervals:
        if guard != res_guard: continue
        for i in range(strt, end):
            minutes[i % 100] += 1
    res_minute = max(minutes, key=minutes.get)

    return res_guard * res_minute   

def day4_part2(input):
    intervals = parse_input(input)

    # find guard with most minutes asleep
    guard_minutes = {}
    for (strt, end, guard) in intervals:
        for i in range(strt, end):
            if (guard, i % 100) not in guard_minutes:
                guard_minutes[(guard, i % 100)] = 0
            guard_minutes[(guard, i % 100)] += 1
    res_guard_minute = max(guard_minutes, key=guard_minutes.get)

    return res_guard_minute[0] * res_guard_minute[1]

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day4_part1(example_input) ==  240
    print(day4_part1(test_input))

    assert day4_part2(example_input) ==  4455
    print(day4_part2(test_input))