import random

from secret import FLAG

state = random.randint(0, 1 << 64)
state = 11648793142163433888

def getbit():
    global state
    state <<= 1
    if state & (1 << 64):
        state ^= 0x1da785fc480000001
        return 1
    return 0

flag = list(map(int, ''.join(["{:08b}".format(c) for c in FLAG])))
output = []
for _ in range(len(flag)):
    for __ in range(36):
        getbit()
    output.append(getbit())

# print(list(map(int, list(bin(state)[2:]))))

for _ in range(70):
    for __ in range(36):
        getbit()
    output.append(getbit())


for i in range(len(flag)):
    output[i] ^= flag[i]

print(output)
