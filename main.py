import algo_ca
import algo_sca


# ----------------------------------------------------------------------------------------------------------------- main
def main():
    width = int(input("Enter map width: "))
    height = int(input("Enter map height: "))

    # generate map
    map = [0] * width
    for i in range(width):
        map[i] = [0] * height

    print("Available algorithms: ")
    print("[1] Basic cellular automaton.")
    print("[2] Stochastic cellular automaton.")

    selection = int(input("Which one should I use? "))

    if selection == 1:
        algo_ca.run(map)
    if selection == 2:
        algo_sca.run(map)

    print_map(map)
# ------------------------------------------------------------------------------------------------------------- end main


# ------------------------------------------------------------------------------------------------------------- printMap
def print_map(map):
    width  = len(map)
    height = len(map[0])

    for y in range(height):
        for x in range(width):
            print('#' if map[x][y]==1 else '.', end='')
        print("")


if __name__ == '__main__':
    main()