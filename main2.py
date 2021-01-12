import pygame
import time
import funcs
from board import dict_x as dx
from board import dict_y as dy
from board import roads_x as rx
from board import roads_y as ry
from board import all_dots as dots_x
import ghosts
import random
import board
from board import intersections as inter

pygame.init()

blue = (0, 0, 175)
black = (0, 0, 0)
red = (225, 0, 0)
white = (255, 255, 255)

display_width = 1360
display_height = 1030

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PACKMAN')
clock = pygame.time.Clock()

big_packman = pygame.image.load('C:\\Users\\Admin\\Pictures\\Saved Pictures\\packman.jpg')
Packman = pygame.transform.scale(big_packman, (40, 40))
packman_width = 40
packman_height = 40

blue_ghost = ghosts.Ghost('blue', 40, 40, 660, 355, 625, 495)
red_ghost = ghosts.Ghost('red', 40, 40, 660, 355, 695, 495)
pink_ghost = ghosts.Ghost('pink', 40, 40, 660, 355, 765, 495)
orange_ghost = ghosts.Ghost('orange', 40, 40, 660, 355, 555, 495)

all_ghosts = [blue_ghost, red_ghost, pink_ghost, orange_ghost]

x = 610
y = 775
x_change = 0
y_change = 0
rotate = 0
current_direction = None
new_direction = None
situation = 0
timer = 0
timer1 = 0
special = 0
lives = 3
oppisate = {'right': 'left', 'left': 'right', 'up': 'down', 'down': 'up'}


def ghosts_starting_point(g, first, second):
    g = pygame.transform.rotate(g.which_ghost(), 0)
    gameDisplay.blit(g, (first, second))


def ghost_location(g, first, second, third, forth):
    if g.out is True:
        ghosts_starting_point(g, first, second)
    else:
        ghosts_starting_point(g, third, forth)


def choose(g, dic):
    if (g.horizontal, g.vertical) in dic.keys():
        new_path = random.choice(dic[(g.horizontal, g.vertical)])
        g.current_direction = new_path


def choose_smart(g, dic, h, v):
    if (g.horizontal, g.vertical) in dic.keys():
        if h > g.horizontal and 'right' in dic[(g.horizontal, g.vertical)]:
            g.current_direction = 'right'
        elif h < g.horizontal and 'left' in dic[(g.horizontal, g.vertical)]:
            g.current_direction = 'left'
        elif v > g.vertical and 'down' in dic[(g.horizontal, g.vertical)]:
            g.current_direction = 'down'
        elif v < g.vertical and 'up' in dic[(g.horizontal, g.vertical)]:
            g.current_direction = 'up'
        else:
            choose(g, dic)


def movment(g):
    if g.current_direction == 'up':
        g.vertical -= 5
    elif g.current_direction == 'down':
        g.vertical += 5
    elif g.current_direction == 'right':
        g.horizontal += 5
    elif g.current_direction == 'left':
        g.horizontal -= 5


def ghost_start(g):
    options = ['right', 'left']
    new_path = random.choice(options)
    g.current_direction = new_path


def smart_start(g, h):
    if g.horizontal < h:
        g.current_direction = 'right'
    elif g.horizontal > h:
        g.current_direction = 'left'
    else:
        ghost_start(g)


def ghost_movment(g, dic):
    if g.out is True:
        if g.current_direction is None:
            ghost_start(g)
            movment(g)
        else:
            choose(g, dic)
            movment(g)


def smart_movment(g, dic, h, v):
    if g.out is True:
        if g.current_direction is None:
            smart_start(g, h)
            movment(g)
        else:
            choose_smart(g, dic, h, v)
            movment(g)


def busted(h, v, lst_of_ghosts):
    for g in lst_of_ghosts:
        if g.horizontal <= h <= g.horizontal + 40 or g.horizontal <= h + 40 <= g.horizontal + 40:
            if g.vertical <= v <= g.vertical + 40 or g.vertical <= v + 40 <= g.vertical:
                return [True, g]
    else:
        return [False]


