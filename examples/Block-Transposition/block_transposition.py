"""Block Transposition Cipher Implementation

Rearranges columns based on keyword ordering.
"""

def block_transposition_encrypt(plaintext, keyword):
    """
    Encrypt plaintext using Block Transposition Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        keyword (str): Keyword for column ordering
    
    Returns:
        str: Encrypted ciphertext
    """
    keyword = keyword.upper()
    keyword_len = len(keyword)
    
    # Number the columns based on alphabetical order of keyword
    numbered_keyword = []
    for i, letter in enumerate(keyword):
        numbered_keyword.append((letter, i))
    numbered_keyword.sort()
    
    column_order = [pos for _, pos in numbered_keyword]
    
    # Pad plaintext if necessary
    plaintext = plaintext.upper().replace(' ', '')
    padding_needed = (keyword_len - len(plaintext) % keyword_len) % keyword_len
    plaintext += 'X' * padding_needed
    
    # Write plaintext in rows
    rows = []
    for i in range(0, len(plaintext), keyword_len):
        rows.append(plaintext[i:i+keyword_len])
    
    # Read columns in sorted order
    ciphertext = ""
    for col_index in column_order:
        for row in rows:
            if col_index < len(row):
                ciphertext += row[col_index]
    
    return ciphertext


def block_transposition_decrypt(ciphertext, keyword):
    """
    Decrypt ciphertext using Block Transposition Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        keyword (str): Keyword for column ordering
    
    Returns:
        str: Decrypted plaintext
    """
    keyword = keyword.upper()
    keyword_len = len(keyword)
    
    # Number the columns
    numbered_keyword = []
    for i, letter in enumerate(keyword):
        numbered_keyword.append((letter, i))
    numbered_keyword.sort()
    column_order = [pos for _, pos in numbered_keyword]
    
    num_rows = len(ciphertext) // keyword_len
    
    # Create empty grid
    grid = [[''] * keyword_len for _ in range(num_rows)]
    
    # Fill grid from columns
    cipher_index = 0
    for col_order_index in range(keyword_len):
        col_index = column_order[col_order_index]
        for row in range(num_rows):
            if cipher_index < len(ciphertext):
                grid[row][col_index] = ciphertext[cipher_index]
                cipher_index += 1
    
    # Read plaintext from rows
    plaintext = ""
    for row in grid:
        plaintext += ''.join(row)
    
    return plaintext.rstrip('X')


def visualize_encryption(plaintext, keyword):
    """
    Visualize the Block Transposition encryption process.
    
    Args:
        plaintext (str): Message to encrypt
        keyword (str): Keyword for column ordering
    """
    keyword = keyword.upper()
    plaintext = plaintext.upper().replace(' ', '')
    keyword_len = len(keyword)
    
    # Pad
    padding_needed = (keyword_len - len(plaintext) % keyword_len) % keyword_len
    plaintext_padded = plaintext + 'X' * padding_needed
    
    # Number keyword
    numbered_keyword = []
    for i, letter in enumerate(keyword):
        numbered_keyword.append((letter, i))
    numbered_keyword.sort()
    column_order = [pos for _, pos in numbered_keyword]
    
    print(f"\nKeyword: {keyword}")
    print(f"Order:   ", end="")
    for letter, pos in numbered_keyword:
        print(f"{letter}({pos}) ", end="")
    print()
    
    print(f"\nColumn order: {column_order}")
    
    # Show grid
    print(f"\nPlaintext arranged in rows:")
    print("     ", end="")
    for i in range(keyword_len):
        print(f"{i} ", end="")
    print()
    
    for row_idx in range(0, len(plaintext_padded), keyword_len):
        row = plaintext_padded[row_idx:row_idx+keyword_len]
        print(f"Row {row_idx//keyword_len}: ", end="")
        for char in row:
            print(f"{char} ", end="")
        print()


if __name__ == "__main__":
    plaintext = "WEAREDISCOVEREDSAVEYOURSELF"
    keyword = "SECRET"
    
    print(f"Original: {plaintext}")
    print(f"Keyword:  {keyword}")
    
    visualize_encryption(plaintext, keyword)
    
    # Encrypt
    ciphertext = block_transposition_encrypt(plaintext, keyword)
    print(f"\nEncrypted: {ciphertext}")
    
    # Decrypt
    recovered = block_transposition_decrypt(ciphertext, keyword)
    print(f"Decrypted: {recovered}")
