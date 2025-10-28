import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(num, x, y, circ):
    circ.set_data(x[:num], y[:num])
    return circ

fig, ax = plt.subplots(2)

N = 1000
freq = 10

#plot the signal
x = np.linspace(0, 1, N)
x_n = np.sin(2 * freq * np.pi * x)
ax[0].plot(x, x_n)

#plot the circles
for u in [1, 2, 5, 7, 13]:
    y_n = x_n * np.exp(-2j * np.pi * u * x)
    ax[1].set_aspect('equal')
    ax[1].plot(np.real(y_n), np.imag(y_n))
    plt.savefig(f'circle_{u}hz.svg')
    plt.cla()

u = 2
y_n = x_n * np.exp(-2j * np.pi * u * x)
ax[1].set_aspect('equal')
ax[1].plot(np.real(y_n), np.imag(y_n))

plt.show()