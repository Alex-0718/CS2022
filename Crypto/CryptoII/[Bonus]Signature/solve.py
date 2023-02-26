from hashlib import sha256
from Crypto.Util.number import bytes_to_long, long_to_bytes, inverse
from sage.all import *

bit = 120
n = 115792089210356248762697446949407573529996955224135760342422259061068512044369
msg = [b"Hello, hacker!", b"Try to get my private key!!"]
h = [bytes_to_long(sha256(m).digest()) for m in msg]
sign = [(14172544598918977582736152384082694687121456824918411266907579237575266002947, 38528799796899765092185727228272549246038841460529798154756991351227809477727), (102410874022419490407751324722432727415240151256077403282895529845175734096401, 20470919246887983223139090762537744291734387640660110985346629907021889142754)]
t, u = -inverse(sign[0][1], n) * sign[1][1] * sign[0][0] * inverse(sign[1][0], n), inverse(sign[0][1], n) * sign[0][0] * h[1] * inverse(sign[1][0], n) - inverse(sign[0][1], n) * h[0]
M = Matrix([[n, 0, 0], [t, 1, 0], [u, 0, 1 << bit]])
vectors = M.LLL()

for vector in vectors:
    if vector[2] == 1 << bit:
        break
    if vector[2] == -(1 << bit):
        vector = -vector
        break

d = (vector[1] * sign[1][1] - h[1]) * inverse(sign[1][0], n) % n
print(long_to_bytes(d))