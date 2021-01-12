import dots

black = (0, 0, 0)
red = (225, 0, 0)
white = (255, 255, 255)
bx = 50
by = 200

lines = [((50, 835), (1310, 835)), ((1310, 200), (1310, 835)), ((50, 200), (1310, 200)),
         ((50, 200), (50, 835)), ((bx + 1050, by + 70), (bx + 1050, by + 140)), ((bx + 1050, by + 70),
                                                                                 (bx + 1190, by + 70)),
         ((bx + 1190, by + 70), (bx + 1190, by + 280)), ((bx + 1120, by + 280), (bx + 1190, by + 280)),
         ((bx + 1120, by + 140), (bx + 1120, by + 280)), ((bx + 1050, by + 140), (bx + 1120, by + 140)),
         ((bx + 980, by + 0), (bx + 980, by + 140)), ((bx + 910, by + 0), (bx + 910, by + 140)),
         ((bx + 910, by + 140), (bx + 980, by + 140)), ((bx + 910, by + 210), (bx + 1050, by + 210)),
         ((bx + 1050, by + 210), (bx + 1050, by + 280)), ((bx + 910, by + 280), (bx + 1050, by + 280)),
         ((bx + 910, by + 210), (bx + 910, by + 280)), ((bx + 910, by + 350), (bx + 910, by + 420)),
         ((bx + 910, by + 420), (bx + 1050, by + 420)), ((bx + 1050, by + 350), (bx + 1050, by + 420)),
         ((bx + 910, by + 350), (bx + 1050, by + 350)), ((bx + 1120, by + 350), (bx + 1190, by + 350)),
         ((bx + 1190, by + 350), (bx + 1190, by + 560)), ((bx + 1050, by + 560), (bx + 1190, by + 560)),
         ((bx + 1050, by + 490), (bx + 1050, by + 560)), ((bx + 1050, by + 490), (bx + 1120, by + 490)),
         ((bx + 1120, by + 350), (bx + 1120, by + 490)), ((bx + 980, by + 490), (bx + 980, by + 630)),
         ((bx + 910, by + 490), (bx + 980, by + 490)), ((bx + 910, by + 490), (bx + 910, by + 630)),
         ((bx + 700, by + 210), (bx + 830, by + 210)), ((bx + 830, by + 210), (bx + 830, by + 420)),
         ((bx + 420, by + 420), (bx + 830, by + 420)), ((bx + 420, by + 210), (bx + 420, by + 420)),
         ((bx + 420, by + 210), (bx + 560, by + 210)), ((bx + 560, by + 210), (bx + 560, by + 280)),
         ((bx + 490, by + 280), (bx + 560, by + 280)), ((bx + 490, by + 280), (bx + 490, by + 350)),
         ((bx + 490, by + 350), (bx + 770, by + 350)), ((bx + 770, by + 280), (bx + 770, by + 350)),
         ((bx + 700, by + 280), (bx + 770, by + 280)), ((bx + 700, by + 210), (bx + 700, by + 280)),
         ((bx + 280, by + 0), (bx + 280, by + 140)), ((bx + 280, by + 140), (bx + 350, by + 140)),
         ((bx + 350, by + 0), (bx + 350, by + 140)), ((bx + 210, by + 210), (bx + 350, by + 210)),
         ((bx + 350, by + 210), (bx + 350, by + 280)), ((bx + 210, by + 280), (bx + 350, by + 280)),
         ((bx + 210, by + 210), (bx + 210, by + 280)), ((bx + 210, by + 350), (bx + 350, by + 350)),
         ((bx + 350, by + 350), (bx + 350, by + 420)), ((bx + 210, by + 420), (bx + 350, by + 420)),
         ((bx + 210, by + 350), (bx + 210, by + 420)), ((bx + 280, by + 490), (bx + 280, by + 630)),
         ((bx + 280, by + 490), (bx + 350, by + 490)), ((bx + 350, by + 490), (bx + 350, by + 630)),
         ((bx + 70, by + 70), (bx + 210, by + 70)), ((bx + 210, by + 70), (bx + 210, by + 140)),
         ((bx + 140, by + 140), (bx + 140, by + 280)), ((bx + 70, by + 280), (bx + 140, by + 280)),
         ((bx + 70, by + 70), (bx + 70, by + 280)), ((bx + 70, by + 350), (bx + 140, by + 350)),
         ((bx + 140, by + 350), (bx + 140, by + 490)), ((bx + 140, by + 490), (bx + 210, by + 490)),
         ((bx + 210, by + 490), (bx + 210, by + 560)), ((bx + 70, by + 560), (bx + 210, by + 560)),
         ((bx + 70, by + 350), (bx + 70, by + 560)), ((bx + 420, by + 490), (bx + 830, by + 490)),
         ((bx + 830, by + 490), (bx + 830, by + 560)), ((bx + 420, by + 490), (bx + 420, by + 560)),
         ((bx + 420, by + 560), (bx + 830, by + 560)), ((bx + 420, by + 70), (bx + 830, by + 70)),
         ((bx + 830, by + 70), (bx + 830, by + 140)), ((bx + 420, by + 140), (bx + 830, by + 140)),
         ((bx + 420, by + 70), (bx + 420, by + 140)), ((bx + 140, by + 140), (bx + 210, by + 140)),
         ((bx + 140, by + 350), (bx + 140, by + 490))]

