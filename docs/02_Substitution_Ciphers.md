# 02. Substitution Ciphers

Navigation: [Previous: 01. Introduction to Cryptography](01_Introduction_to_Cryptography.md) | [Next: 03. Transposition Ciphers](03_Transposition_Ciphers.md)

This chapter combines the main lesson overview with the richer extended guide so that the full substitution cipher material is available in one place.

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
5. [Comparison and Learning Path](#comparison-and-learning-path)
6. [Summary](#summary)

---

## What is a Substitution Cipher?

A substitution cipher replaces each plaintext letter or symbol with another letter according to a fixed rule. The order of the characters stays the same, but the symbols change.

### Key Principle
- The order of letters is preserved.
- Only the identity of each letter changes.

### Example

```text
Plaintext:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext: DEFGHIJKLMNOPQRSTUVWXYZABC
```

For a Caesar shift of 3:

```text
Plaintext:  HELLO WORLD
Ciphertext: KHOOR ZRUOG
```

### Why This Matters
Substitution ciphers are important because they introduce the core ideas of cryptography: transforming information, using keys, and understanding how patterns can be exploited.

---

# MONOALPHABETIC CIPHERS

## Caesar Cipher

### Definition
The Caesar Cipher shifts each letter by a fixed number of positions in the alphabet.

### Formula

$$
C \equiv (P + K) \bmod 26
$$

Where:
- $P$ = plaintext letter position
- $K$ = shift value
- $C$ = ciphertext letter position

### How It Works
1. Convert each letter to a number from 0 to 25.
2. Add the chosen shift.
3. Wrap around the alphabet with modulo 26.
4. Convert the result back to a letter.

### Encryption Process
- Choose a shift such as 3.
- Move every letter forward by that amount.
- Preserve spaces and punctuation.

### Decryption Process
- Move each letter backward by the same shift.

### Worked Example
Plaintext: HELLO
Key: 3

Result: KHOOR

### Advantages
- Easy to understand
- Fast to implement
- Useful for teaching the concept of encryption

### Disadvantages
- Only 26 possible shifts
- Very vulnerable to brute force and frequency analysis

### Real-World Relevance
- Historically important
- Used as a simple teaching tool and for ROT13-style encoding

### Difficulty
- Very easy

### Summary
The Caesar Cipher is the simplest substitution cipher and is often the first example taught in cryptography.

---

## Additive Cipher

### Definition
The additive cipher is a modular addition version of the Caesar cipher.

### Formula

$$
C = (P + K) \bmod 26
$$

### Encryption Process
- Convert plaintext letters to numbers.
- Add the key modulo 26.
- Convert back to letters.

### Decryption Process
- Subtract the same key modulo 26.

### Worked Example
Plaintext: CRYPTOGRAPHY
Key: 5

Ciphertext: HWDUYTLWFUMD

### Advantages
- Simple mathematical model
- Great for introducing modular arithmetic

### Disadvantages
- Small key space
- Easily broken by brute force

### Difficulty
- Easy

### Summary
The additive cipher demonstrates that even a slightly mathematical substitution rule is still very weak if the key space is small.

---

## Multiplicative Cipher

### Definition
The multiplicative cipher multiplies each letter position by a key modulo 26.

### Formula

$$
C = (P \times K) \bmod 26
$$

### Key Requirement
The multiplier must be coprime with 26 so that an inverse exists for decryption.

### Valid Keys
- 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

### Encryption Process
- Convert letters to positions.
- Multiply by the key.
- Apply modulo 26.

### Decryption Process
- Use the modular inverse of the key.

### Worked Example
Plaintext: HELLO
Key: 5

Ciphertext: JUDDS

### Advantages
- Introduces modular multiplication
- Slightly more mathematical than Caesar

### Disadvantages
- Limited valid keys
- Still vulnerable to cryptanalysis

### Difficulty
- Easy to medium

### Summary
The multiplicative cipher shows how mathematical structure can make a cipher more complex, but not necessarily secure.

---

## Affine Cipher

### Definition
The Affine Cipher combines multiplication and addition.

### Formula

$$
C = (aP + b) \bmod 26
$$

Where:
- $a$ = multiplicative key, must be coprime with 26
- $b$ = additive key

### Key Requirements
- $a$ must be one of the valid multiplicative keys.
- $b$ can be any value from 0 to 25.

### Encryption Process
1. Convert plaintext letter to a number.
2. Multiply by $a$.
3. Add $b$.
4. Apply modulo 26.

### Decryption Process
Use the modular inverse of $a$:

$$
P \equiv a^{-1}(C - b) \bmod 26
$$

### Worked Example
Plaintext: AFFINE
$a = 5$, $b = 8$

Ciphertext: IHHWVC

### Advantages
- More flexible than simpler monoalphabetic ciphers
- Excellent for teaching modular inverses

### Disadvantages
- Still weak against frequency analysis
- Much more complex than Caesar but still not secure

### Difficulty
- Medium

### Summary
The Affine Cipher illustrates how combining two simple operations can create a richer substitution system, but it remains breakable.

---

# POLYALPHABETIC CIPHERS

## Vigenère Cipher

### Definition
The Vigenère Cipher uses a repeating keyword so that each letter is shifted by a different amount.

### Formula

$$
C_i = (P_i + K_{i \bmod n}) \bmod 26
$$

### How It Works
1. Choose a keyword.
2. Repeat the keyword to match the plaintext length.
3. Shift each plaintext letter according to its corresponding keyword letter.

### Encryption Process
- Convert both plaintext and keyword letters to positions.
- Add the corresponding values modulo 26.
- Convert the result back to letters.

### Decryption Process
- Subtract the keyword positions modulo 26.

### Worked Example
Plaintext: VIGENERE
Keyword: CIPHER

Ciphertext: XQVLRVTM

### Advantages
- More resistant to simple frequency analysis
- Introduces the idea of changing shifts over time

### Disadvantages
- Can be broken once the key length is discovered
- Vulnerable to Kasiski analysis

### Difficulty
- Medium

### Historical Note
The Vigenère Cipher was considered very strong for centuries until cryptanalysts discovered better methods for finding key length.

### Summary
The Vigenère Cipher is the classical example of a polyalphabetic substitution system.

---

## Homophonic Cipher

### Definition
A homophonic cipher maps each plaintext letter to several possible ciphertext symbols so that frequency patterns are less obvious.

### How It Works
- Common letters such as E may have many substitutes.
- Rare letters may have fewer options.

### Example
- E may map to 17, 42, 68, 91, 15, or 73.
- T may map to 19, 54, 88, or 32.

### Advantages
- Makes simple frequency counts less useful
- More sophisticated than single-symbol substitution

### Disadvantages
- Harder to implement manually
- Still not secure by modern standards

### Difficulty
- Medium

### Summary
The homophonic cipher shows how a cipher can be made less obvious by giving letters multiple possible substitutes.

---

# BLOCK SUBSTITUTION CIPHERS

## Playfair Cipher

### Definition
The Playfair Cipher encrypts letters in pairs, called digraphs, using a 5x5 matrix.

### How It Works
1. Build a 5x5 matrix from a keyword.
2. Split the plaintext into pairs.
3. Apply rules based on the position of the pair:
   - Same row: shift right
   - Same column: shift down
   - Rectangle: swap corners

### Encryption Process
- Prepare the plaintext into digraphs.
- Replace each pair using the matrix.

### Decryption Process
- Reverse the same rules by shifting left or up.

### Worked Example
With keyword PLAYFAIR, the plaintext HELLO is split into digraphs and encrypted in the matrix.

### Advantages
- Stronger than single-letter substitution
- Introduces pair-based encryption

### Disadvantages
- Still vulnerable to digraph analysis
- More complex to implement

### Difficulty
- Medium-hard

### Summary
The Playfair Cipher is a major step up from simple substitution because it works with pairs of letters rather than one at a time.

---

## Autokey Cipher

### Definition
The Autokey Cipher uses the plaintext itself to continue the key after the initial keyword.

### How It Works
The key is formed as:

```text
Keyword + Plaintext
```

### Example
Plaintext: AUTOKEY
Keyword: SECRET

The key grows as the plaintext is used.

### Advantages
- Avoids simple repetitive keyword patterns
- More complex than a standard repeated-key system

### Disadvantages
- Can be attacked if some plaintext is known
- Still not secure by modern standards

### Difficulty
- Medium

### Summary
The Autokey Cipher shows how a cipher can become more adaptive by extending the key with plaintext itself.

---

## Nihilist Cipher

### Definition
The Nihilist Cipher combines a Polybius square with a transposition-style process.

### How It Works
1. Convert letters to coordinates from a Polybius square.
2. Combine those numbers to form a representation.
3. Use a keyword-based arrangement to produce ciphertext.

### Example
A letter such as A may be encoded as 11, while B becomes 12, and so on.

### Advantages
- More complex than simple substitution
- Shows how classical methods can be combined

### Disadvantages
- Vulnerable to cryptanalysis
- Historically not secure enough for modern use

### Difficulty
- Medium-hard

### Summary
The Nihilist Cipher is an interesting hybrid and helps show the evolution of classical cryptography.

---

## One-Time Pad Cipher

### Definition
The One-Time Pad uses a random key that is as long as the plaintext and is used only once.

### Formula

$$
C = (P + K) \bmod 26
$$

### Requirements
- The key must be truly random.
- The key must be as long as the plaintext.
- The key must never be reused.

### Advantages
- Theoretically unbreakable if used correctly
- Provides perfect secrecy in theory

### Disadvantages
- Key distribution is difficult
- Practical key management is hard

### Difficulty
- Medium

### Important Note
A one-time pad is secure only when the key is truly random, secret, and never reused.

### Summary
The One-Time Pad is the most important theoretical cipher in classical cryptography because it shows what perfect secrecy looks like.

---

## Comparison and Learning Path

### Quick Comparison Table

| Cipher | Type | Key Space | Security | Breakable |
|--------|------|-----------|----------|-----------|
| Caesar | Monoalphabetic | 26 | Very weak | Yes |
| Additive | Monoalphabetic | 26 | Very weak | Yes |
| Multiplicative | Monoalphabetic | 12 valid keys | Very weak | Yes |
| Affine | Monoalphabetic | 312 | Weak | Yes |
| Vigenère | Polyalphabetic | Large | Weak-medium | Yes |
| Homophonic | Polyalphabetic-style | Variable | Weak | Yes |
| Playfair | Digraph | Large | Medium | Yes |
| Autokey | Polyalphabetic | Variable | Medium | Yes |
| Nihilist | Hybrid | Variable | Medium | Yes |
| One-Time Pad | Theoretical perfect | Infinite in principle | Perfect if used correctly | No, if correctly implemented |

### Suggested Learning Order
1. Caesar Cipher
2. Additive Cipher
3. Multiplicative Cipher
4. Affine Cipher
5. Vigenère Cipher
6. Homophonic Cipher
7. Playfair Cipher
8. Autokey Cipher
9. Nihilist Cipher
10. One-Time Pad

### Key Insights
- Simple substitution is easy to understand but weak.
- Polyalphabetic methods are more complex and harder to break.
- Classical ciphers are excellent for learning, but modern security requires modern cryptography.

---

## Summary

Substitution ciphers introduce the core ideas of cryptography: changing symbols, using keys, and protecting meaning. They are excellent for learning the foundations of encryption, but they are not suitable for protecting real data in modern systems. Modern solutions such as AES, RSA, and secure protocols build on these ideas with far stronger mathematics and key management.

Next, continue with the transposition lesson to see how rearranging letters can also create encryption.
