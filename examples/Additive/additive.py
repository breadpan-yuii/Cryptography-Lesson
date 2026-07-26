"""Additive Cipher Implementation

Additive cipher using modular arithmetic.
Formula: C = (P + K) mod 26
"""

def additive_encrypt(plaintext, key):
    """
    Encrypt plaintext using Additive Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        key (int): Additive key (0-25)
    
    Returns:
        str: Encrypted ciphertext
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            ciphertext += char
    
    return ciphertext


def additive_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Additive Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        key (int): Additive key (0-25)
    
    Returns:
        str: Decrypted plaintext
    """
    return additive_encrypt(ciphertext, -key)


if __name__ == "__main__":
    plaintext = "CRYPTOGRAPHY"
    key = 5
    
    print(f"Original:  {plaintext}")
    print(f"Key:       {key}")
    
    ciphertext = additive_encrypt(plaintext, key)
    print(f"Encrypted: {ciphertext}")
    
    recovered = additive_decrypt(ciphertext, key)
    print(f"Decrypted: {recovered}")
