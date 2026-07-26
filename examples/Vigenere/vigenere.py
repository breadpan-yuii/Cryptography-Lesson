"""Vigenère Cipher Implementation

Uses a repeating keyword to generate multiple shift values.
Formula: C = (P + K[i mod keylen]) mod 26
"""

def vigenere_encrypt(plaintext, keyword):
    """
    Encrypt plaintext using Vigenère Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        keyword (str): Repeating keyword for shifts
    
    Returns:
        str: Encrypted ciphertext
    """
    ciphertext = ""
    keyword = keyword.upper()
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Get current key letter and its shift value
            key_shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            
            # Shift the character
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))
            
            # Move to next key letter
            key_index += 1
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char
    
    return ciphertext


def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypt ciphertext using Vigenère Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        keyword (str): Repeating keyword for shifts
    
    Returns:
        str: Decrypted plaintext
    """
    plaintext = ""
    keyword = keyword.upper()
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Get current key letter and its shift value
            key_shift = ord(keyword[key_index % len(keyword)]) - ord('A')
            
            # Reverse the shift
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
            
            # Move to next key letter
            key_index += 1
        else:
            # Keep non-alphabetic characters unchanged
            plaintext += char
    
    return plaintext


def find_key_length(ciphertext, max_length=20):
    """
    Estimate key length using Kasiski examination (simplified).
    Finds coincident sequences and analyzes distances.
    
    Args:
        ciphertext (str): Encrypted message
        max_length (int): Maximum key length to check
    
    Returns:
        int: Estimated key length
    """
    # This is a simplified version - full Kasiski is complex
    # Returns most likely key length based on statistical analysis
    return 3  # Placeholder


if __name__ == "__main__":
    # Example usage
    plaintext = "VIGENERE"
    keyword = "CIPHER"
    
    print(f"Original: {plaintext}")
    print(f"Keyword:  {keyword}")
    
    # Encrypt
    ciphertext = vigenere_encrypt(plaintext, keyword)
    print(f"Encrypted: {ciphertext}")
    
    # Decrypt
    recovered = vigenere_decrypt(ciphertext, keyword)
    print(f"Decrypted: {recovered}")
    
    # Longer example
    print("\n" + "="*50)
    plaintext2 = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    print(f"Original: {plaintext2}")
    ciphertext2 = vigenere_encrypt(plaintext2, "SECRET")
    print(f"Encrypted: {ciphertext2}")
    recovered2 = vigenere_decrypt(ciphertext2, "SECRET")
    print(f"Decrypted: {recovered2}")
