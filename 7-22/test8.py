for z in [[x, y, x*y] for x in range(1, 10) for y in range(1, x+1)]:
    if z[2] > 9:
        print("{}*{}={}".format(z[0], z[1], z[2]), end=" ")
    else:
        print("{}*{}={}".format(z[0], z[1], z[2]), end="  ")
    if z[0] == z[1]:
        print("\n")