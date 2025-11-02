import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    samples = 100_000
    alpha = np.linspace(-np.pi/2, np.pi/2, samples)

    fig, ax = plt.subplots(2, 2, figsize=(12,14))

    # first plot
    p_sin, = ax[0,0].plot(alpha, np.sin(alpha), color='purple')
    p_lin, = ax[0,0].plot(alpha, alpha, color='y')
    p_err, = ax[0,0].plot(alpha, np.abs(np.sin(alpha) - alpha), color='g')

    p_sin.set_label('sin(x)')
    p_lin.set_label('x')
    p_err.set_label('|sin(x)-x|')

    ax[0,0].grid()
    ax[0,0].set_title('sin(x) vs x')
    ax[0,0].legend()

    # first plot logarithmic
    p_sin, = ax[1,0].plot(alpha, np.log10(np.sin(alpha)), color='purple')
    p_lin, = ax[1,0].plot(alpha, np.log10(alpha), color='y')
    p_err, = ax[1,0].plot(alpha, np.log10(np.abs(np.sin(alpha) - alpha)), color='g')

    p_sin.set_label('sin(x)')
    p_lin.set_label('x')
    p_err.set_label('|sin(x)-x|')

    ax[1,0].grid()
    ax[1,0].set_title('sin(x) vs x logarithmic')
    ax[1,0].legend()


    # second plot
    pade = (alpha - (7 * alpha**3 / 60))/(1 + alpha**2/20)
    p_pade, = ax[0,1].plot(alpha, np.sin(alpha), color='purple')
    p_sin, = ax[0,1].plot(alpha, pade, color='y')
    p_err, = ax[0,1].plot(alpha, np.abs(pade - np.sin(alpha)), color='g')

    p_sin.set_label('sin(x)')
    p_pade.set_label('pade')
    p_err.set_label('|sin(x) - pade|')

    ax[0,1].grid()
    ax[0,1].set_title('sin(x) vs pade')
    ax[0,1].legend()

    # second plot logarithmic
    pade = (alpha - (7 * alpha**3 / 60))/(1 + alpha**2/20)
    p_pade, = ax[1,1].plot(alpha, np.log10(np.sin(alpha)), color='purple')
    p_sin, = ax[1,1].plot(alpha, np.log10(pade), color='y')
    p_err, = ax[1,1].plot(alpha, np.log10(np.abs(pade - np.sin(alpha))), color='g')

    p_sin.set_label('sin(x)')
    p_pade.set_label('pade')
    p_err.set_label('|sin(x) - pade|')

    ax[1,1].grid()
    ax[1,1].set_title('sin(x) vs pade logarithmic')
    ax[1,1].legend()



    plt.tight_layout()
    plt.savefig("./img/8.svg")
    plt.show()