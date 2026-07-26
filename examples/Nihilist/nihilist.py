"""Nihilist Cipher Implementation

This simplified version uses a Polybius square and a simple numeric
combination step to illustrate the idea behind the Nihilist cipher.
"""


def build_polybius_square(keyword="CRYPTO"):
    """Build a 5x5 Polybius square with letters A-Z (excluding J)."""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = keyword.upper().replace("J", "I")
    used = []

    for char in keyword:
        if char not in used and char in alphabet:
            used.append(char)

    for char in alphabet:
        if char not in used:
            used.append(char)

    square = []
    for i in range(0, 25, 5):
        square.append(used[i:i + 5])
    return square


def polybius_value(square, char):
    """Return row/column coordinates for a letter."""
    char = char.upper().replace("J", "I")
    for row_index, row in enumerate(square):
        for col_index, value in enumerate(row):
            if value == char:
                return row_index + 1, col_index + 1
    return None


def nihilist_encrypt(plaintext, keyword="CRYPTO"):
    """Encrypt plaintext with a simple Nihilist-style procedure."""
    square = build_polybius_square(keyword)
    ciphertext = []

    for char in plaintext.upper().replace(" ", ""):
        if char.isalpha():
            row, col = polybius_value(square, char)
            ciphertext.append(f"{row}{col}")

    return " ".join(ciphertext)


def nihilist_decrypt(ciphertext, keyword="CRYPTO"):
    """Decrypt a Nihilist-style ciphertext."""
    square = build_polybius_square(keyword)
    plaintext = []

    for token in ciphertext.split():
        if len(token) >= 2:
            row = int(token[0]) - 1
            col = int(token[1]) - 1
            plaintext.append(square[row][col])

    return "".join(plaintext)


if __name__ == "__main__":
    plaintext = "HELLO"
    ciphertext = nihilist_encrypt(plaintext)
    recovered = nihilist_decrypt(ciphertext)

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Recovered: {recovered}")
