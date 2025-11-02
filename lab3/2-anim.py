import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(num, x, y, circ, xs, ys, signal, point_signal, point_circle):
    circ.set_data(x[:num], y[:num])        
    signal.set_data(xs[:num], ys[:num])    
    point_signal.set_data(xs[num-1], ys[num-1])
    point_circle.set_data(x[num-1], y[num-1])
    return circ, signal, point_signal, point_circle

fig, ax = plt.subplots(2, 1, figsize=(6, 8))

N = 1000
freq = 10
x = np.linspace(0, 1, N)
x_n = np.sin(2 * freq * np.pi * x)

# circle
u = 4
y_n = x_n * np.exp(-2j * np.pi * u * x)

# Signal plot
ax[0].set_xlim(0, 1)
ax[0].axhline(0, color='k', linewidth=1)
ax[0].set_ylim(-1.1, 1.1)
ax[0].set_title("Sine Wave (Signal)")
signal, = ax[0].plot([], [], lw=2, color='tab:blue')
point_signal, = ax[0].plot([], [], 'ro', markersize=6)

# Circle plot
ax[1].set_aspect('equal')
ax[1].set_xlim(-1.1, 1.1)
ax[1].set_ylim(-1.1, 1.1)
ax[1].set_title(f'wrapping freq = {u}')
circ, = ax[1].plot([], [], lw=2, color='tab:red')
point_circle, = ax[1].plot([], [], 'bo', markersize=6)

anim = animation.FuncAnimation(
    fig, animate, frames=N, interval=10,
    fargs=[np.real(y_n), np.imag(y_n), circ, x, x_n, signal, point_signal, point_circle],
    blit=True
)

plt.tight_layout()
anim.save('./img/2.gif', writer='ffmpeg', fps=30)
plt.show()