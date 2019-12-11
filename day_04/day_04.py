from collections import Counter


def permutations(min, max):
    possible_permutations = 0
    possibilities = [i for i in range(min, max, 1)]

    for pos in possibilities:
        split_numbers = [int(d) for d in str(pos)]

        strictly_rising = all(x <= y for x, y in zip(split_numbers, split_numbers[1:]))
        if strictly_rising:
            adjacent_equals = any(x == y for x, y in zip(split_numbers, split_numbers[1:]))
            if adjacent_equals:
                count = Counter(split_numbers).values()
                if 2 in count:
                    possible_permutations += 1

    return possible_permutations


possible_count = permutations(171309, 643603)
print(possible_count)