dict_x = {}
dict_y = {}


def uniqe(lst):
    xs = []
    ys = []
    for line in lst:
        for (x, y) in line:
            xs.append(x)
            ys.append(y)
    uniqe_x = set(xs)
    uniqe_y = set(ys)
    return list(uniqe_x), list(uniqe_y)


a, b = uniqe(lines)
match_a = []
match_b = []

for num in a:
    for line in lines:
        if line[0][0] == line[1][0]:
            if line[0][0] == num:
                height = [line[0][1], line[1][1]]
                match_a.append(height)

    dict_x[num] = match_a
    match_a = []

for num in b:
    for line in lines:
        if line[0][1] == line[1][1]:
            if line[0][1] == num:
                width = [line[0][0], line[1][0]]
                match_b.append(width)

    dict_y[num] = match_b
    match_b = []

# print(dict_x)
# print(dict_y)

all_dots = []
dots_locations_y = {235: [(85, 295), (435, 925), (1065, 1275)], 375: [(225, 1135)], 515: [(85, 435), (925, 1275)],
                    655: [(225, 1135)], 795: [(85, 295), (435, 925), (1065, 1275)]}
for key in dots_locations_y.keys():
    for item in dots_locations_y[key]:
        line = range(item[0], item[1] + 1, 35)
        for i in line:
            if i == 85 or i == 1275:
                if key == 235 or key == 795:
                    dot = dots.Dot(red, black, i, key, False)
                    all_dots.append(dot)
                else:
                    dot = dots.Dot(white, black, i, key, False)
                    all_dots.append(dot)
            else:
                dot = dots.Dot(white, black, i, key, False)
                all_dots.append(dot)

dots_locations_x = {85: [(235, 795)], 225: [(375, 655)], 295: [(235, 375), (655, 795)], 435: [(235, 795)],
                    925: [(235, 795)], 1065: [(235, 375), (655, 795)], 1275: [(235, 795)], 1135: [(375, 655)]}
for key in dots_locations_x.keys():
    for item in dots_locations_x[key]:
        line = range(item[0], item[1] + 1, 35)
        for i in line:
            if key == 85 or key == 1275:
                if i == 235 or i == 795:
                    dot = dots.Dot(red, black, key, i, False)
                    all_dots.append(dot)
                else:
                    dot = dots.Dot(white, black, key, i, False)
                    all_dots.append(dot)
            else:
                dot = dots.Dot(white, black, key, i, False)
                all_dots.append(dot)

roads_y = {}
roads_x = {}

for line_x in dots_locations_x.keys():
    new_x = line_x - 20
    new_y = []
    for part in dots_locations_x[line_x]:
        corr = list(part)
        new_part = (corr[0] - 20, corr[1] - 20)
        new_y.append(new_part)
    roads_x[new_x] = new_y

for line_y in dots_locations_y.keys():
    new_y = line_y - 20
    new_x = []
    for part in dots_locations_y[line_y]:
        corr = list(part)
        new_part = (corr[0] - 20, corr[1] - 20)
        new_x.append(new_part)
    roads_y[new_y] = new_x

intersections = {}
all_dots_x = []
all_dots_y = []


def find_directions(lst_x, lst_y, point):
    directions = []
    p = list(point)
    up = (p[0], p[1] - 5)
    down = (p[0], p[1] + 5)
    right = (p[0] + 5, p[1])
    left = (p[0] - 5, p[1])
    if up in lst_x:
        directions.append('up')
    if down in lst_x:
        directions.append('down')
    if right in lst_y:
        directions.append('right')
    if left in lst_y:
        directions.append('left')

    return directions


for key in roads_y.keys():
    for part in roads_y[key]:
        lst = list(part)
        dots = range(lst[0], lst[1] + 1, 5)
        for dot in dots:
            all_dots_y.append((dot, key))

for key in roads_x.keys():
    for part in roads_x[key]:
        lst = list(part)
        dots = range(lst[0], lst[1] + 1, 5)
        for dot in dots:
            all_dots_x.append((key, dot))

for dot in all_dots_x:
    if dot in all_dots_y:
        all_d = find_directions(all_dots_x, all_dots_y, dot)
        intersections[dot] = all_d

print(roads_y)
print(roads_x)