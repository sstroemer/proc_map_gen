import random
import copy

# ------------------------------------------------------------------------------------------------------------- SETTINGS
SCA_INITIAL_PERCENTAGE = 0.4

SCA_PRE_RUNS = 3
SCA_SMOOTH_RUNS = 5
SCA_NONSTOCH_RUNS = 2
SCA_SURVIVE = 5


# ------------------------------------------------------------------------------------------------------------------ RUN
def run(map):
    width = len(map)
    height = len(map[0])

    # first, we fill the map randomly. every cell has a given chance to turn into a wall
    for x in range(width):
        for y in range(height):
            map[x][y] = 1 if (random.random() < SCA_INITIAL_PERCENTAGE) else 0

    # we now apply a modified smoothing that applies a spawning percentage
    for i in range(SCA_PRE_RUNS):
        pre_smooth(map)

    # stochastic smoothing (without spawning)
    for i in range(SCA_SMOOTH_RUNS):
        smooth(map)

    # now the final smoothing
    for i in range(SCA_NONSTOCH_RUNS):
        smooth(map)


# ----------------------------------------------------------------------------------------------------------- PRE SMOOTH
def pre_smooth(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        for y in range(height):
            nb = neighbours(tmp, x, y)
            map[x][y] = 1 if (random.random() <= survive(nb) or random.random() <= spawn(nb)) else 0


# ----------------------------------------------------------------------------------------------------------- PRE SMOOTH
def smooth(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        for y in range(height):
            nb = neighbours(tmp, x, y)
            map[x][y] = 1 if (random.random() <= survive(nb)) else 0


# ------------------------------------------------------------------------------------------------------------ NON STOCH
def non_stoch(map):
    width = len(map)
    height = len(map[0])

    tmp = copy.deepcopy(map)

    for x in range(width):
        for y in range(height):
            nb = neighbours(tmp, x, y)
            map[x][y] = 1 if (nb >= SCA_SURVIVE) else 0


# ----------------------------------------------------------------------------------------------------------- NEIGHBOURS
def neighbours(map, x, y):
    width = len(map)
    height = len(map[0])

    nb = 0
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= i < width and 0 <= j < height:
                nb = nb + map[i][j]

    return nb


# -------------------------------------------------------------------------------------------------------------- SURVIVE
def survive(neighbours):
    chance = [0.0, 0.05, 0.10, 0.25, 0.40, 0.55, 0.70, 0.85, 0.90, 0.95]
    return chance[neighbours]


# -------------------------------------------------------------------------------------------------------------- SURVIVE
def spawn(neighbours):
    chance = [0.90, 0.80, 0.50, 0.10, 0.05, 0.03, 0.01, 0.01, 0.01, 0.01]
    return chance[neighbours]

