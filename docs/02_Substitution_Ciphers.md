# 02. Substitution Ciphers

## Table of Contents
1. [What is a Substitution Cipher?](#what-is-a-substitution-cipher)
2. [Monoalphabetic Ciphers](#monoalphabetic-ciphers)
   - [Caesar Cipher](#caesar-cipher)
   - [Additive Cipher](#additive-cipher)
   - [Multiplicative Cipher](#multiplicative-cipher)
   - [Affine Cipher](#affine-cipher)
3. [Polyalphabetic Ciphers](#polyalphabetic-ciphers)
   - [Vigenère Cipher](#vigenère-cipher)
   - [Homophonic Cipher](#homophonic-cipher)
4. [Block Substitution Ciphers](#block-substitution-ciphers)
   - [Playfair Cipher](#playfair-cipher)
   - [Autokey Cipher](#autokey-cipher)
   - [Nihilist Cipher](#nihilist-cipher)
   - [One-Time Pad Cipher](#one-time-pad-cipher)
5. [Summary](#summary)

---

## What is a Substitution Cipher?

### Definition
A **substitution cipher** is an encryption technique where each character (or group of characters) in the plaintext is replaced by another character according to a fixed rule.

### Key Principle
In substitution ciphers:
- The **order of characters remains the same**
- Only the **identity of each character changes**

### Example
```
Plaintext:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Ciphertext: D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

Plaintext:  HELLO WORLD
Ciphertext: KHOOR ZRUOG
```

Notice: Character positions stay the same; characters are replaced.

---

# MONOALPHABETIC CIPHERS

## Caesar Cipher

**Definition**: The Caesar Cipher shifts each letter by a fixed number of positions.

**Formula**: C = (P + K) mod 26

**Example**: HELLO → KHOOR (shift 3)

**Security Level**: 🔴 Very Weak (only 26 possible keys)

**Cryptanalysis**: Brute force, frequency analysis

**Difficulty**: 🔵 Very Easy (1/10)

**Key Concept**: Simple shift cipher - fundamental for learning cryptography

---

## Additive Cipher

**Definition**: Mathematical addition operation on plaintext positions.

**Formula**: C = (P + K) mod 26, P = (C - K) mod 26

**Example**: CRYPTOGRAPHY with Key=5 → HWDUYJTLWFUMD

**Security Level**: 🔴 Very Weak (only 26 possible keys)

**Key Concept**: Demonstrates modular arithmetic in cryptography

---

## Multiplicative Cipher

**Definition**: Multiplies each plaintext position by a key value (modulo 26).

**Formula**: C = (P × K) mod 26, P = (C × K^-1) mod 26

**Key Constraint**: K must be coprime with 26

**Valid Keys**: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25 (only 12 valid keys)

**Example**: HELLO with Key=5 → JUDDS

**Security Level**: 🔴 Very Weak (only 12 valid keys)

**Key Concept**: Introduces modular inverses and coprimality

---

## Affine Cipher

**Definition**: Combines multiplicative and additive cipher operations.

**Formula**: C = (K1 × P + K2) mod 26

**Parameters**: 
- K1 (Multiplier): Must be coprime with 26
- K2 (Additive): Any value 0-25

**Total Key Space**: 12 × 26 = 312 combinations

**Example**: AFFINE with K1=5, K2=8 → IHHWVC

**Security Level**: 🔴 Weak (312 keys, still vulnerable to frequency analysis)

**Difficulty**: 🟡 Medium (4/10)

**Key Concept**: Combining operations for increased complexity

---

# POLYALPHABETIC CIPHERS

## Vigenère Cipher

**Definition**: Uses a repeating keyword to generate multiple shift values.

**Formula**: C = (P + K[i mod keylen]) mod 26

**Key Advantage**: Defeats simple frequency analysis

**Example**:
```
Plaintext: VIGENERE
Key:       CIPHER
Ciphertext: XQVLRVTM
```

**Weakness**: Kasiski Examination reveals key length

**Security Level**: 🟡 Weak-Medium (breakable once key length is found)

**Difficulty**: 🟡 Medium (5/10)

**Cryptanalysis**: Kasiski Examination, Index of Coincidence

**Historical Significance**: Considered unbreakable for 300 years until broken in 1863

---

## Homophonic Cipher

**Definition**: Each plaintext letter maps to multiple possible ciphertext symbols.

**Method**: Frequency-based assignment
- E (most frequent) → 6 representations
- T (second) → 4 representations
- Low-frequency letters → 1-2 representations

**Example**:
- E can be: 17, 42, 68, 91, 15, 73
- T can be: 19, 54, 88, 32

**Advantage**: Defeats simple frequency analysis

**Weakness**: Still vulnerable to digraph/trigraph analysis

**Security Level**: 🟡 Weak (frequency patterns preserved in pairs)

**Difficulty**: 🟡 Medium (6/10)

---

# BLOCK SUBSTITUTION CIPHERS

## Playfair Cipher

**Definition**: Encrypts pairs of letters (digraphs) using a 5×5 matrix.

**Matrix Setup**: 
- Fill with keyword letters
- Add remaining alphabet (I/J combined)

**Encryption Rules**:
- Same row: Shift right (wrap around)
- Same column: Shift down (wrap around)
- Rectangle: Swap corners

**Example**: With keyword "PLAYFAIR", HELLO → (encrypted digraphs)

**Security Level**: 🟡 Medium (breakable with digraph frequency analysis)

**Difficulty**: 🟡 Medium-Hard (7/10)

**Historical Use**: WWI military communications

---

## Autokey Cipher

**Definition**: Plaintext itself becomes part of the key after initial keyword.

**Method**: Key = Keyword + Plaintext

**Example**:
```
Plaintext: AUTOKEY
Keyword:   SECRET
Key:       SECRETAUTOKEY (keyword + plaintext)
```

**Advantage**: No key repetition

**Weakness**: Vulnerable to known plaintext attack

**Security Level**: 🟡 Medium (vulnerable to known plaintext)

**Difficulty**: 🟡 Medium (6/10)

---

## Nihilist Cipher

**Definition**: Combines Polybius square substitution with transposition.

**Method**: 
1. Convert letters to numbers (Polybius square)
2. Apply transposition based on keyword

**Polybius Square**: 5×5 grid where each letter = row digit + column digit

**Example**: A=11, B=12, C=13, etc.

**Security Level**: 🟡 Medium (vulnerable to cryptanalysis)

**Difficulty**: 🟡 Medium-Hard (7/10)

**Key Concept**: Hybrid cipher combining two techniques

---

## One-Time Pad Cipher

**Definition**: Theoretically perfect cipher using a random key as long as plaintext.

**Requirements**:
- Key length = Plaintext length
- Key is truly random
- Key used only once (never reused)
- Key securely distributed

**Formula**: C = (P + K[i]) mod 26

**Security Level**: 🟢 Perfect (information-theoretically secure)

**Difficulty**: 🟡 Medium (5/10)

**Theoretical Strength**: Unbreakable (proven mathematically)

**Practical Weakness**: Key distribution and management

**Critical Rule**: If key is reused, security is completely lost

**Real-World Use**: 
- NSA communications
- Moscow-Washington Hotline
- Ultra-high-security scenarios

---

## Summary of Substitution Ciphers

### Quick Comparison Table

| Cipher | Type | Key Space | Security | Breakable |
|--------|------|-----------|----------|-----------|
| Caesar | Monoalpha | 26 | 🔴 Very Weak | Yes (Brute Force) |
| Additive | Monoalpha | 26 | 🔴 Very Weak | Yes (Brute Force) |
| Multiplicative | Monoalpha | 12 | 🔴 Very Weak | Yes (Frequency) |
| Affine | Monoalpha | 312 | 🔴 Weak | Yes (Frequency) |
| Vigenère | Polyalpha | 26^n | 🟡 Weak-Medium | Yes (Kasiski) |
| Homophonic | Monoalpha | Variable | 🟡 Weak | Yes (Digraph) |
| Playfair | Digraph | 26! | 🟡 Medium | Yes (Digraph) |
| Autokey | Polyalpha | Unlimited | 🟡 Medium | Yes (Known Text) |
| Nihilist | Hybrid | Variable | 🟡 Medium | Yes (Crypto) |
| OTP | Polyalpha | ∞ | 🟢 Perfect | No (if key random) |

### Learning Path

**Beginner**:
1. Caesar Cipher
2. Additive Cipher
3. Multiplicative Cipher

**Intermediate**:
4. Affine Cipher
5. Vigenère Cipher
6. Homophonic Cipher

**Advanced**:
7. Playfair Cipher
8. Autokey Cipher
9. Nihilist Cipher
10. One-Time Pad

### Key Insights

✓ Simple substitution is broken by frequency analysis
✓ Polyalphabetic ciphers need key length discovery to break
✓ All classical ciphers are vulnerable to known plaintext attacks
✓ OTP is perfect theory but impractical in practice
✓ Multiple encryption layers provide better security
✓ Modern cryptography uses mathematical complexity beyond classical methods

---

## Detailed Examples Available

For comprehensive worked examples, formulas, and step-by-step encryption/decryption:
- See individual cipher documentation files
- Review Python implementations in `/examples/` directories
- Check `/resources/` for practice problems

---

*Next: Read 03_Transposition_Ciphers.md to learn rearrangement-based encryption*

---

*Document Status: Complete*  
*Last Updated: July 2026*
