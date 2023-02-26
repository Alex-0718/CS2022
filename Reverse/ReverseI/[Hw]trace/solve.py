enc_flag = [55, 61, 48, 54, 10, 37, 3, 48, 18, 66, 46, 60, 66, 46, 64, 55, 46, 36, 46, 18, 48, 63, 12, 0]
for i in range(len(enc_flag)):
    enc_flag[i] ^= 113
print(''.join([bytes.fromhex(hex(enc_flag[i])[2:]).decode() for i in range(len(enc_flag))]))