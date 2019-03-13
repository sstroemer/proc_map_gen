import random
import copy

# ------------------------------------------------------------------------------------------------------------- SETTINGS
CA_INITIAL_PERCENTAGE = 0.4

CA_PRE_RUNS = 4
CA_SMOOTH_RUNS = 3

CA_N2SURVIVE = 5
CA_N2SPAWN = 0


# ------------------------------------------------------------------------------------------------------------------ RUN
def run(map):
    width = len(map)
    height = len(map[0])
    
    # first, we fill the map randomly. every cell has a given chance to turn into a wall
    for x in range(width):
        for y in range(height):
            map[x][y] = 1 if (random.random() < CA_INITIAL_PERCENTAGE) else 0

    fix_map(map)

    # we now apply a modified smoothing that reduces the chance of single big caves
    for i in range(CA_PRE_RUNS):
        pre_smooth(map)
#        fix_map(map)

    # now the final smoothing
    for i in range(CA_SMOOTH_RUNS):
        smooth(map)
#        fix_map(map)

    fix_map(map)


# ----------------------------------------------------------------------------------------------------------- PRE SMOOTH
def pre_smooth(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        for y in range(height):
            nb = neighbours(tmp, x, y)
            map[x][y] = 1 if (nb >= CA_N2SURVIVE or nb <= CA_N2SPAWN) else 0


# ----------------------------------------------------------------------------------------------------------- PRE SMOOTH
def smooth(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        for y in range(height):
            nb = neighbours(tmp, x, y)
            map[x][y] = 1 if (nb >= CA_N2SURVIVE) else 0


# ----------------------------------------------------------------------------------------------------------- NEIGHBOURS
def neighbours(map, x, y):
    width = len(map)
    height = len(map[0])

    nb = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if 0 <= i < width and 0 <= j < height:
                nb = nb + map[i][j]

    return nb


def fix_map(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        map[x][0] = 1
        map[x][height-1] = 1

    for y in range(height):
        map[0][y] = 1
        map[width-1][y] = 1
