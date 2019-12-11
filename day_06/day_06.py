from collections import defaultdict


def generate_com_dict(data):
    com_dict = defaultdict()
    data = data.split('\n')

    # Fill dict.
    for line in data:
        center_of_mass, planet = line.split(')')
        com_dict[planet] = center_of_mass

    return com_dict


def count_orbits(orbits):
    orbit_counter = 0
    for orbit in orbits.keys():
        current_orbit = orbit
        while current_orbit in orbits.keys():
            orbit_counter += 1
            current_orbit = orbits[current_orbit]

    return orbit_counter


def smallest_common(orbits):
    you = orbits['YOU']
    san = orbits['SAN']
    you_dict = defaultdict()
    san_dict = defaultdict()

    key = you
    while key != 'COM':
        you_dict[key] = orbits[key]
        key = orbits[key]

    key = san
    while key != 'COM':
        san_dict[key] = orbits[key]
        key = orbits[key]

    changes_to_you = 0
    changes_to_san = 0
    common = None

    for k in you_dict.keys():
        if k in san_dict.keys():
            common = k
            break
        changes_to_san += 1

    for k in san_dict.keys():
        if k == common:
            break
        changes_to_you += 1

    return changes_to_you + changes_to_san

test_input = 'test_input.txt'
test_answer = 42

test_input_2 = 'test_input_02.txt'
test_answer_02 = 4

actual_input = 'input.txt'

inp = open(test_input_2).read()
graph = generate_com_dict(inp)

smallest = smallest_common(graph)

print(smallest)
