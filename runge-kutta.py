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

# Using equations (9), (10), and (11) from document Test 2B
for _ in range(n_end):
    x = x_values[n]
    y = y_values[n]
    k1 = h * f(x, y)
    k2 = h * f((x + (h/2)), (y + (k1 / 2)))
    k3 = h * f((x + (h/2)), (y + (k2 / 2)))
    k4 = h * f((x + h), (y + k3))
    K = (1/6) * (k1 + (2 * k2) + (2 * k3) + k4)
    new_x = x + h
    new_y = y + K
    x_values.append(new_x)
    y_values.append(new_y)
    print("----------------")
    print("Generation " + str(n + 1))
    print("----------------")
    print("x = " + str(new_x))
    print("y = " + str(new_y))
    print("----------------")
    n += 1
