import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    fig, ax = plt.subplots(1, 2)    

    rnd_2d = np.random.rand(128, 128)    
    ax[0].imshow(rnd_2d)
    ax[0].title.set_text('Random signal')

    my_2d = np.random.rand(128, 128)
    for i in range(128):
        for j in range(128):
            if i % 2 == 0:
                my_2d[i][j] = np.random.randint(1, 4) * j
            else:
                my_2d[i][j] = j

    ax[1].imshow(my_2d)
    ax[1].title.set_text('Custom signal')
            
    fig.tight_layout()
    plt.savefig("./img/2ef.svg")
    plt.show()

