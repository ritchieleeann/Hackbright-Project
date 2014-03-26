import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave
import sys
import math
from scipy.fftpack import dct

num_coefficients = 13 
min_hz = 0
max_hz= 8000



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


def split(data, bin_len=400, bin_overlap=160):
    bins = []
    for i in range(0,len(data), bin_len-bin_overlap):
        bins.append(data[i:i+bin_len])
    if len(bins[-1]) != bin_len: # if last bin is short of len
        bins[-1] += [0] * (bin_len - len(bins[-1])) # zero pad it
    num_of_bins = len(bins)
    return bins


def power_spectrum(bins):
    power_spectrum = []
    for bin in bins:
        spectrum = np.fft.rfft(bin)
        magnitude = np.absolute(spectrum)
        power = np.square(magnitude)
        power_spectrum.append(power)
    return power_spectrum

def MFCC(power_spectrum, filter_matrix):
    dct_spectrum = []
    for power in power_spectrum:
        filtered_spectrum = np.dot(power, filter_matrix)
        log_spectrum = np.log(filtered_spectrum)
        dct_item= dct(log_spectrum, type=2)
        dct_spectrum.append(dct_item)
    return dct_spectrum

def hertz_mels(hertz):
    mels = 2595 * np.log10(1+hertz/700.0)
    return mels

def mels_hertz(mels):
    hertz = 700*(10**(mels/2595.0)-1)
    return hertz

def mel_filterbank(power_spectrum):
    block_size = int(len(power_spectrum[0]))
    num_bands = int(num_coefficients)
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



def plot_wave(rate, data):
    Time=np.linspace(0, len(data)/rate, num=len(data))

    plt.title('Wave')
    plt.plot(Time,data)
    return plt.show()


def master:
    pass





    


rate, data = read_file("Alohamora_4.wav")
data = normalize(data)
# print len(data)
bins = split(data)
# print "number of bins is %s" % len(bins)
# print "len of each bin is %s" % len(bins[-1])
power_spectrum = power_spectrum(bins)
# print "len of power_spectrum is %s" % len(power_spectrum)
# print "len of each in power_spectrum is %s" % len(power_spectrum[0])
# print power_spectrum[0].shape
filter_matrix = mel_filterbank(power_spectrum)
# print filter_matrix.shape

dct_spectrum = MFCC(power_spectrum, filter_matrix)

print dct_spectrum[0]









# print plot_wave(rate, data)















