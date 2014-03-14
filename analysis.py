import scipy.io.wavfile
import numpy


def read_file(filename):
    rate, data_info = scipy.io.wavfile.read(filename)
    data = []
    for i in data_info:
        data.append(i[0])
    return rate, data

def split(data):
    number_bins = len(data)/1000
    bins = {}
    for i in range(0,number_bins+1):
        bins["bin_%s" % i] = []
    for sample_i in range(len(data)):
        bin_num = int(sample_i/1000)
        bins["bin_%s" % bin_num].append(data[sample_i])
    return bins['bin_1']


def get_fft(bin):
    fft = numpy.fft.hfft(bin)
    return fft


rate, data = read_file("Alohamora_1.wav")
bins = split(data)


# print data
print get_fft(bins)
# print split(data)













