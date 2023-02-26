from tqdm import tqdm
import itertools

SIZE, SIZE1, SIZE2, SIZE3, RATIO = 200, 27, 23, 25, 0.7
result = [1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
flag, hint = result[:232], result[232:]
_state = []

def int2str(a):
    return chr(int('0b' + a, 2))

def getbit(tap):
    global _state
    f = sum([_state[i] for i in tap]) & 1
    x = _state.pop(0)
    _state.append(f)
    return x

def tri_getbit(tap, num):
    global _state
    f = sum([_state[num][i] for i in tap]) & 1
    x = _state[num].pop(0)
    _state[num].append(f)
    return f

def get_state(tap, size):
    global _state
    for state in tqdm(list(itertools.product([0, 1], repeat=size))): 
        count, _state = 0, list(state)
        for i in range(200): 
            r = getbit(tap)
            if r == hint[i]: count = count + 1
            if count + 199 - i < RATIO * SIZE or count > RATIO * SIZE: break
        if count / SIZE >= RATIO: return state

def lsfr2state(lfsr, tap):
    global _state
    _state, output = list(lfsr), [0 for _ in range(200)]
    for i in range(200): output[i] = getbit(tap)
    return output

def get_correct_state(taps, size, lfsrA, lfsrB):
    global _state
    output2, output3 = lsfr2state(lfsrA, taps[1]), lsfr2state(lfsrB, taps[2])
    for state in tqdm(itertools.product([0, 1], repeat=size)): 
        count, _state = 0, list(state)
        for i in range(200):
            r = getbit(taps[0])
            if (r == 1 and output2[i] == hint[i]) or (r == 0 and output3[i] == hint[i]):
                count = count + 1
            else:
                break
        if count == 200: return state

if __name__ == '__main__':
    taps = [[26, 16, 13, 0], [22, 7, 5, 0], [24, 19, 17, 0]]
    output = [[0 for _ in range(200)], [0 for _ in range(200)], [0 for _ in range(200)]]

    lfsr2 = get_state(taps[1], SIZE2)
    # lfsr2 = (0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0)
    lfsr3 = get_state(taps[2], SIZE3)
    # lfsr3 = (1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1)
    lfsr1 = get_correct_state(taps, SIZE1, lfsr2, lfsr3)
    # lfsr1 = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1)

    taps, elements = [[14, 11, 1, 0], [18, 16, 1, 0], [8, 6, 1, 0]], []
    _state = [list(reversed(lfsr1)), list(reversed(lfsr2)), list(reversed(lfsr3))]
    for i in tqdm(range(len(flag))):
        x1 = tri_getbit(taps[0], 0)
        x2 = tri_getbit(taps[1], 1)
        x3 = tri_getbit(taps[2], 2)
        elements.append(x2 if x1 else x3)
    flag = [str(flag[i] ^ elements[len(flag) - i - 1]) for i in range(len(flag))]
    plainText = list(map(int2str, ["".join(flag[8 * i:8 * (i + 1)]) for i in range(int(len(flag) / 8))]))   
    print("".join(plainText))