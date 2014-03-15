import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave
import sys


def read_file(filename):
    raw = wave.open(filename)
    signal = raw.readframes(-1)
    data = np.fromstring(signal, 'Int16')
    if raw.getnchannels() == 2:
        data = data[::2]
    rate= raw.getframerate()
    return rate, data

def normalize(data):
    data_max = max([abs(val) for val in data])
    new_range_val = 1
    data = [float(val)/data_max * new_range_val for val in data]
    return data

def split(data):
    number_bins = len(data)/500
    bins = {}
    for i in range(0,number_bins+1):
        bins["bin_%s" % i] = []
    for sample_i in range(len(data)):
        bin_num = int(sample_i/500)
        bins["bin_%s" % bin_num].append(data[sample_i])
    return bins

def plot_wave(rate, data):
    Time=np.linspace(0, len(data)/rate, num=len(data))

    plt.title('Wave')
    plt.plot(Time,data)
    return plt.show()


def get_ffts(bins):
    for key in bins:
        np.fft.hfft(bins[key])
    return bins


def get_max_ffts(bins):
    max_ffts = []
    for key in bins:
        max_fft = max(bins[key])
        max_ffts.append(max_fft)
    return max_ffts

# def plot_ffts(max_ffts):
#     # X_axis = np.linspace(0,99)
#     Y_axis = np.linspace(0,1)
#     plt.plot(max_ffts, Y_axis)
#     return plt.show()

def get_freqs(data):
    # array = bins["bin_1"]
    freq = np.fft.fftfreq(data)
    return freq

    

    









rate, data = read_file("Alohamora_1.wav")
data = normalize(data)
# print plot_wave(rate, data)

bins = split(data)

# bins = get_ffts(bins)

# print get_freqs(bins)

# max_ffts = get_max_ffts(bins)




# fft_1 = get_fft(bins["bin_1"])
# fft_2 = get_fft(bins["bin_2"])
# fft_3 = get_fft(bins["bin_3"])
# fft_4 = get_fft(bins["bin_4"])
# fft_5 = get_fft(bins["bin_5"])





# print data
# print ffts["fft_1"]
# print max(fft_2)
# print max(fft_3)
# print max(fft_4)
# print max(fft_5)
# print plot_wave(rate, data)
# print fft
# print get_fft(data)


# print split(data)













