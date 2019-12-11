import math


def get_data(path):
    file = open(path).read()
    file_content = file.split('\n')
    return [int(i) for i in file_content]


def part_1():
    file_content = get_data('input.txt')

    sum_of_mass = 0
    for mass in file_content:
        sum_of_mass += math.floor((int(mass) / 3)) - 2

    return sum_of_mass


def part_2():
    file_content = get_data('input.txt')

    fuels = []

    for mass in file_content:
        while mass >= 0:
            mass = (math.floor((mass / 3)) - 2)
            if mass >= 0:
                fuels.append(mass)

    return sum(fuels)


masses = part_2()
print(masses)
