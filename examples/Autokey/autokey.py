"""Autokey Cipher Implementation

This is a beginner-friendly version of the Autokey cipher. The key grows
by appending plaintext characters after the initial keyword.
"""


def autokey_encrypt(plaintext, keyword):
    """Encrypt text using the Autokey cipher."""
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")

    key_stream = keyword + plaintext
    ciphertext = []

    for index, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key_stream[index]) - ord("A")
            pos = (ord(char) - ord("A") + shift) % 26
            ciphertext.append(chr(pos + ord("A")))

    return "".join(ciphertext)


def autokey_decrypt(ciphertext, keyword):
    """Decrypt text using the Autokey cipher."""
    ciphertext = ciphertext.upper().replace(" ", "")
    keyword = keyword.upper().replace(" ", "")

    key_stream = keyword
    plaintext_chars = []

    for index, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key_stream[index]) - ord("A") if index < len(key_stream) else ord(plaintext_chars[index - len(keyword)]) - ord("A")
            pos = (ord(char) - ord("A") - shift) % 26
            plain_char = chr(pos + ord("A"))
            plaintext_chars.append(plain_char)
            key_stream += plain_char

    return "".join(plaintext_chars)


if __name__ == "__main__":
    plaintext = "AUTOKEY"
    keyword = "SECRET"
    ciphertext = autokey_encrypt(plaintext, keyword)
    recovered = autokey_decrypt(ciphertext, keyword)

    print(f"Plaintext: {plaintext}")
    print(f"Keyword:   {keyword}")
    print(f"Ciphertext:{ciphertext}")
    print(f"Recovered: {recovered}")
