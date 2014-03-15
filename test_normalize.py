
original_vals = [-23.5, -12.7, -20.6, -11.3, -9.2, -4.5, 2, 8, 11, 15, 17, 21 ]

# get max absolute value
original_max = max([abs(val) for val in original_vals])

# normalize to desired range size
new_range_val = 1
normalized_vals = [float(val)/original_max * new_range_val for val in original_vals]

print normalized_vals