def special_ability():
    if x < 85 < x + 40 or x < 1275 < x + 40:
        if y < 235 < y + 40 or y < 795 < y + 40:
            return True
    else:
        return False


def game(first, second, ro):
    bx = 50
    by = 200
    gameDisplay.fill(black)
    pygame.draw.line(gameDisplay, blue, (50, 200), (50, 835), 5)
    pygame.draw.line(gameDisplay, blue, (50, 200), (1310, 200), 5)
    pygame.draw.line(gameDisplay, blue, (1310, 835), (1310, 200), 5)
    pygame.draw.line(gameDisplay, blue, (1310, 835), (50, 835), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 490), (bx + 830, by + 490), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 490), (bx + 830, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 490), (bx + 420, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 560), (bx + 830, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 70), (bx + 830, by + 70), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 70), (bx + 830, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 140), (bx + 830, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 70), (bx + 420, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 70), (bx + 1050, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 70), (bx + 1190, by + 70), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1190, by + 70), (bx + 1190, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 280), (bx + 1190, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 280), (bx + 1120, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 140), (bx + 1050, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 0), (bx + 980, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 0), (bx + 910, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 140), (bx + 910, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 210), (bx + 1050, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 210), (bx + 1050, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 280), (bx + 910, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 280), (bx + 910, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 350), (bx + 910, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 420), (bx + 1050, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 420), (bx + 1050, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 350), (bx + 1050, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 350), (bx + 1190, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1190, by + 350), (bx + 1190, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 560), (bx + 1190, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 490), (bx + 1050, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 490), (bx + 1120, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 490), (bx + 1120, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 630), (bx + 980, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 490), (bx + 980, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 490), (bx + 910, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 210), (bx + 830, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 210), (bx + 830, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 420), (bx + 830, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 210), (bx + 420, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 210), (bx + 560, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 560, by + 210), (bx + 560, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 280), (bx + 560, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 280), (bx + 490, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 350), (bx + 770, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 770, by + 280), (bx + 770, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 280), (bx + 770, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 210), (bx + 700, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 0), (bx + 280, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 140), (bx + 350, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 0), (bx + 350, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 210), (bx + 350, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 210), (bx + 350, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 280), (bx + 350, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 210), (bx + 210, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 350), (bx + 350, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 350), (bx + 350, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 420), (bx + 350, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 350), (bx + 210, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 490), (bx + 280, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 490), (bx + 350, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 490), (bx + 350, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 70), (bx + 210, by + 70), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 70), (bx + 210, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 140), (bx + 210, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 140), (bx + 140, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 280), (bx + 140, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 70), (bx + 70, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 350), (bx + 140, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 350), (bx + 140, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 490), (bx + 210, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 490), (bx + 210, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 560), (bx + 210, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 350), (bx + 70, by + 560), 5)
    home(x, y, packman_width, dots_x)
    for spot in dots_x:
        pygame.draw.circle(gameDisplay, spot.dot_color(), (spot.horizontal, spot.vertical), 5, 0)
    for key in rx.keys():
        for part in rx[key]:
            new_part = list(part)
            start = new_part[0]
            end = new_part[1]
            pygame.draw.line(gameDisplay, black, (key, start), (key, end), 3)
    for key in ry.keys():
        for part in ry[key]:
            new_part = list(part)
            start = new_part[0]
            end = new_part[1]
            pygame.draw.line(gameDisplay, black, (start, key), (end, key), 3)
    packman_starting_point(first, second, ro)
    ghost_movment(blue_ghost, inter)
    ghost_location(blue_ghost, blue_ghost.horizontal, blue_ghost.vertical, blue_ghost.home_x, blue_ghost.home_y)
    ghost_movment(red_ghost, inter)
    ghost_location(red_ghost, red_ghost.horizontal, red_ghost.vertical, red_ghost.home_x, red_ghost.home_y)
    ghost_movment(pink_ghost, inter)
    ghost_location(pink_ghost, pink_ghost.horizontal, pink_ghost.vertical, pink_ghost.home_x, pink_ghost.home_y)
    ghost_movment(orange_ghost, inter)
    ghost_location(orange_ghost, orange_ghost.horizontal, orange_ghost.vertical,
                   orange_ghost.home_x, orange_ghost.home_y)
    pygame.display.update()
    clock.tick(50)


