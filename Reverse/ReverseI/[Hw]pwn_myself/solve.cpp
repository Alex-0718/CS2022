#include <openssl/aes.h>
#include <iostream>
#include <vector>
#include <string>

int main() {
    unsigned char key[] {
        0x4b, 0x29, 0x47, 0x0f, 0x38, 0xd4, 0xa3, 0x4d,
        0x1c, 0x9f, 0x4f, 0xc7, 0x74, 0xe4, 0x29, 0x6a
    };
    unsigned char iv[] = {
        0xb5, 0x9a, 0xec, 0x92, 0x51, 0xe2, 0x5e, 0x3f,
        0x90, 0x81, 0xe4, 0x27, 0x19, 0x2e, 0x50, 0x29
    };

    unsigned char cipher[] = {
        0xd2, 0xb2, 0x40, 0xf2, 0xde, 0x77, 0xe0, 0x85,
        0xfd, 0xe5, 0xbf, 0xb1, 0xeb, 0xf7, 0x64, 0x18,
        0xe4, 0xad, 0x85, 0xef, 0x80, 0x68, 0xda, 0x2c,
        0x25, 0x2d, 0xe1, 0xf8, 0xdd, 0xe7, 0x0b, 0x59,
        0xe8, 0xd7, 0x57, 0x37, 0x2f, 0xb5, 0x41, 0x25,
        0x78, 0x5a, 0xb9, 0x82, 0x22, 0x8d, 0x81, 0x26
    };

    int n = sizeof(cipher) / sizeof(char);

    unsigned char *plain = (unsigned char *)malloc(sizeof(char) * n);
    AES_KEY ctx;
    AES_set_decrypt_key(key, 128, &ctx);
    AES_cbc_encrypt(cipher, plain, n, &ctx, iv, AES_DECRYPT);
    for (int i = 0; i < n; i++) putchar(plain[i]);
    return 0;
}