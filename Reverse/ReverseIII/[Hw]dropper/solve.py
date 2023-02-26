import win32api
import win32con

from ctypes import FormatError, GetLastError
from ctypes import windll, c_void_p, byref, create_string_buffer, c_int

from wincrypto.constants import HP_ALGID, HP_HASHSIZE, KP_KEYLEN, KP_ALGID, CRYPT_EXPORTABLE

key = [255, 0, 0, 0, 0, 0, 0, 0]
length = 10
plainText = []

def main():
    hProv = c_void_p()
    phHash = c_void_p()
    hkey = c_void_p()
    if (windll.advapi32.CryptAcquireContextA(byref(hProv), 0, 0, 1, 0) == 0):
        return 0
    if GetLastError():
        return 0
    if (windll.advapi32.CryptCreateHash(hProv, 32772, 0, None, byref(phHash)) == 0):
        return 0
    # if (windll.advapi32.CryptHashData(phHash, key, 1, 0) == 0):
    #     return 0
    if (windll.advapi32.CryptDeriveKey(hProv, 26625, phHash, CRYPT_EXPORTABLE, byref(hkey)) == 0):
        return 0
    if (windll.advapi32.CryptDestroyHash(phHash) == 0):
        return 0

    
   
    

    print('Good!')
    print(len('FLAG{H3r3_U_G0_iT_Is_UR_flAg}\n'))
main()