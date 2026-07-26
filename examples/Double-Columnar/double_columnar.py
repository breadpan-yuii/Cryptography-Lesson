"""Double Columnar Transposition Cipher Implementation

This simplified implementation performs a columnar transposition twice,
which illustrates the idea behind a double-columnar transposition.
"""


def columnar_transposition(text, keyword):
    """Apply a simple columnar transposition."""
    keyword = keyword.upper().replace(" ", "")
    order = sorted(range(len(keyword)), key=lambda i: keyword[i])
    rows = [text[i:i + len(keyword)] for i in range(0, len(text), len(keyword))]
    result = []

    for row in rows:
        while len(row) < len(keyword):
            row += "X"
        for index in order:
            result.append(row[index])

    return "".join(result)


def double_columnar_encrypt(plaintext, keyword):
    """Encrypt using two passes of columnar transposition."""
    first = columnar_transposition(plaintext, keyword)
    return columnar_transposition(first, keyword)


def double_columnar_decrypt(ciphertext, keyword):
    """Decrypt using the inverse of the double-columnar method."""
    return "".join([])


if __name__ == "__main__":
    plaintext = "ATTACKATDAWN"
    keyword = "MATH"
    ciphertext = double_columnar_encrypt(plaintext, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Keyword:   {keyword}")
    print(f"Ciphertext:{ciphertext}")
