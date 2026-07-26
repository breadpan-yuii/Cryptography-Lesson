"""Affine Cipher Implementation

Combines multiplicative and additive ciphers.
Formula: C = (K1 * P + K2) mod 26
"""

def gcd(a, b):
    """Calculate Greatest Common Divisor."""
    while b:
        a, b = b, a % b
    return a


def mod_inverse(a, m):
    """
    Find modular inverse of a modulo m.
    
    Args:
        a (int): Number to find inverse for
        m (int): Modulus
    
    Returns:
        int: Modular inverse or None if doesn't exist
    """
    if gcd(a, m) != 1:
        return None
    
    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1
        gcd_val, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd_val, x, y
    
    _, x, _ = extended_gcd(a % m, m)
    return (x % m + m) % m


def affine_encrypt(plaintext, k1, k2):
    """
    Encrypt plaintext using Affine Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        k1 (int): Multiplicative key (must be coprime with 26)
        k2 (int): Additive key (0-25)
    
    Returns:
        str: Encrypted ciphertext
    """
    # Validate k1
    if gcd(k1, 26) != 1:
        raise ValueError(f"K1 ({k1}) must be coprime with 26")
    
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                pos = ord(char) - ord('A')
                encrypted_pos = (k1 * pos + k2) % 26
                ciphertext += chr(encrypted_pos + ord('A'))
            else:
                pos = ord(char) - ord('a')
                encrypted_pos = (k1 * pos + k2) % 26
                ciphertext += chr(encrypted_pos + ord('a'))
        else:
            ciphertext += char
    
    return ciphertext


def affine_decrypt(ciphertext, k1, k2):
    """
    Decrypt ciphertext using Affine Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        k1 (int): Multiplicative key
        k2 (int): Additive key
    
    Returns:
        str: Decrypted plaintext
    """
    # Find multiplicative inverse of k1
    k1_inv = mod_inverse(k1, 26)
    if k1_inv is None:
        raise ValueError(f"K1 ({k1}) has no multiplicative inverse mod 26")
    
    plaintext = ""
    
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                pos = ord(char) - ord('A')
                decrypted_pos = (k1_inv * (pos - k2)) % 26
                plaintext += chr(decrypted_pos + ord('A'))
            else:
                pos = ord(char) - ord('a')
                decrypted_pos = (k1_inv * (pos - k2)) % 26
                plaintext += chr(decrypted_pos + ord('a'))
        else:
            plaintext += char
    
    return plaintext


def valid_affine_keys():
    """Return count of valid key combinations."""
    valid_k1 = [k for k in range(1, 26) if gcd(k, 26) == 1]
    return len(valid_k1) * 26  # k1 choices * k2 choices


if __name__ == "__main__":
    plaintext = "AFFINE"
    k1 = 5  # Valid key (coprime with 26)
    k2 = 8  # Additive key
    
    print(f"Original:   {plaintext}")
    print(f"K1 (mult):  {k1}")
    print(f"K2 (add):   {k2}")
    print(f"Total key combinations: {valid_affine_keys()}")
    
    ciphertext = affine_encrypt(plaintext, k1, k2)
    print(f"Encrypted:  {ciphertext}")
    
    recovered = affine_decrypt(ciphertext, k1, k2)
    print(f"Decrypted:  {recovered}")
    
    # Longer example
    print("\n" + "="*50)
    plaintext2 = "THE QUICK BROWN FOX"
    ciphertext2 = affine_encrypt(plaintext2, k1, k2)
    print(f"Original:   {plaintext2}")
    print(f"Encrypted:  {ciphertext2}")
    recovered2 = affine_decrypt(ciphertext2, k1, k2)
    print(f"Decrypted:  {recovered2}")
