import random

from secret import FLAG

# state = random.randint(0, 1 << 32)
state = random.randint(0, 1 << 18)
a = state

def getbit():
    global state, a
    state <<= 1
    if state & (1 << 18):
        # state ^= 0x1008345a9
        state ^= 0x745a9
        return 1
    return 0

flag = list(map(int, ''.join(["{:08b}".format(c) for c in FLAG])))
output = []
for _ in range(len(flag)):
    for __ in range(36):
        getbit()
    if _ + 1 == len(flag): print(f"Last state = {state}")
    output.append(getbit())

print(f"state = {state}\n")

for _ in range(40):
    for __ in range(36):
        getbit()
    output.append(getbit())

for i in range(len(flag)):
    print(output[i], end='')
    output[i] ^= flag[i]

print('\n', output)
