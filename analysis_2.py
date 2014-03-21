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


# def split(data, bin_len=400, bin_overlap=160):
#     bins = []
#     for i in range(0,len(data), bin_len-bin_overlap):
#         bins.append(data[i:i+bin_len])
#     if len(bins[-1]) != bin_len: # if last bin is short of len
#         bins[-1] += [0] * (bin_len - len(bins[-1])) # zero pad it
#     return bins

def split(data,bin_len=400,bin_step=160,winfunc=lambda x:np.ones((1,x))):
    datalen = len(data)
    if datalen <= bin_len: 
        numbins = 1
    else:
        numbins = 1 + math.ceil((1.0*datalen - bin_len)/bin_step)
        
    padlen = (numbins-1)*bin_step + bin_len
    
    zeros = np.zeros((padlen - datalen,))
    padsignal = np.concatenate((data,zeros))
    
    indices = np.tile(np.arange(0,bin_len),(numbins,1)) + np.tile(np.arange(0,numbins*bin_step,bin_step),(bin_len,1)).T
    indices = np.array(indices,dtype=np.int32)
    bins = padsignal[indices]
    win = np.tile(winfunc(bin_len),(numbins,1))
    return bins*win

def power_spectrum(bins, nFFT=512):
    spectrum = np.fft.rfft(bins,nFFT)
    magnitude = np.absolute(spectrum)
    power_spectrum = 1.0/nFFT*np.square(magnitude)
    return power_spectrum

def hertz_mels(hertz):
    mels = 2595 * np.log10(1+hertz/700.0)
    return mels

def mels_hertz(mels):
    hertz = 700*(10**(mels/2595.0)-1)
    return hertz

def preemphasis(signal,coeff=0.95):   
    return np.append(signal[0],signal[1:]-coeff*signal[:-1])


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
    return fbank

def fbank(data,bins,samplerate=16000,winlen=0.025,winstep=0.01,
          nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97):        
    # highfreq= highfreq or samplerate/2
    signal = preemphasis(data,preemph)
    frames = split(signal, winlen*samplerate, winstep*samplerate)
    pspec = power_spectrum(bins,nfft)
    energy = np.sum(pspec,1) # this stores the total energy in each frame
    
    fb = get_filterbanks(nfilt,nfft,samplerate)
    feat = np.dot(pspec,fb.T) # compute the filterbank energies
    return feat,energy

def logfbank(signal,samplerate=16000,winlen=0.025,winstep=0.01,
          nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97):        
    feat,energy = fbank(signal,samplerate,winlen,winstep,nfilt,nfft,lowfreq,highfreq,preemph)
    return np.log(feat)


# def fbank(power_spectrum,fbank,samplerate=16000,nfilt=40,nfft=400,lowfreq=0,highfreq=8000):
         
#     energy = np.sum(power_spectrum) # this stores the total energy in each frame
    
 
#     feature = np.dot(power_spectrum,fbank) # compute the filterbank energies
#     feature = np.log(feature)
#     return feature,energy 


def mfcc(signal,samplerate=16000,winlen=0.025,winstep=0.01,numcep=13,
          nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97,ceplifter=22,appendEnergy=True):
           
    feat,energy = fbank(signal,samplerate,winlen,winstep,nfilt,nfft,lowfreq,highfreq,preemph)
    feat = numpy.log(feat)
    feat = dct(feat, type=2, axis=1, norm='ortho')[:,:numcep]
    # feat = lifter(feat,ceplifter)
    if appendEnergy: feat[:,0] = numpy.log(energy) # replace first cepstral coefficient with log of frame energy
    return feat
# def mfcc(feature, energy, numcep=13, appendEnergy=True):
#     feature = dct(feature)[:,:numcep]
#     return feature




# def get_ffts(bins):
#     for key in bins:
#         np.fft.hfft(bins[key])
#     return bins


# def get_max_ffts(bins):
#     max_ffts = []
#     for key in bins:
#         max_fft = max(bins[key])
#         max_ffts.append(max_fft)
#     return max_ffts



# def get_freqs(data):
#     # array = bins["bin_1"]
#     freq = np.fft.fftfreq(data)
#     return freq

    


rate, data = read_file("Alohamora_1.wav")
# data = normalize(data)
bins = split(data)
# print bins
power_spectrum = power_spectrum(bins)

get_filterbanks(nfilt=40,samplerate=16000,lowfreq=0, highfreq=8000)
fbank(power_spectrum,fbank,samplerate=16000,nfilt=40,nfft=400,lowfreq=0,highfreq=8000)
print mfcc(signal,samplerate=16000,winlen=0.025,winstep=0.01,numcep=13,
          nfilt=26,nfft=512,lowfreq=0,highfreq=None,preemph=0.97,ceplifter=22,appendEnergy=True)



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













