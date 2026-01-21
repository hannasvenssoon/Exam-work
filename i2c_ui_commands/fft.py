"""import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

df_abnormal = pd.read_csv("dataset_1767782044.csv", sep=';', header=None, names=['x','y','z'])
#df_normal   = pd.read_csv("test_normal.csv",   sep=';', header=None, names=['x','y','z'])

fs = 1000  

def compute_fft(signal, fs):
    signal = signal - np.mean(signal)
    N = len(signal)
    
    fft_vals = np.fft.fft(signal)
    fft_vals = np.abs(fft_vals) / N
    freqs = np.fft.fftfreq(N, 1/fs)

    mask = freqs >= 0
    return freqs[mask], fft_vals[mask]

freqs_abnormal, fft_abnormal = compute_fft(df_abnormal["z"].values, fs)
#freqs_normal,   fft_normal   = compute_fft(df_normal["z"].values,   fs)

plt.figure(figsize=(12,6))
plt.plot(freqs_abnormal, fft_abnormal)
plt.title("FFT - Abnormal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("fft_abnormali2c_output.png")
plt.close()

plt.figure(figsize=(12,6))
plt.plot(freqs_normal, fft_normal)
plt.title("FFT - Normal")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig("normal_output.png")
plt.close()"""
import numpy as np
import pandas as pd
import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os



df = pd.read_csv(
    "dataset_normal_2026-01-20_15-29-16.csv",
    #"dataset_abnormal30hz_2026-01-20_15-39-23.csv",
    sep=',',
    decimal='.'
)

fs = 3300

z = df["az"].values
z = z - np.mean(z)
plt.figure(figsize=(12,6))
plt.plot(z)
plt.show()

fft_vals = np.abs(np.fft.fft(z))      
freqs = np.fft.fftfreq(len(z), 1/fs)

mask = freqs >= 0
freqs = freqs[mask]
fft_vals = fft_vals[mask]

plt.figure(figsize=(12,6))
plt.plot(freqs, fft_vals)
plt.xlim(0, fs/2)
plt.ylim(0, np.max(fft_vals)*1.1)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.title("FFT - normal")
plt.grid(True)
plt.tight_layout()
plt.show()
#plt.close()

#print("Saved to:", os.path.abspath("abnormal.png"))