from Crypto.Util.number import long_to_bytes, bytes_to_long
flag = [10200821951308413619, 10203629115627637650, 15026413888945050268, 10132466459609120209, 15692731109035709122, 14470003818609151377, 18446744073709539202]
FLAG = []
print(bytes_to_long(b'FLAG{for'))
for i in range(len(flag)):
    segment = int((hex(flag[i])[2:14] + hex(flag[i])[16:18] + hex(flag[i])[14:16]), 16)
    FLAG.append(long_to_bytes(int(1 << 64) - segment).decode()[::-1])
print(''.join(FLAG))