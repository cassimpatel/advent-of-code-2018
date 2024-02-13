def parse_input(input):
    stream = [int(x) for x in input.split(' ')]

    def process(l, r):
        node = {
            'children': [],
            'metadata': [],
            'length'  : 2
        }

        # extract header data, move pointer along
        num_child = stream[l]
        num_metad = stream[l+1]
        l += 2

        # append each child, move pointer along length and increase node size
        for _ in range(num_child):
            child = process(l, r)
            node['children'].append(child)
            node['length'] += child['length']
            l += child['length']
            
        # append each metadata, increase node length and pointer
        for _ in range(num_metad):
            node['metadata'].append(stream[l])
            node['length'] += 1
            l += 1

        return node

    return process(0, len(stream) - 1)

def day8_part1(input):
    root = parse_input(input)

    # take sum of metadata and recur for children
    def sum_metadata(node):
        res = sum(node['metadata'])
        for child in node['children']:
            res += sum_metadata(child)
        return res
    
    return sum_metadata(root)

def day8_part2(input):
    root = parse_input(input)

    # calculate node value
    def node_value(node):
        if len(node['children']) == 0:
            return sum(node['metadata'])
        
        # recur if the metadata indicates valid reference
        res = 0
        for ref in node['metadata']:
            if not 1 <= ref <= len(node['children']): continue
            res += node_value(node['children'][ref-1])

        return res
    
    return node_value(root)

if __name__ == "__main__":
    example_input = open('example.txt', 'r').read()
    test_input = open('input.txt', 'r').read()

    assert day8_part1(example_input) ==  138
    print(day8_part1(test_input))

    assert day8_part2(example_input) ==  66
    print(day8_part2(test_input))