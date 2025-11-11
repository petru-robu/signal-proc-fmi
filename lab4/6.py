import numpy as np
import matplotlib.pyplot as plt
import scipy

def stereoToMono(sgn):
    if sgn.ndim == 2:
        return sgn.mean(axis=1)

if __name__ == '__main__':
    # Read signal
    audio_path = './audio/cargo.wav'
    rate, sgn = scipy.io.wavfile.read(audio_path)
    sgn = stereoToMono(sgn).astype(np.float32)
    sgn = sgn[:len(sgn)//8]

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

    #ax.plot(sgn)
    ax.set_xlabel('Group')
    ax.set_ylabel('Frequency')
    ax.set_title(f"My spectrogram of {audio_path.split('/')[-1]}")
    fig.colorbar(im, ax=ax, label='Magnitude')



    plt.tight_layout()
    plt.savefig('./img/6.svg')
    plt.show()
