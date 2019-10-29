from random import randint


def battleship(n):

  enemy_coordinates = generate_coordinates(n)
  enemy_grid = generate_grid(n, enemy_coordinates)

  player_coordinates = generate_coordinates(n)
  player_grid = generate_grid(n, player_coordinates)

  start_game(enemy_coordinates, enemy_grid, player_coordinates, player_grid)


def start_game(enemy_coordinates, enemy_grid, player_coordinates, player_grid):

    ask_mode = input("Do you want to play in god mode?\nIf so, enter 'Y' for yes.\n")
    mode = 0
    if mode == 'Y':
      cheat_code = input("Enter cheat code!\n")
      if cheat_code == "1234":
          mode = 1
      else:
          print("Wrong cheat code. You're now playing in normal mode.\n")

    strike_counts=[0,0]
    while strike_counts[0] < 2 or strike_counts[1] < 2:
        strike_counts[0] = fire_shots() 
          


def generate_coordinates(n):
    
    coordinates = [[4,4], [0,0]]
    while coordinates[0][0] and coordinates[0][1] == 4:
        coordinates[0] = [randint(0,4), randint(0,4)]
    orientation = randint(0,1)
    
    # horizontal orientation
    if orientation == 0:
        if coordinates[0][0] != 4: # ensures battlehsips are within grid
            coordinates[1][0] = coordinates[0][0] + 1
            coordinates[1][1] = coordinates[0][1]
        else: # if not, forces all last column ships to be vertical
            coordinates[1][0] = coordinates[0][0]
            coordinates[1][1] = coordinates[0][1] + 1

    # vertical orientation
    elif orientation == 1:
        if coordinates[0][1] != 4: # ensures battlehsips are within grid
            coordinates[1][0] = coordinates[0][0]
            coordinates[1][1] = coordinates[0][1] + 1
        else: # if not, forces all last row ships to be horizontal
            coordinates[1][0] = coordinates[0][0] + 1
            coordinates[1][1] = coordinates[0][1]

    return coordinates


def generate_grid(n, coordinates):

    grid = ""
    for i in range(n): # Y (vertical) coordinates
      for j in range(n): # X (horizontal) coordinates
        if j == coordinates[0][0] and i == coordinates[0][1]:
          grid += "||"
        elif j == coordinates[1][0] and i == coordinates[1][1]:
          grid += "||"
        else:
          grid += "~~"     
      grid += "\n"

    return grid


def fire_shots(coordinates, viewable_grid=""):

    print(viewable_grid)

    hit = "\nENEMY BATTLESHIP HIT!\n    |||  \n \-****-/ \n~~~~~~~~~~\n"
    sink = "ENEMY BATTLESHIP SUNK!\n\n  S.O.S.  \n~~~~~~~~~~\n"
    miss = "\nMISSED! ADJUST FIRE!\n"
    c = 0
    s = 0
    while c < 2:
        attack_coordinates = [0,0]
        input_coordinates =  int(input("Input grids coordinate, between 1 and 5, and press ENTER!\n"))
        attack_coordinates[0] = (input_coordinates // 10) - 1
        attack_coordinates[1] = (input_coordinates % 10) - 1

        for coordinate in coordinates:
          s = 0
          if coordinate == attack_coordinates:
            print(hit)
            c += 1
            s = 1
            break

        if c == 2:
            print(sink)
        elif s == 0:
            print(miss)


battleship(5)