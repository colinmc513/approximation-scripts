# Author: Colin McClure

y_0 = float(input("y_0 = "))
x_0 = float(input("x_0 = "))
h = float(input("h = "))
n_end = int(input("When do you want to end the approximation? n_end = "))

y_values = [y_0]
x_values = [x_0]
n = 0

# The multi-variable function given in equation (6) from document Test 2B
def f(x, y):
    return (2 * x) + y

# Using equations (3) and (4) from document Test 2B
for _ in range(n_end):
    new_y = y_values[n] + f(x_values[n], y_values[n]) * h
    y_values.append(new_y)
    new_x = x_values[n] + h
    x_values.append(new_x)
    print("Generation " + str(n + 1))
    print("----------------")
    print("x = " + str(new_x))
    print("y = " + str(new_y))
    print("----------------")
    n = n + 1
