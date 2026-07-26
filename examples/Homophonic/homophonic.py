"""Homophonic Cipher Implementation

Each plaintext letter maps to multiple possible ciphertext symbols.
Based on letter frequency in English.
"""

# Homophonic substitution table
# More frequent letters have more representations
HOMOPHONIC_TABLE = {
    'E': ['17', '42', '68', '91', '15', '73'],  # Most frequent
    'T': ['19', '54', '88', '32'],
    'A': ['26', '61', '74', '09'],
    'O': ['38', '62', '87'],
    'I': ['11', '50', '76'],
    'N': ['25', '64', '44'],
    'S': ['33', '58', '72'],
    'H': ['21', '65', '85'],
    'R': ['04', '46', '79'],
    'D': ['06', '83'],
    'L': ['05', '94'],
    'U': ['14', '51'],
    'C': ['16', '81'],
    'M': ['24', '73'],
    'W': ['12', '93'],
    'F': ['30', '71'],
    'G': ['37', '66'],
    'Y': ['23', '92'],
    'P': ['20', '70'],
    'B': ['13', '97'],
    'V': ['36', '89'],
    'K': ['22', '84'],
    'X': ['41'],
    'J': ['40'],
    'Q': ['39'],
    'Z': ['35']
}

# Reverse table for decryption
REVERSE_TABLE = {}
for letter, codes in HOMOPHONIC_TABLE.items():
    for code in codes:
        REVERSE_TABLE[code] = letter

import random


def homophonic_encrypt(plaintext):
    """
    Encrypt plaintext using Homophonic Cipher.
    
    Args:
        plaintext (str): Message to encrypt
    
    Returns:
        str: Encrypted ciphertext (two-digit codes separated by spaces)
    """
    ciphertext = []
    
    for char in plaintext:
        if char.isalpha():
            char_upper = char.upper()
            if char_upper in HOMOPHONIC_TABLE:
                # Randomly select one of the possible codes
                code = random.choice(HOMOPHONIC_TABLE[char_upper])
                ciphertext.append(code)
        else:
            # Keep non-alphabetic characters
            if char.isdigit():
                ciphertext.append(f"({char})")
            elif char == ' ':
                ciphertext.append('|')
            else:
                ciphertext.append(f"[{char}]")
    
    return ' '.join(ciphertext)


def homophonic_decrypt(ciphertext):
    """
    Decrypt ciphertext using Homophonic Cipher.
    
    Args:
        ciphertext (str): Encrypted message (codes separated by spaces)
    
    Returns:
        str: Decrypted plaintext
    """
    codes = ciphertext.split()
    plaintext = ""
    
    for code in codes:
        if code in REVERSE_TABLE:
            plaintext += REVERSE_TABLE[code]
        elif code.startswith('(') and code.endswith(')'):
            plaintext += code[1:-1]  # Digit
        elif code == '|':
            plaintext += ' '  # Space
        elif code.startswith('[') and code.endswith(']'):
            plaintext += code[1:-1]  # Other character
        else:
            plaintext += '?'
    
    return plaintext


def print_frequency_table():
    """Print the homophonic substitution table."""
    print("\nHomophonic Substitution Table:")
    print("Letter | Number of Codes | Codes")
    print("-" * 50)
    for letter in sorted(HOMOPHONIC_TABLE.keys(), 
                         key=lambda x: len(HOMOPHONIC_TABLE[x]), 
                         reverse=True):
        codes = HOMOPHONIC_TABLE[letter]
        print(f"{letter:6} | {len(codes):15} | {', '.join(codes)}")


if __name__ == "__main__":
    plaintext = "HELLO WORLD"
    
    print(f"Original: {plaintext}")
    print_frequency_table()
    
    # Note: Encryption produces different output each time due to randomness
    print(f"\nEncryption 1: ", end="")
    ciphertext1 = homophonic_encrypt(plaintext)
    print(ciphertext1)
    
    decrypted1 = homophonic_decrypt(ciphertext1)
    print(f"Decrypted 1:  {decrypted1}")
    
    print(f"\nEncryption 2: ", end="")
    ciphertext2 = homophonic_encrypt(plaintext)
    print(ciphertext2)
    
    decrypted2 = homophonic_decrypt(ciphertext2)
    print(f"Decrypted 2:  {decrypted2}")
    
    print("\nNotice: Same plaintext encrypts to different ciphertext (randomness)!")
