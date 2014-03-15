from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

def plotSpectru(data,rate):
    n = len(data) # lungime semnal
    k = arange(n)
    T = n/rate
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(data)/n # fft computing and normalization
    Y = Y[range(n/2)]

    plt.plot(frq,abs(Y)) # plotting the spectrum
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')