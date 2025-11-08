import numpy as np
import matplotlib.pyplot as plt
import scipy.io

def stereoToMono(audiodata):
    newaudiodata = []
    for i in range(len(audiodata)):
        d = (audiodata[i][0] + audiodata[i][1]) / 2
        newaudiodata.append(d)
    return np.array(newaudiodata, dtype='int16')

def plot_fft_spectrogram(audio_path, ax, num_groups=100):
    rate, sgn = scipy.io.wavfile.read(audio_path)
    sgn = stereoToMono(sgn)

    # Split groups
    N = len(sgn)
    group_size = max(1, N // num_groups)
    step = group_size // 2
    groups = []
    start = 0
    while start + group_size <= N:
        groups.append(sgn[start : start + group_size])
        start += step

    # Compute FFT for each group
    fft_mat = [np.abs(np.fft.fft(group))[:len(group)//2] for group in groups]
    fft_mat = np.column_stack(fft_mat)

    # Plot
    im = ax.imshow(
        60 * np.log10(fft_mat + 1e-6),  # magnitude
        origin='lower',
        aspect='auto',
        extent=[0, len(groups), 0, rate/2]
    )
    ax.set_title(audio_path.split('/')[-1])
    ax.set_xlabel('Group')
    ax.set_ylabel('Frequency')
    return im

if __name__ == '__main__':
    files = ['./audio/a.wav', './audio/e.wav', './audio/i.wav', './audio/o.wav']

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for i, file in enumerate(files):
        im = plot_fft_spectrogram(file, axes[i])

    plt.tight_layout()
    plt.savefig('./img/6all.svg')
    plt.show()
