import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave
import sys
import math
from scipy.fftpack import dct
import itertools
import os



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

def get_threshhold(data, thresh=.15):
    for i in range(len(data)):
        if data[i] >= thresh:
            return i

def get_end(data, end_thresh=.1):
    for i in reversed(range(len(data))):
        if data[i] >= end_thresh:
            return i

def new_data_start(data, threshhold, end, min_len=40000):
    data = data[threshhold:end]
    if len(data) >= min_len:
        return data
    else:
        return [0] * len(data)


def split(data, bin_len=400, bin_overlap=160):
    bins = []
    for i in range(0,len(data), bin_len-bin_overlap):
        bins.append(data[i:i+bin_len])
    if len(bins[-1]) != bin_len: # if last bin is short of len
        bins[-1] += [0] * (bin_len - len(bins[-1])) # zero pad it
    if len(bins[-2]) != bin_len: # if last bin is short of len
        bins[-2] += [0] * (bin_len - len(bins[-2]))
    num_of_bins = len(bins)
    return bins

def freq_split(data, bin_len=400, bin_overlap=0):
    f_bins = []
    for i in range(0,len(data), bin_len-bin_overlap):
        f_bins.append(data[i:i+bin_len])
    if len(f_bins[-1]) != bin_len: # if last bin is short of len
        f_bins[-1] += [0] * (bin_len - len(f_bins[-1])) # zero pad it
    return f_bins

def get_power_spectrum(bins):
    power_spectrum = []
    for bin in bins:
        spectrum = np.fft.rfft(bin)
        magnitude = np.absolute(spectrum)
        power = np.square(magnitude)
        power_spectrum.append(power)
    return power_spectrum

def get_frequency(f_bins):
    frequencies = []
    for bin in f_bins:
        w = np.fft.fft(bin)
        freqs = np.fft.fftfreq(len(bin))
        idx = np.argmax(np.abs(w)**2)
        freq = freqs[idx]
        freq_hz = abs(freq*40000)
        frequencies.append(freq_hz)
    # average_freq = sum(frequencies)/len(frequencies)
    return frequencies

def hertz_mels(hertz):
    mels = 2595 * np.log10(1+hertz/700.0)
    return mels

def mels_hertz(mels):
    hertz = 700*(10**(mels/2595.0)-1)
    return hertz

def mel_filterbank(power_spectrum):
    block_size = int(len(power_spectrum[0]))
    num_bands = int(13)
    min_hz = 0
    max_hz = 3000
    max_mel = int(hertz_mels(max_hz))
    min_mel = int(mels_hertz(min_hz))

    filter_matrix = np.zeros((num_bands, block_size))

    mel_range = np.array(xrange(num_bands + 2))

    mel_centers = mel_range * (max_mel - min_mel)/(num_bands + 1) + min_mel

    aux = np.log(1 + 1000.0 / 700.0) / 1000.0
    aux = (np.exp(mel_centers * aux) -1) / 22050
    aux = 0.5 + 700 * block_size * aux
    aux = np.floor(aux)
    center_index = np.array(aux, int)


    for i in xrange(num_bands):
        start, center, end = center_index[i:i + 3]
        k1 = np.float32(center - start)
        k2 = np.float32(end - center)
        up = (np.array(xrange(start, center)) - start) / k1
        down = (end - np.array(xrange(center, end))) / k2

        filter_matrix[i][start:center] = up
        filter_matrix[i][center:end] = down

    return filter_matrix.transpose()

def MFCC(power_spectrum, filter_matrix):
    dct_spectrum = []
    for power in power_spectrum:
        filtered_spectrum = np.dot(power, filter_matrix)
        log_spectrum = np.log(filtered_spectrum)
        dct_item= dct(log_spectrum, type=2)
        dct_spectrum.append(dct_item)
    return dct_spectrum

def get_average(dct_spectrum):
    #take average MFCC for each bin
    avg_spectrum = []
    for each in dct_spectrum:
        avg = sum(each)/len(each)
        avg_spectrum.append(avg)
    return avg_spectrum

# def un_split(dct_spectrum):
#     new_dct_spectrum = [item for sublist in dct_spectrum for item in sublist]

#     # new_dct_spectrum = []
#     # for dct_item in dct_spectrum:
#     #     for item in dct_item:
#     #         new_dct_spectrum.append(item)
#     return new_dct_spectrum


def plot_wave(rate, data):
    Time=np.linspace(0, len(data)/rate, num=len(data))

    plt.title('Wave')
    plt.plot(Time,data)
    return plt.show()


def master(filename):
    rate, data = read_file(filename)
    data = normalize(data)
    threshhold = get_threshhold(data)
    end = get_end(data)
    data = new_data_start(data, threshhold, end)
    bins = split(data)
    # f_bins = freq_split(data)
    # hertz = get_frequency(f_bins)
    power_spectrum = get_power_spectrum(bins)
    filter_matrix = mel_filterbank(power_spectrum)
    dct_spectrum = MFCC(power_spectrum, filter_matrix)
    avg_spectrum = get_average(dct_spectrum)


    # new_dct_spectrum = un_split(dct_spectrum)

    # plt.show() = plot_wave(rate, data)

    return avg_spectrum
    

# print master(os.path.abspath("audios/input_full_len.wav"))
# print master(os.path.abspath("audios/tone_2.wav"))
# print master(os.path.abspath("test.wav"))
# rate, data = read_file("Alohamora_1.wav")
# data = normalize(data)
# print data[0:100]


    

















