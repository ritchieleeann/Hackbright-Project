import scipy.io.wavfile
import numpy as np
import matplotlib.pyplot as plt
import wave
import sys
import math


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
    return bins[-1]

def power_spectrum(bins):
    spectrum = np.fft.rfft(bins)
    magnitude = np.absolute(spectrum)
    power_spectrum = np.square(magnitude)
    return power_spectrum

def hertz_mels(hertz):
    mels = 2595 * np.log10(1+hertz/700.0)
    return mels

def mels_hertz(mels):
    hertz = 700*(10**(mels/2595.0)-1)
    return hertz


def plot_wave(rate, data):
    Time=np.linspace(0, len(data)/rate, num=len(data))

    plt.title('Wave')
    plt.plot(Time,data)
    return plt.show()

def get_filterbanks(nfilt=40,nfft=400,samplerate=16000,lowfreq=0, highfreq=8000):

    # highfreq= highfreq or samplerate/2
    
    # compute points evenly spaced in mels
    low_mel = hertz_mels(lowfreq)
    high_mel = hertz_mels(highfreq)
    mel_points = np.linspace(low_mel,high_mel,nfilt+2)
    # our points are in Hz, but we use fft bins, so we have to convert
    #  from Hz to fft bin number
    bin = np.floor((nfft+1)*mels_hertz(mel_points)/samplerate)

    fbank = np.zeros([nfilt,nfft/2+1])
    for j in xrange(0,nfilt):
        for i in xrange(int(bin[j]),int(bin[j+1])):
            fbank[j,i] = (i - bin[j])/(bin[j+1]-bin[j])
        for i in xrange(int(bin[j+1]),int(bin[j+2])):
            fbank[j,i] = (bin[j+2]-i)/(bin[j+2]-bin[j+1])
    return mel_points, fbank

def fbank(power_spectrum,fbank,samplerate=16000,nfilt=40,nfft=400,lowfreq=0,highfreq=8000):
         
    energy = np.sum(power_spectrum) # this stores the total energy in each frame
    
 
    feature = np.dot(power_spectrum,fbank) # compute the filterbank energies
    feature = np.log(feature)
    return energy 

def mfcc(feature, energy, numcep=13, appendEnergy=True):
    feature = dct(feature)[:,:numcep]
    if appendEnergy: feat[:,0] = numpy.log(energy) # replace first cepstral coefficient with log of frame energy
    return feature




rate, data = read_file("Alohamora_1.wav")
data = normalize(data)
bins = split(data)
# print bins
print power_spectrum(bins)

# print get_filterbanks(nfilt=40,samplerate=16000,lowfreq=0, highfreq=8000)
# print fbank(power_spectrum,fbank,samplerate=16000,nfilt=40,nfft=400,lowfreq=0,highfreq=8000)
# print mfcc(feature, numcep=13)



# print power_spectrum


# print len(data)
# bins, num_bins = split(data)
# print num_bins
# print plot_wave(rate, power_spectrum)

















# print plot_wave(rate, data)

# bins = split(data)

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













