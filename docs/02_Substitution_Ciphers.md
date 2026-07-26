# 02. Substitution Ciphers

## Overview

Substitution ciphers replace each character (or group of characters) in plaintext with another character according to a fixed rule. This document covers:

- **Monoalphabetic Ciphers**: Caesar, Additive, Multiplicative, Affine
- **Polyalphabetic Ciphers**: Vigenère, Homophonic
- **Block Substitution**: Playfair, Autokey, Nihilist, One-Time Pad

## Monoalphabetic Ciphers

### Caesar Cipher

**Definition**: Each letter shifted by fixed number of positions.

**Formula**: C = (P + K) mod 26

**Example**: HELLO → KHOOR (shift 3)

**Security**: Very weak (only 26 possible keys)

**Cryptanalysis**: Brute force, frequency analysis

---

## Polyalphabetic Ciphers

### Vigenère Cipher

**Definition**: Uses repeating keyword to generate multiple shifts.

**Key Advantage**: Defeats simple frequency analysis

**Weakness**: Kasiski Examination breaks it

**Example**: 
Plaintext: VIGENERE
Key: CIPHER
Ciphertext: XQVLRVTM

---

## Additional Resources

Detailed implementations with worked examples are provided in the `/examples/` directories.

For comprehensive documentation on all 14 ciphers, see the complete guides in each cipher folder.

---

*Last Updated: July 2026*