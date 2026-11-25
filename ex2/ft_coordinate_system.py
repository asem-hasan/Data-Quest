import math


def get_player_pos() -> tuple[float, float, float]:
    flag = True
    while flag:
        try:
            arg = input("Enter new coordinates as floats in format ’x,y,z’: ")
            args = arg.split(",")
            if len(args) != 3:
                print("Invalid syntax")
            else:
                i = 0
                while i < len(args):
                    num = float(args[i])
                    i += 1
                x = float(args[0])
                y = float(args[1])
                z = num
                flag = False
        except ValueError as Error:
            print(f"Error on parameter ’{args[i]}’: {Error}")

    return (x, y, z)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    x_o, y_o, z_o = get_player_pos()
    print(f"Got a first tuple: ({x_o}, {y_o}, {z_o})")
    print(f"It includes: X={x_o}, Y={y_o}, Z={z_o}")
    distance = math.sqrt((x_o - 0)**2 + (y_o - 0)**2 + (z_o - 0)**2)
    print(f"Distance to center: {distance:.4f}\n")
    print("Get a second set of coordinates")
    x_t, y_t, z_t = get_player_pos()
    distance = math.sqrt((x_t - x_o)**2 + (y_t - y_o)**2 + (z_t - z_o)**2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")
