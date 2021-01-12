def find_match_positive(d, start_point):
    close = range(int(start_point), int(start_point) + 21)
    for num in close:
        if num in d.keys():
            return num
        else:
            continue
    return - 1


def find_match_negative(d, start_point):
    close = range(int(start_point) - 21, int(start_point) + 1)
    for num in close:
        if num in d.keys():
            return num
        else:
            continue
    return - 1


def find_second_match(d, num, start_point, end, direction):
    if num == -1:
        return True
    if direction == 'up' or direction == 'left':
        packman_range = range(int(start_point), int(end) + 9)
    else:
        packman_range = range(int(start_point) - 9, int(end))
    for line in d[num]:
        line_range = set(range(line[0], line[1]+1))
        overlap = line_range.intersection(packman_range)
        if len(overlap) > 0:
            return False
        else:
            continue
    return True





