def manhattan_distance(start_x, start_y, goal_x, goal_y):
    return abs(goal_x - start_x) + abs(goal_y - start_y)


def parse_input(data):
    data_parsed = data.split('\n')
    return data_parsed


def find_crossings(data):
    list_of_visited = []
    list_of_visited_with_steps = []

    for wire in data:
        x = y = 0
        dx = dy = 0
        number_of_steps = 0
        visited = []

        for instruction in wire.split(','):
            direction, distance = instruction[0], int(instruction[1:])

            if direction == 'U':
                dx = 0
                dy = 1
            elif direction == 'D':
                dx = 0
                dy = -1
            elif direction == 'L':
                dx = -1
                dy = 0
            elif direction == 'R':
                dx = 1
                dy = 0

            for _ in range(distance):
                x += dx
                y += dy
                number_of_steps += 1
                visited.append([(x, y), number_of_steps])

        list_of_visited.append(visited)
        list_of_visited_with_steps.append([vis[0] for vis in visited])

    crossings = set(list_of_visited_with_steps[0]) & set(list_of_visited_with_steps[1])

    total_steps = []
    for cross in crossings:
        list_1_distance = list_of_visited[0][list_of_visited_with_steps[0].index(cross)][1]
        list_2_distance = list_of_visited[1][list_of_visited_with_steps[1].index(cross)][1]

        total_steps.append(list_1_distance+list_2_distance)

    return min(total_steps)



def find_distance_crossing(crossings):
    for crossing in crossings:
        pass
    pass


test_data_01 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83'
test_data_01_expected_output = 159

test_data_02 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
test_data_02_expected_output = 135

closest_crossings_01 = find_crossings(parse_input(test_data_01))
closest_crossings_02 = find_crossings(parse_input(test_data_02))

assert closest_crossings_01, test_data_01
assert closest_crossings_02, test_data_02

print(closest_crossings_01)
print(closest_crossings_02)

data = parse_input(open('input.txt').read())
print(find_crossings(data))