# make packman appear at starting point
def packman_starting_point(first, second, num):
    packman = pygame.transform.rotate(Packman, 90 * num)
    gameDisplay.blit(packman, (first, second))


# checks if can keep moving in current path or make a turn
def check_for_limits_positive(d, first, second, long, direction):
    match = funcs.find_match_positive(d, first + long)
    free = funcs.find_second_match(d, match, second, second + long, direction)
    return free


def check_for_limits_negative(d, first, second, long, direction):
    match = funcs.find_match_negative(d, first)
    free = funcs.find_second_match(d, match, second, second + long, direction)
    return free


def arrows_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return 'q'

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                return 'left'

            elif event.key == pygame.K_RIGHT:
                return 'right'

            elif event.key == pygame.K_UP:
                return 'up'

            elif event.key == pygame.K_DOWN:
                return 'down'

            else:
                return 'same'


def check_path_positive(d, first, second, long, direction):
    clear = check_for_limits_positive(d, first, second, long, direction)
    if clear is True:
        return True
    else:
        return False


def check_path_negative(d, first, second, long, direction):
    clear = check_for_limits_negative(d, first, second, long, direction)
    if clear is True:
        return True
    else:
        return False


def home(h, v, long, dots):
    for d in dots:
        if h < d.horizontal < h + long:
            if v < d.vertical < v + long:
                d.visited = True
            else:
                pass


def check_where_to_go(horizontal, vertical, r):
    if current_direction == 'right':
        for p in board.roads_y[vertical]:
            lst = list(p)
            if horizontal in range(p[0], p[1] + 1):
                if lst[1] > horizontal:
                    x_add = 5
                    ro = 2
                    y_add = 0
                    return [x_add, y_add, ro]
                else:
                    return [0, 0, r]

    elif current_direction == 'down':
        for p in board.roads_x[horizontal]:
            lst = list(p)
            if vertical in range(p[0], p[1] + 1):
                if lst[1] > vertical:
                    y_add = 5
                    x_add = 0
                    ro = 1
                    return [x_add, y_add, ro]
                else:
                    return [0, 0, r]

    elif current_direction == 'left':
        for p in board.roads_y[vertical]:
            lst = list(p)
            if horizontal in range(p[0], p[1] + 1):
                if lst[0] < horizontal:
                    x_add = -5
                    y_add = 0
                    ro = 0
                    return [x_add, y_add, ro]
                else:
                    return [0, 0, r]

    elif current_direction == 'up':
        for p in board.roads_x[horizontal]:
            lst = list(p)
            if vertical in range(p[0], p[1] + 1):
                if lst[0] < vertical:
                    y_add = -5
                    x_add = 0
                    ro = 3
                    return [x_add, y_add, ro]
                else:
                    return [0, 0, r]


def win(dots):
    visit = []
    for dot in dots:
        condition = dot.visited
        visit.append(condition)
    if set(visit) == {True}:
        print('you won')
        lives = 0
    else:
        pass


