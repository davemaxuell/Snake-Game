def movement(x_axis, y_axis, input):
    if input == "w":
        return x_axis, y_axis + 20
    elif input == "s":
        return x_axis, y_axis - 20
    elif input == "a":
        return x_axis + 20, y_axis
    elif input == "d":
        return x_axis - 20, y_axis