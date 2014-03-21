import numpy
import wave



def read_file(filename):
    raw = wave.open(filename)
    signal = raw.readframes(-1)
    data = numpy.fromstring(signal, 'Int16')
    if raw.getnchannels() == 2:
        data = data[::2]
        print "Channels: 2"
    rate= raw.getframerate()
    return rate, data

rate, data = read_file("Alohamora_1.wav")
print rate
print data




