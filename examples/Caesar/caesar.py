"""Caesar Cipher Implementation

The Caesar Cipher shifts each letter by a fixed number of positions.
Formula: C = (P + K) mod 26
"""

def caesar_encrypt(plaintext, key):
    """
    Encrypt plaintext using Caesar Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        key (int): Shift value (1-25)
    
    Returns:
        str: Encrypted ciphertext
    """
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            # Determine if uppercase or lowercase
            if char.isupper():
                # Shift uppercase letter
                ciphertext += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            else:
                # Shift lowercase letter
                ciphertext += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    
    return ciphertext


def caesar_decrypt(ciphertext, key):
    """
    Decrypt ciphertext using Caesar Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        key (int): Shift value (1-25)
    
    Returns:
        str: Decrypted plaintext
    """
    return caesar_encrypt(ciphertext, -key)


def brute_force_caesar(ciphertext):
    """
    Attempt to break Caesar cipher by trying all 26 possible keys.
    
    Args:
        ciphertext (str): Encrypted message
    
    Returns:
        list: List of tuples (key, decrypted_text) for all possibilities
    """
    results = []
    for key in range(26):
        decrypted = caesar_decrypt(ciphertext, key)
        results.append((key, decrypted))
    return results


if __name__ == "__main__":
    # Example usage
    plaintext = "HELLO WORLD"
    key = 3
    
    print(f"Original:  {plaintext}")
    
    # Encrypt
    ciphertext = caesar_encrypt(plaintext, key)
    print(f"Key:       {key}")
    print(f"Encrypted: {ciphertext}")
    
    # Decrypt
    recovered = caesar_decrypt(ciphertext, key)
    print(f"Decrypted: {recovered}")
    
    # Brute force demonstration
    print("\nBrute Force Results:")
    print("-" * 50)
    results = brute_force_caesar(ciphertext)
    for k, text in results:
        if k == key:
            print(f"Key {k:2d}: {text} <-- CORRECT")
        else:
            print(f"Key {k:2d}: {text}")
