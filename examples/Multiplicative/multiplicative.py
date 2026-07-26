"""Multiplicative Cipher Implementation

Multiplicative cipher using modular arithmetic.
Formula: C = (P * K) mod 26
"""

def gcd(a, b):
    """Calculate Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Find modular inverse of a modulo m.
    Returns None if inverse doesn't exist.
    
    Args:
        a (int): Number to find inverse for
        m (int): Modulus
    
    Returns:
        int: Modular inverse or None
    """
    if gcd(a, m) != 1:
        return None  # Inverse doesn't exist
    
    # Extended Euclidean Algorithm
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(a % m, m)
    return (x % m + m) % m


def multiplicative_encrypt(plaintext, key):
    """
    Encrypt plaintext using Multiplicative Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        key (int): Multiplicative key (must be coprime with 26)
    
    Returns:
        str: Encrypted ciphertext
    """
    # Validate key
    if gcd(key, 26) != 1:
        raise ValueError(f"Key {key} is not coprime with 26")
    
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A')) * key % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a')) * key % 26 + ord('a'))
        else:
            ciphertext += char
    
    return ciphertext


def multiplicative_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Multiplicative Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        key (int): Multiplicative key
    
    Returns:
        str: Decrypted plaintext
    """
    # Find multiplicative inverse
    key_inv = mod_inverse(key, 26)
    if key_inv is None:
        raise ValueError(f"Key {key} has no multiplicative inverse mod 26")
    
    return multiplicative_encrypt(ciphertext, key_inv)


def valid_multiplicative_keys():
    """Return list of valid multiplicative keys (coprime with 26)."""
    valid = []
    for k in range(1, 26):
        if gcd(k, 26) == 1:
            valid.append(k)
    return valid


if __name__ == "__main__":
    plaintext = "HELLO"
    key = 5  # Valid key (coprime with 26)
    
    print(f"Valid keys: {valid_multiplicative_keys()}")
    print(f"\nOriginal:  {plaintext}")
    print(f"Key:       {key}")
    
    ciphertext = multiplicative_encrypt(plaintext, key)
    print(f"Encrypted: {ciphertext}")
    
    recovered = multiplicative_decrypt(ciphertext, key)
    print(f"Decrypted: {recovered}")
    
    # Show inverse
    inv = mod_inverse(key, 26)
    print(f"\nKey inverse: {inv}")
    print(f"Verification: ({key} * {inv}) mod 26 = {(key * inv) % 26}")
