from random import randint

def battleship(n):

    coordinates = [[4,4], [0,0]]
    while coordinates[0][0] and coordinates[0][1] == 4:
        coordinates[0] = generate_coordinates()
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


    print(coordinates[0][0], coordinates[0][1])
    print(coordinates[1][0], coordinates[1][1])


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

    print(grid)

    fire_shots(coordinates)


def fire_shots(coordinates):

    hit = "\nENEMY BATTLESHIP HIT!\n    |||  \n \-****-/ \n~~~~~~~~~~\n"
    sink = "ENEMY BATTLESHIP SUNK!\n\n  S.O.S.  \n~~~~~~~~~~\n"
    miss = "\nMISSED! ADJUST FIRE!\n"
    c = 0
    s = 0
    while c < 2:

        attack_coordinates = [0,0]
        attack_coordinates[0] = int(input("Input horizontal grid coordinate and press ENTER!\n"))
        attack_coordinates[1] = int(input("Input vertical grid coordinate and press ENTER!\n"))

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


def generate_coordinates():
    x, y = randint(0,4), randint(0,4)
    return [x, y]

battleship(5)