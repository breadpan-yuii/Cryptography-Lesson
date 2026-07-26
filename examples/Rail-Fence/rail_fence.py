"""Rail Fence Transposition Cipher Implementation

Arranges plaintext in a zigzag pattern across rails.
"""

def rail_fence_encrypt(plaintext, rails):
    """
    Encrypt plaintext using Rail Fence Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        rails (int): Number of rails (rows)
    
    Returns:
        str: Encrypted ciphertext
    """
    if rails == 1:
        return plaintext
    
    # Create list of strings for each rail
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Write plaintext in zigzag pattern
    for char in plaintext:
        fence[rail].append(char)
        
        # Change direction at top and bottom
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Read off each rail
    ciphertext = ""
    for rail_chars in fence:
        ciphertext += ''.join(rail_chars)
    
    return ciphertext


def rail_fence_decrypt(ciphertext, rails):
    """
    Decrypt ciphertext using Rail Fence Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        rails (int): Number of rails (rows)
    
    Returns:
        str: Decrypted plaintext
    """
    if rails == 1:
        return ciphertext
    
    # Calculate length of each rail
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Mark which positions belong to which rail
    for _ in range(len(ciphertext)):
        fence[rail].append(None)
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Fill in the cipher characters
    cipher_index = 0
    for i in range(rails):
        for j in range(len(fence[i])):
            fence[i][j] = ciphertext[cipher_index]
            cipher_index += 1
    
    # Read in zigzag order
    plaintext = ""
    rail = 0
    direction = 1
    
    fence_indices = [0] * rails
    
    for _ in range(len(ciphertext)):
        plaintext += fence[rail][fence_indices[rail]]
        fence_indices[rail] += 1
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    return plaintext


def visualize_encryption(plaintext, rails):
    """
    Visualize the Rail Fence encryption process.
    
    Args:
        plaintext (str): Message to encrypt
        rails (int): Number of rails
    """
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1
    
    # Write plaintext
    for i, char in enumerate(plaintext):
        fence[rail].append((i, char))
        
        if rail == 0:
            direction = 1
        elif rail == rails - 1:
            direction = -1
        
        rail += direction
    
    # Display
    print(f"\nPlaintext: {plaintext}")
    print(f"Rails: {rails}")
    print("\nZigzag Pattern:")
    
    for rail_num, rail_chars in enumerate(fence):
        print(f"Rail {rail_num}: ", end="")
        for pos, char in rail_chars:
            print(f"{char} ", end="")
        print()


if __name__ == "__main__":
    # Example usage
    plaintext = "ATTACKATDAWN"
    rails = 3
    
    print(f"Original: {plaintext}")
    print(f"Rails: {rails}")
    
    # Visualize
    visualize_encryption(plaintext, rails)
    
    # Encrypt
    ciphertext = rail_fence_encrypt(plaintext, rails)
    print(f"\nEncrypted: {ciphertext}")
    
    # Decrypt
    recovered = rail_fence_decrypt(ciphertext, rails)
    print(f"Decrypted: {recovered}")
    
    # Test with different rail counts
    print("\n" + "="*50)
    for num_rails in range(2, 5):
        encrypted = rail_fence_encrypt(plaintext, num_rails)
        decrypted = rail_fence_decrypt(encrypted, num_rails)
        print(f"Rails {num_rails}: {encrypted} -> {decrypted}")
