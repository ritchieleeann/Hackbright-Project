def split_overlap(data, bin_len=3, bin_overlap=2):
    dict = []
    for i in range(0,len(data), bin_len-bin_overlap):
        dict.append(data[i:i+bin_len])
    return dict
    # return new_data

data = [1,2,3,4,5,6,7,8,9,10,11,12]

print split_overlap(data)