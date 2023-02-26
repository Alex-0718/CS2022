from Crypto.Util.number import long_to_bytes
array = [80, 86, 75, 81, 133, 115, 120, 115, 126, 105, 112, 115, 120, 115, 105, 119, 122, 124, 121, 126, 111, 109, 126, 43, 135]
flag = b''
for i in range(len(array)):
    flag += (long_to_bytes(array[i] - 10))
print(flag.decode())