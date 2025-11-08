import numpy as np
import matplotlib.pyplot as plt
import scipy

def stereoToMono(audiodata):
    newaudiodata = []
    for i in range(len(audiodata)):
        d = (audiodata[i][0] + audiodata[i][1]) / 2
        newaudiodata.append(d)
    return np.array(newaudiodata, dtype='int16')

if __name__ == '__main__':
    # Read signal
    audio_path = './audio/a.wav'
    rate, sgn = scipy.io.wavfile.read(audio_path)
    sgn = stereoToMono(sgn)

    # Split in groups
    N = len(sgn)
    group_size = max(1, N // 100)
    step = group_size // 2
    groups = []
    start = 0

    while start + group_size <= N:
        groups.append(sgn[start : start+group_size])
        start += step

    print(f"Signal length: {N}\nGroup size: {group_size}\nGroup count: {len(groups)}")

    # FFT for every group
    fft_mat = []
    for group in groups:
        gr_fft = np.abs(np.fft.fft(group))
        fft_mat.append(gr_fft[:len(gr_fft)//2])  # positive frequencies only

    fft_mat = np.column_stack(fft_mat)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(
        60 * np.log10(fft_mat + 1e-6),  # dB
        origin='lower',
        aspect='auto',
        extent=[0, len(groups), 0, rate/2]
    )

    ax.set_xlabel('Group')
    ax.set_ylabel('Frequency')
    fig.colorbar(im, ax=ax, label='Magnitude')

    plt.tight_layout()
    plt.savefig('./img/6.svg')
    plt.show()
