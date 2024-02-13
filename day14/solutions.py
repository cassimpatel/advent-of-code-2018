def day14_part1(input):
    recipes = '37'
    elf1, elf2 = 0, 1

    while len(recipes) < input + 10:
        recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
        elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
        elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)

    return recipes[input: input + 10]

def day14_part2(input):
    recipes = '37'
    elf1, elf2 = 0, 1

    while input not in recipes[-len(input)-1:]:
        recipes += str(int(recipes[elf1]) + int(recipes[elf2]))
        elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
        elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)
    
    return recipes.index(input)

if __name__ == "__main__":
    test_input = 505961

    assert day14_part1(9   ) == '5158916779'
    assert day14_part1(5   ) == '0124515891'
    assert day14_part1(18  ) == '9251071085'
    assert day14_part1(2018) == '5941429882'
    print(day14_part1(test_input))

    assert day14_part2('51589') == 9
    assert day14_part2('01245') == 5
    assert day14_part2('92510') == 18
    assert day14_part2('59414') == 2018
    print(day14_part2(str(test_input)))