def fuel_calc(noun, verb):
    import csv

    dict = {}
    with open("input.csv", "r") as int_values:
        csv_reader = csv.reader(int_values, delimiter=',')
        address = 0
        for line in csv_reader:
            for item in line:
                dict[address] = int(item)
                address += 1

    dict[1] = noun
    dict[2] = verb

    amount = (len(dict))
    for instruction_pointer in range(0, amount, 4):
        opcode = instruction_pointer
        paramA = instruction_pointer + 1
        paramB = instruction_pointer + 2
        paramC = instruction_pointer + 3

        if dict[opcode] == 99:
            break
        elif dict[opcode] == 1:
            x = dict[dict[paramA]] + dict[dict[paramB]]
        elif dict[opcode] == 2:
            x = dict[dict[paramA]] * dict[dict[paramB]]

        address = int(dict[paramC])

        dict[address] = x
    return dict[0]

from itertools import permutations

test_list = list(range(100))

perm = permutations(test_list, 2)
combos = list(perm)

for item in combos:
    noun = int(item[0])
    verb = int(item[1])
    x = (fuel_calc(noun, verb))
    if x == 19690720:
        print("Answer: " + str((100 * noun + verb)))
        break