data = {i:0 for i in range(34, 11, -1)}
print(data)
for k in data.items():
    if  33 > k >= 31:
        data[k] = 1
    elif 27 < k <= 30:
        data[k] += data[k+2]
    elif k <= 27:
        data[k] += data[k+2] + data[k+5]
print(data)
