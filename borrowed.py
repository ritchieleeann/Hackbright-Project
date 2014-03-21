def split(data, bin_len=400, bin_step=160, winfunc=lambda x:np.ones((1,x))):
    data_len = len(data)
    if data_len <= bin_len: #if sample is shorter than bin
        num_bins = 1 
    else:
        num_bins = 1 + math.ceil((1.0*data_len - bin_len)/bin_step)

    pad_len = (num_bins - 1)*bin_step + bin_len

    zeros = np.zeros((pad_len - data_len,))
    pad_signal = np.concatenate((data, zeros))

    indices = np.tile(np.arange(0,bin_len), (num_bins, 1)) + np.tile(np.arange(0,num_bins*bin_step,bin_step),(bin_len,1)).T
    indices = np.array(indices, dtype=np.int32)
    bins = pad_signal[indices]
    win = np.tile(winfunc(bin_len), (num_bins, 1))
    return bins*win, num_bins 

def overlap(bins, siglen=0, bin_len=400, bin_step=160, winfunc=lambda x:np.ones((1,x))):
    num_bins = np.shape(bins)[0]
    assert np.shape(frames)[1] == bin_len, '"frames" matrix is wrong size, 2nd dim is not equal to frame_len'

    indices = np.tile(np.arange(0,bin_len), (num_bins, 1)) + np.tile(np.arange(0,num_bins*bin_step, bin_step), (bin_len, 1)).T
    indices = np.aray(indices, dtype=np.int32)
    pad_len = (num_bins-1)*bin_step + bin_len

    if siglen <= 0: siglen = pad_len

    rec_signal = np.zeros((1,pad_len))
    window_correction = np.zeros((1,pad_len))
    win = winfunc(bin_len)

    for i in range(0, num_bins):
        window_correction[indices[i,:]] = window_correction[indices[i,:]] + win + 1e-15
        rec_signal[indices[i, :]] = rec_signal[indices[i,:]] + frames[i,:]

    rec_signal = rec_signal/window_correction
    return rec_signal[0:siglen]

def magnitude(bins, NFFT=512):
    complex_spec = np.fft.rfft(bins, NFFT)
    return np.absolute(complex_spec)

def power(bins, NFFT=512):
    return 1.0/NFFT * np.square(magnitude(bins, NFFT))

def log_power(bins, NFFT=512, norm=1):
    p = power(bins, NFFT);
    p[p <= 1e-30] = 1e-30
    log_p = 10*np.log10(p)
    if norm:
        return log_p - np.max(log_p)
    else:
        return log_p

def preemphasis(data, coeff=0.95):
    return np.append(data[0], data[1:]-coeff*data[:-1])