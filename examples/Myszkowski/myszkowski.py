"""Myszkowski Transposition Cipher Implementation

This is a simplified educational version of the Myszkowski transposition
cipher using a keyword-based column ordering.
"""


def myszkowski_encrypt(plaintext, keyword):
    """Encrypt plaintext using a keyword-based column arrangement."""
    keyword = keyword.upper().replace(" ", "")
    cols = sorted(range(len(keyword)), key=lambda i: keyword[i])
    padded = plaintext + "X" * (len(keyword) - len(plaintext) % len(keyword))
    rows = [padded[i:i + len(keyword)] for i in range(0, len(padded), len(keyword))]

    ciphertext = []
    for index in cols:
        for row in rows:
            ciphertext.append(row[index])

    return "".join(ciphertext)


def myszkowski_decrypt(ciphertext, keyword):
    """Decrypt ciphertext using the inverse arrangement."""
    keyword = keyword.upper().replace(" ", "")
    cols = sorted(range(len(keyword)), key=lambda i: keyword[i])
    rows = len(ciphertext) // len(keyword)
    matrix = [[""] * len(keyword) for _ in range(rows)]

    pointer = 0
    for index in cols:
        for row in range(rows):
            matrix[row][index] = ciphertext[pointer]
            pointer += 1

    return "".join("".join(row) for row in matrix).rstrip("X")


if __name__ == "__main__":
    plaintext = "CRYPTOGRAPHY"
    keyword = "KEY"
    ciphertext = myszkowski_encrypt(plaintext, keyword)
    recovered = myszkowski_decrypt(ciphertext, keyword)

    print(f"Plaintext: {plaintext}")
    print(f"Keyword:   {keyword}")
    print(f"Ciphertext:{ciphertext}")
    print(f"Recovered: {recovered}")