while lives > 0:
    time1 = pygame.time.get_ticks()
    if situation == 0:
        game(x, y, rotate)
        where_to = arrows_input()
        if where_to == 'q':
            lives = 0
        else:
            if where_to is None:
                pass
            else:
                current_direction = where_to
                situation = 1

    elif situation == 1:  # keep current path
        where_to = arrows_input()
        if where_to == 'q':
            lives = 0

        elif where_to == current_direction or where_to is None:
            print(x)
            answer = check_where_to_go(x, y, rotate)
            print('answer is ' + str(answer))
            x += answer[0]
            y += answer[1]
            rotate = answer[2]
            # if current_direction == 'right':
            #     new way
            #     for part in board.roads_y[y]:
            #         lst = list(part)
            #         if x in range(part[0], part[1] + 1):
            #             if lst[1] > x:
            #                 x += 5
            #                 rotate = 2

            # old way
            # keep_going = check_path_positive(dx, x, y, packman_width, current_direction)
            # if keep_going is True:
            #     rotate = 2
            #     x += 5
            # else:
            #     pass

            # elif current_direction == 'down':
            #     new way
            #     for part in board.roads_x[x]:
            #         lst = list(part)
            #         if y in range(part[0], part[1] + 1):
            #             if lst[1] > y:
            #                 y += 5
            #                 rotate = 1

            # old way
            # keep_going = check_path_positive(dy, y, x, packman_height, current_direction)
            # if keep_going is True:
            #     rotate = 1
            #     y += 5
            # else:
            #     pass

            # elif current_direction == 'left':
            #     new way
            #     for part in board.roads_y[y]:
            #         lst = list(part)
            #         if x in range(part[0], part[1] + 1):
            #             if lst[0] < x:
            #                 x -= 5
            #                 rotate = 0

            # old way
            # keep_going = check_path_negative(dx, x, y, packman_width, current_direction)
            # if keep_going is True:
            #     rotate = 0
            #     x += -5
            # else:
            #     pass

            # elif current_direction == 'up':
            #     new way
            #     for part in board.roads_x[x]:
            #         lst = list(part)
            #         if y in range(part[0], part[1] + 1):
            #             if lst[0] < y:
            #                 y -= 5
            #                 rotate = 3

            # old way
            # keep_going = check_path_negative(dy, y, x, packman_height, current_direction)
            # if keep_going is True:
            #     rotate = 3
            #     y += -5
            # else:
            #     pass
        else:
            new_direction = where_to
            situation = 2

    elif situation == 2:
        where_to = arrows_input()
        if where_to == 'q':
            lives = 0
        elif where_to == current_direction:
            situation = 1

        elif where_to is not None and where_to != new_direction:
            new_direction = where_to

        elif oppisate[current_direction] == new_direction:
            current_direction = new_direction
            situation = 1

        else:
            if new_direction == 'right':
                # new way
                if (x, y) in inter.keys():
                    if 'right' in inter[(x, y)]:
                        situation = 3
                    else:
                        answer = check_where_to_go(x, y, rotate)
                        x += answer[0]
                        y += answer[1]
                        rotate = answer[2]

                else:
                    answer = check_where_to_go(x, y, rotate)
                    x += answer[0]
                    y += answer[1]
                    rotate = answer[2]
                    # if current_direction == 'right':
                    #     for part in board.roads_y[y]:
                    #         lst = list(part)
                    #         if x in range(part[0], part[1] + 1):
                    #             if lst[1] > x:
                    #                 x += 5
                    #                 rotate = 2
                    #
                    # elif current_direction == 'down':
                    #     for part in board.roads_x[x]:
                    #         lst = list(part)
                    #         if y in range(part[0], part[1] + 1):
                    #             if lst[1] > y:
                    #                 y += 5
                    #                 rotate = 1
                    #
                    # elif current_direction == 'left':
                    #     for part in board.roads_y[y]:
                    #         lst = list(part)
                    #         if x in range(part[0], part[1] + 1):
                    #             if lst[0] < x:
                    #                 x -= 5
                    #                 rotate = 0
                    #
                    # elif current_direction == 'up':
                    #     for part in board.roads_x[x]:
                    #         lst = list(part)
                    #         if y in range(part[0], part[1] + 1):
                    #             if lst[0] < y:
                    #                 y -= 5
                    #                 rotate = 3

                # old way
                # make_turn = check_path_positive(dx, x, y, packman_width, current_direction)
                # if make_turn is True:
                #     situation = 3
                # else:
                #     if current_direction == 'right':
                #         keep_going = check_path_positive(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 2
                #             x += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'down':
                #         keep_going = check_path_positive(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 1
                #             y += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'left':
                #         keep_going = check_path_negative(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 0
                #             x += -5
                #         else:
                #             pass
                #
                #     elif current_direction == 'up':
                #         keep_going = check_path_negative(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 3
                #             y += -5
                #         else:
                #             pass

            if new_direction == 'left':
                # new way
                if (x, y) in inter.keys():
                    if 'left' in inter[(x, y)]:
                        situation = 3
                    else:
                        answer = check_where_to_go(x, y, rotate)
                        x += answer[0]
                        y += answer[1]
                        rotate = answer[2]

                else:
                    answer = check_where_to_go(x, y, rotate)
                    x += answer[0]
                    y += answer[1]
                    rotate = answer[2]
                #     if current_direction == 'right':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[1] > x:
                #                     x += 5
                #                     rotate = 2
                #
                #     elif current_direction == 'down':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[1] > y:
                #                     y += 5
                #                     rotate = 1
                #
                #     elif current_direction == 'left':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[0] < x:
                #                     x -= 5
                #                     rotate = 0
                #
                #     elif current_direction == 'up':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[0] < y:
                #                     y -= 5
                #                     rotate = 3

                # old way
                # make_turn = check_path_negative(dx, x, y, packman_width, current_direction)
                # if make_turn is True:
                #     situation = 3
                # else:
                #     if current_direction == 'right':
                #         keep_going = check_path_positive(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 2
                #             x += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'down':
                #         keep_going = check_path_positive(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 1
                #             y += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'left':
                #         keep_going = check_path_negative(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 0
                #             x += -5
                #         else:
                #             pass
                #
                #     elif current_direction == 'up':
                #         keep_going = check_path_negative(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 3
                #             y += -5
                #         else:
                #             pass

            if new_direction == 'down':
                # new way
                if (x, y) in inter.keys():
                    if 'down' in inter[(x, y)]:
                        situation = 3
                    else:
                        answer = check_where_to_go(x, y, rotate)
                        print(answer)
                        x += answer[0]
                        y += answer[1]
                        rotate = answer[2]

                else:
                    answer = check_where_to_go(x, y, rotate)
                    x += answer[0]
                    y += answer[1]
                    rotate = answer[2]
                #     if current_direction == 'right':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[1] > x:
                #                     x += 5
                #                     rotate = 2
                #
                #     elif current_direction == 'down':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[1] > y:
                #                     y += 5
                #                     rotate = 1
                #
                #     elif current_direction == 'left':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[0] < x:
                #                     x -= 5
                #                     rotate = 0
                #
                #     elif current_direction == 'up':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[0] < y:
                #                     y -= 5
                #                     rotate = 3

                # old way
                # make_turn = check_path_positive(dy, y, x, packman_width, current_direction)
                # if make_turn is True:
                #     situation = 3
                # else:
                #     if current_direction == 'right':
                #         keep_going = check_path_positive(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 2
                #             x += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'down':
                #         keep_going = check_path_positive(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 1
                #             y += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'left':
                #         keep_going = check_path_negative(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 0
                #             x += -5
                #         else:
                #             pass
                #
                #     elif current_direction == 'up':
                #         keep_going = check_path_negative(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 3
                #             y += -5
                #         else:
                #             pass

            if new_direction == 'up':
                # new way
                if (x, y) in inter.keys():
                    if 'up' in inter[(x, y)]:
                        situation = 3
                    else:
                        answer = check_where_to_go(x, y, rotate)
                        x += answer[0]
                        y += answer[1]
                        rotate = answer[2]

                else:
                    answer = check_where_to_go(x, y, rotate)
                    x += answer[0]
                    y += answer[1]
                    rotate = answer[2]

                #     if current_direction == 'right':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[1] > x:
                #                     x += 5
                #                     rotate = 2
                #
                #     elif current_direction == 'down':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[1] > y:
                #                     y += 5
                #                     rotate = 1
                #
                #     elif current_direction == 'left':
                #         for part in board.roads_y[y]:
                #             lst = list(part)
                #             if x in range(part[0], part[1] + 1):
                #                 if lst[0] < x:
                #                     x -= 5
                #                     rotate = 0
                #
                #     elif current_direction == 'up':
                #         for part in board.roads_x[x]:
                #             lst = list(part)
                #             if y in range(part[0], part[1] + 1):
                #                 if lst[0] < y:
                #                     y -= 5
                #                     rotate = 3

                # old way
                # make_turn = check_path_negative(dy, y, x, packman_width, current_direction)
                # if make_turn is True:
                #     situation = 3
                # else:
                #     if current_direction == 'right':
                #         keep_going = check_path_positive(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 2
                #             x += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'down':
                #         keep_going = check_path_positive(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 1
                #             y += 5
                #         else:
                #             pass
                #
                #     elif current_direction == 'left':
                #         keep_going = check_path_negative(dx, x, y, packman_width, current_direction)
                #         if keep_going is True:
                #             rotate = 0
                #             x += -5
                #         else:
                #             pass
                #
                #     elif current_direction == 'up':
                #         keep_going = check_path_negative(dy, y, x, packman_height, current_direction)
                #         if keep_going is True:
                #             rotate = 3
                #             y += -5
                #         else:
                #             pass

    elif situation == 3:
        current_direction = new_direction
        new_direction = None
        if current_direction == 'right':
            rotate = 2
        elif current_direction == 'left':
            rotate = 0
        elif current_direction == 'up':
            rotate = 3
        elif current_direction == 'down':
            rotate = 1
        situation = 1

    bx = 50
    by = 200
    gameDisplay.fill(black)
    pygame.draw.line(gameDisplay, blue, (50, 200), (50, 835), 5)
    pygame.draw.line(gameDisplay, blue, (50, 200), (1310, 200), 5)
    pygame.draw.line(gameDisplay, blue, (1310, 835), (1310, 200), 5)
    pygame.draw.line(gameDisplay, blue, (1310, 835), (50, 835), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 490), (bx + 830, by + 490), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 490), (bx + 830, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 490), (bx + 420, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 560), (bx + 830, by + 560), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 70), (bx + 830, by + 70), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 70), (bx + 830, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 140), (bx + 830, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 70), (bx + 420, by + 140), 5)
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 70), (bx + 1050, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 70), (bx + 1190, by + 70), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1190, by + 70), (bx + 1190, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 280), (bx + 1190, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 280), (bx + 1120, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 140), (bx + 1050, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 0), (bx + 980, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 0), (bx + 910, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 140), (bx + 910, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 210), (bx + 1050, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 210), (bx + 1050, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 280), (bx + 910, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 280), (bx + 910, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 350), (bx + 910, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 420), (bx + 1050, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 420), (bx + 1050, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 350), (bx + 1050, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 350), (bx + 1190, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1190, by + 350), (bx + 1190, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 560), (bx + 1190, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 490), (bx + 1050, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1050, by + 490), (bx + 1120, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 1120, by + 490), (bx + 1120, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 980, by + 630), (bx + 980, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 490), (bx + 980, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 910, by + 490), (bx + 910, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 210), (bx + 830, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 830, by + 210), (bx + 830, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 420), (bx + 830, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 210), (bx + 420, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 420, by + 210), (bx + 560, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 560, by + 210), (bx + 560, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 280), (bx + 560, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 280), (bx + 490, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 490, by + 350), (bx + 770, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 770, by + 280), (bx + 770, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 280), (bx + 770, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 700, by + 210), (bx + 700, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 0), (bx + 280, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 140), (bx + 350, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 0), (bx + 350, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 210), (bx + 350, by + 210), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 210), (bx + 350, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 280), (bx + 350, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 210), (bx + 210, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 350), (bx + 350, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 350), (bx + 350, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 420), (bx + 350, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 350), (bx + 210, by + 420), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 490), (bx + 280, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 280, by + 490), (bx + 350, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 350, by + 490), (bx + 350, by + 630), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 70), (bx + 210, by + 70), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 70), (bx + 210, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 140), (bx + 210, by + 140), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 140), (bx + 140, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 280), (bx + 140, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 70), (bx + 70, by + 280), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 350), (bx + 140, by + 350), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 350), (bx + 140, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 140, by + 490), (bx + 210, by + 490), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 210, by + 490), (bx + 210, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 560), (bx + 210, by + 560), 5)  #
    pygame.draw.line(gameDisplay, blue, (bx + 70, by + 350), (bx + 70, by + 560), 5)
    home(x, y, packman_width, dots_x)
    power = special_ability()
    if power is True:
        timer1 = time1 + 7000
    if timer1 > time1:
        for g in all_ghosts:
            g.run = True
        gotcha = busted(x, y, all_ghosts)
        timer = time1
        if gotcha[0] is True:
            gotcha[1].horizontal = 660
            gotcha[1].vertical = 355
            gotcha[1].out = False
            gotcha[1].current_direction = None

    else:
        for g in all_ghosts:
            g.run = False
        free = busted(x, y, all_ghosts)
        if free[0] is True:
            lives -= 1
            timer = time1 + 3000
            x = 610
            y = 775
            rotate = 0
            current_direction = None
            new_direction = None
            situation = 0
            for g in all_ghosts:
                g.horizontal = 660
                g.vertical = 355
                g.out = False
                g.current_direction = None

    for spot in dots_x:
        pygame.draw.circle(gameDisplay, spot.dot_color(), (spot.horizontal, spot.vertical), 5, 0)
    for key in rx.keys():
        for part in rx[key]:
            new_part = list(part)
            start = new_part[0]
            end = new_part[1]
            pygame.draw.line(gameDisplay, black, (key, start), (key, end), 3)
    for key in ry.keys():
        for part in ry[key]:
            new_part = list(part)
            start = new_part[0]
            end = new_part[1]
            pygame.draw.line(gameDisplay, black, (start, key), (end, key), 3)
    packman_starting_point(x, y, rotate)
    if time1 > 6000 + timer:
        blue_ghost.out = True
    smart_movment(blue_ghost, inter, x, y)
    ghost_location(blue_ghost, blue_ghost.horizontal, blue_ghost.vertical, blue_ghost.home_x, blue_ghost.home_y)
    if time1 > 9000 + timer:
        red_ghost.out = True
    ghost_movment(red_ghost, inter)
    ghost_location(red_ghost, red_ghost.horizontal, red_ghost.vertical, red_ghost.home_x, red_ghost.home_y)
    if time1 > 12000 + timer:
        pink_ghost.out = True
    ghost_movment(pink_ghost, inter)
    ghost_location(pink_ghost, pink_ghost.horizontal, pink_ghost.vertical, pink_ghost.home_x, pink_ghost.home_y)
    if time1 > 3000 + timer:
        orange_ghost.out = True
    ghost_movment(orange_ghost, inter)
    ghost_location(orange_ghost, orange_ghost.horizontal, orange_ghost.vertical,
                   orange_ghost.home_x, orange_ghost.home_y)
    pygame.display.update()
    if free is True:
        pygame.time.wait(3000)
    clock.tick(50)
    win(dots_x)

if lives == 0:
    pass
pygame.quit()
quit()
