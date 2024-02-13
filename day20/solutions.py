def parse_input(input):
    # print(input)
    input = input.replace('(', ',[[').replace('|', '],[').replace(')', ']],')
    input = input.replace('^', '').replace('$', '')
    input = input.replace(',', '')
    # print(input)

    res = []
    stck = [res]
    cur_str = ''
    cur = 0
    while cur < len(input):
        # print(cur, input[cur], stck)

        cur_c = input[cur]
        if cur_c == '[':
            stck.append([])
            pass
        elif cur_c == ']':
            stck[-2].append(stck[-1])
            stck = stck[:-1]
            pass
        elif cur_c == ',':

            pass
        else:
            cur_str = ''
            while cur < len(input) and input[cur] in 'WENS':
                cur_str += input[cur]
                cur += 1
            stck[-1].append(cur_str)
            cur -= 1
            pass
            
        cur += 1
    # print(res)

    # print(eval(input))
    return stck[0]

def day20_part1(input):
    root = parse_input(input)

    def max_len(path):
        # print(path)
        res = 0

        for p in path:
            if type(p) == str:
                res += len(p)
                continue

            if [] in p:
                continue

            p1, p2 = max_len(p[0]), max_len(p[1])
            res += max(p1, p2)
        # print(path, res)

        return res


    res = max_len(root)
    # print(res)
    return res

def day20_part2(input):
    return None

if __name__ == "__main__":
    test_input = open('input.txt', 'r').read()

    assert day20_part1('^WNE$') == 3
    assert day20_part1('^ENWWW(NEEE|SSE(EE|N))$') == 10
    assert day20_part1('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$') == 18
    assert day20_part1('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$') == 23
    assert day20_part1('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$') == 31
    print(day20_part1(test_input))
    # 804 too low

    # print(day20_part2(test_input))