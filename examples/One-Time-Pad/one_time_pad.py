"""One-Time Pad Cipher Implementation

This example shows the core idea of a one-time pad: a random key as long as
plaintext is used once for encryption and once for decryption.
"""


def one_time_pad_encrypt(plaintext, key):
    """Encrypt using a one-time pad."""
    plaintext = plaintext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    ciphertext = []
    for index, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[index % len(key)]) - ord("A")
            pos = (ord(char) - ord("A") + shift) % 26
            ciphertext.append(chr(pos + ord("A")))

    return "".join(ciphertext)


def one_time_pad_decrypt(ciphertext, key):
    """Decrypt using the same one-time pad key."""
    ciphertext = ciphertext.upper().replace(" ", "")
    key = key.upper().replace(" ", "")

    plaintext = []
    for index, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[index % len(key)]) - ord("A")
            pos = (ord(char) - ord("A") - shift) % 26
            plaintext.append(chr(pos + ord("A")))

    return "".join(plaintext)


if __name__ == "__main__":
    plaintext = "SECRETMESSAGE"
    key = "RANDOMKEY123"
    ciphertext = one_time_pad_encrypt(plaintext, key)
    recovered = one_time_pad_decrypt(ciphertext, key)

    print(f"Plaintext: {plaintext}")
    print(f"Key:       {key}")
    print(f"Ciphertext:{ciphertext}")
    print(f"Recovered: {recovered}")
