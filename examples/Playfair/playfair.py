"""Playfair Cipher Implementation

Encrypts pairs of letters using a 5x5 matrix.
"""

def create_playfair_matrix(keyword):
    """
    Create a 5x5 Playfair matrix from a keyword.
    
    Args:
        keyword (str): Keyword for matrix creation
    
    Returns:
        list: 5x5 matrix of characters
    """
    # Remove duplicates and convert to uppercase
    keyword = keyword.upper().replace('J', 'I')
    seen = set()
    matrix_chars = []
    
    # Add keyword characters
    for char in keyword:
        if char.isalpha() and char not in seen:
            matrix_chars.append(char)
            seen.add(char)
    
    # Add remaining alphabet (skip J)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # Note: no J
        if char not in seen:
            matrix_chars.append(char)
    
    # Arrange into 5x5 matrix
    matrix = []
    for i in range(5):
        matrix.append(matrix_chars[i*5:(i+1)*5])
    
    return matrix


def find_position(matrix, char):
    """
    Find position of character in matrix.
    
    Args:
        matrix (list): 5x5 matrix
        char (str): Character to find
    
    Returns:
        tuple: (row, column) position
    """
    char = char.upper().replace('J', 'I')
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return None


def playfair_encrypt(plaintext, keyword):
    """
    Encrypt plaintext using Playfair Cipher.
    
    Args:
        plaintext (str): Message to encrypt
        keyword (str): Keyword for matrix
    
    Returns:
        str: Encrypted ciphertext
    """
    matrix = create_playfair_matrix(keyword)
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    
    # Prepare plaintext (add X between doubles, add X at end if odd)
    prepared = ""
    i = 0
    while i < len(plaintext):
        if i + 1 < len(plaintext):
            if plaintext[i] == plaintext[i+1]:
                prepared += plaintext[i] + 'X'
                i += 1
            else:
                prepared += plaintext[i:i+2]
                i += 2
        else:
            prepared += plaintext[i] + 'X'
            i += 1
    
    # Encrypt pairs
    ciphertext = ""
    for i in range(0, len(prepared), 2):
        char1, char2 = prepared[i], prepared[i+1]
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2:  # Same row
            ciphertext += matrix[r1][(c1+1) % 5]
            ciphertext += matrix[r2][(c2+1) % 5]
        elif c1 == c2:  # Same column
            ciphertext += matrix[(r1+1) % 5][c1]
            ciphertext += matrix[(r2+1) % 5][c2]
        else:  # Rectangle
            ciphertext += matrix[r1][c2]
            ciphertext += matrix[r2][c1]
    
    return ciphertext


def playfair_decrypt(ciphertext, keyword):
    """
    Decrypt ciphertext using Playfair Cipher.
    
    Args:
        ciphertext (str): Encrypted message
        keyword (str): Keyword for matrix
    
    Returns:
        str: Decrypted plaintext
    """
    matrix = create_playfair_matrix(keyword)
    ciphertext = ciphertext.upper().replace(' ', '')
    
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        r1, c1 = find_position(matrix, char1)
        r2, c2 = find_position(matrix, char2)
        
        if r1 == r2:  # Same row
            plaintext += matrix[r1][(c1-1) % 5]
            plaintext += matrix[r2][(c2-1) % 5]
        elif c1 == c2:  # Same column
            plaintext += matrix[(r1-1) % 5][c1]
            plaintext += matrix[(r2-1) % 5][c2]
        else:  # Rectangle
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]
    
    return plaintext


def print_matrix(matrix):
    """
    Pretty print the Playfair matrix.
    
    Args:
        matrix (list): 5x5 matrix
    """
    print("\nPlayfair Matrix:")
    print("  ", end="")
    for i in range(5):
        print(f"{i} ", end="")
    print()
    for i, row in enumerate(matrix):
        print(f"{i} ", end="")
        for char in row:
            print(f"{char} ", end="")
        print()


if __name__ == "__main__":
    # Example usage
    plaintext = "HELLO"
    keyword = "PLAYFAIR"
    
    print(f"Original: {plaintext}")
    print(f"Keyword:  {keyword}")
    
    matrix = create_playfair_matrix(keyword)
    print_matrix(matrix)
    
    # Encrypt
    ciphertext = playfair_encrypt(plaintext, keyword)
    print(f"\nEncrypted: {ciphertext}")
    
    # Decrypt
    recovered = playfair_decrypt(ciphertext, keyword)
    print(f"Decrypted: {recovered}")
