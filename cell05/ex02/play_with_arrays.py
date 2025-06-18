number_array = [2, 8, 9, 48, 8, -22, -12, -2]

unique_array = list(set(number_array))

positive_array = [x for x in unique_array if x > 0]

positive_array.sort()

print("Original array:", number_array)
print("New array:", positive_array)
