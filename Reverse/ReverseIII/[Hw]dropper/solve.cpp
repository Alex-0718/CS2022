#include <Windows.h>
#include <wincrypt.h>

#include <cstdlib>
#include <iostream>

using namespace std;

int main() {
    const BYTE key[] = {0xFF, 0, 0, 0, 0, 0, 0, 0};
    signed char secret[] = {0xE1, 0xD6, 0x26, 0x81, 0x83, 0x9F, 0x36, 0x8F,
                            0xF6, 0x39, 0x89, 0x7A, 0x92, 0x97, 0x84, 0xA4,
                            0x70, 0x04, 0x61, 0x4B, 0x77, 0xED, 0x58, 0x5D,
                            0xE0, 0xE1, 0x75, 0x3A, 0xF9, 0x34};
    HCRYPTHASH hProv;
    HCRYPTHASH hHash;
    HCRYPTHASH hkey;
    if (!CryptAcquireContextA(&hProv, 0, 0, 1, 0)) {
        if (GetLastError() != -2146893802) return 0;
        if (!CryptAcquireContextA(&hProv, 0, 0, 1, 8)) return 0;
    }
    if (!CryptCreateHash(hProv, 32772, 0, 0, &hHash)) return 0;
    if (!hHash) return 0;
    if (!CryptHashData(hHash, key, 1, 0)) return 0;
    if (!CryptDeriveKey(hProv, 26625, hHash, 1, &hkey)) return 0;
    CryptDestroyHash(hHash);

    DWORD Size = 30;
    BYTE* plainText = (BYTE*)malloc(30);
    memcpy(plainText, secret, 30);

    if (!CryptEncrypt(hkey, 0, 1, 0, plainText, &Size, Size)) return 0;
    cout << plainText << endl;
}