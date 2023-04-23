y_0 = float(input("y_0 = "))
x_0 = float(input("x_0 = "))
h = float(input("h = "))
n_end = int(input("When do you want to end the approximation? n_end = "))

y_values = [y_0]
y_hat_values = []
x_values = [x_0]
n = 0

# The multi-variable function given in equation (1) from document Test 2B
def f(x, y):
    return (2 * x) + y

# Using equations (7) and (8) from document Test 2B
for _ in range(n_end):
    new_x = x_values[n] + h
    x_values.append(new_x)
    f1 = f(x_values[n], y_values[n])
    y_hat = y_values[n] + f1 * h
    y_hat_values.append(y_hat)
    f2 = f(new_x, y_hat)
    new_y = y_values[n] + ((f1 + f2) / 2) * h
    y_values.append(new_y)
    print("----------------")
    print("Generation " + str(n + 1))
    print("----------------")
    print("x = " + str(new_x))
    print("y-hat = " + str(y_hat))
    print("y = " + str(new_y))
    print("----------------")
    n = n + 1
