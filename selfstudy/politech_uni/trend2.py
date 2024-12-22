import numpy as np
import matplotlib.pyplot as plt


def trnd_1(x, a):
    y = a[0] * x + a[1]
    return y

def trnd_2(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y

def delta(x, y):
    d = (x - y) / x * 100
    return d


x_input = "-0.8 0.2 0.3 0.6 0.6 0.8 1.0 1.3 1.3 1.5 2.3 2.5 2.9 2.9 3.2 4.2 4.2".split()
y_input = "6.2 2.1 1.8 1.1 1.1 0.7 0.3 0.1 0.1 -0.1 0.2 0.5 1.3 1.3 2.1 6.2 6.2".split()

# x_input = input("x_array: ").split()
# y_input = input("y_array: ").split()
x_list = [float(i) for i in x_input]
x_array = np.array(x_list)
y_list = [float(j) for j in y_input]
y_array = np.array(y_list)

k_1 = np.polyfit(x_array, y_array, 1)
k_2 = np.polyfit(x_array, y_array, 2)

calc_1 = np.array(trnd_1(x_array, k_1))
calc_2 = np.array(trnd_2(x_array, k_2))

delta_1 = np.mean(np.abs(np.array(delta(y_array, calc_1))))
delta_2 = np.mean(np.abs(np.array(delta(y_array, calc_2))))

if delta_1 < delta_2:
    print("First level polinome. K = ", np.round(k_1, 2))
else:
    print("Second level polinome. K = ", np.round(k_2, 2))


a = x_list[0]
b = x_list[-1]
n = 100
h = (b - a) / (n - 1)

x_step = np.array([a + h * i for i in range(n)])
calc_plot_1 = np.array(trnd_1(x_step, k_1))
calc_plot_2 = np.array(trnd_2(x_step, k_2))

plt.plot(x_array, y_array, "go", label="facts")
plt.plot(x_step, calc_plot_1, "g-", label="line")
plt.plot(x_step, calc_plot_2, "b-", label="second")

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.legend(loc="upper center")
plt.show()