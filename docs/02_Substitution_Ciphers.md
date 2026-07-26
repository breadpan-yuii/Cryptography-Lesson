# 02. Substitution Ciphers

This chapter merges the main lesson content with the extended substitution guide into a single complete learning resource for beginners.

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

This is the simplest form of substitution.

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
- $P$ = plaintext position
- $K$ = shift value
- $C$ = ciphertext position

### How It Works
1. Convert letters to numbers from 0 to 25.
2. Add the key.
3. Wrap around the alphabet using modulo 26.
4. Convert the result back to letters.

### Worked Example
Plaintext: HELLO
Key: 3

Result: KHOOR

### Advantages
- Very easy to understand
- Fast to implement
- Great for teaching the idea of encryption

### Disadvantages
- Only 26 possible shifts
- Very weak against brute force and frequency analysis

### Difficulty
- Very easy

### Real-World Relevance
- Historical importance only
- Used as a teaching example and for simple encoding such as ROT13

---

## Additive Cipher

### Definition
An additive cipher is a form of Caesar cipher that uses modular addition on letter positions.

### Formula

$$
C = (P + K) \bmod 26
$$

### Example
Plaintext: CRYPTOGRAPHY
Key: 5

Ciphertext: HWDUYTLWFUMD

### Advantages
- Simple to explain with modular arithmetic
- Easy to implement by hand

### Disadvantages
- Still vulnerable to brute-force attacks
- Small key space

### Difficulty
- Easy

---

## Multiplicative Cipher

### Definition
A multiplicative cipher multiplies each letter position by a key value modulo 26.

### Formula

$$
C = (P \times K) \bmod 26
$$

The key must be coprime with 26 so that decryption is possible.

### Valid Keys
The valid keys are:
- 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

### Example
Plaintext: HELLO
Key: 5

Ciphertext: JUDDS

### Advantages
- Introduces modular multiplication
- Slightly more mathematical than Caesar

### Disadvantages
- Limited valid keys
- Still breakable by simple analysis

### Difficulty
- Easy to medium

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

### Example
Plaintext: AFFINE
Key values: $a=5$, $b=8$

Ciphertext: IHHWVC

### Advantages
- More flexible than Caesar or additive ciphers
- Teaches modular inverses and combined operations

### Disadvantages
- Still weak against frequency analysis
- Key space is larger but still small by modern standards

### Difficulty
- Medium

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
3. Shift each plaintext letter by the corresponding keyword letter.

### Example
Plaintext: VIGENERE
Keyword: CIPHER

Ciphertext: XQVLRVTM

### Advantages
- More resistant to simple frequency analysis than monoalphabetic ciphers
- Introduces the idea of key repetition and polyalphabetic structure

### Disadvantages
- Can be broken once the key length is discovered
- Vulnerable to Kasiski analysis and frequency methods

### Difficulty
- Medium

### Historical Note
The Vigenère Cipher was considered very strong for centuries until methods for discovering the key length were developed.

---

## Homophonic Cipher

### Definition
A homophonic cipher maps each plaintext letter to several possible ciphertext symbols so that frequency patterns become less obvious.

### How It Works
- Common letters such as E may have several possible substitutes.
- Rare letters may have fewer options.

### Example
- E may map to 17, 42, 68, 91, 15, or 73
- T may map to 19, 54, 88, or 32

### Advantages
- Makes simple frequency counts less useful
- More complex than Caesar-like systems

### Disadvantages
- More difficult to implement manually
- Still not secure by modern standards

### Difficulty
- Medium

---

# BLOCK SUBSTITUTION CIPHERS

## Playfair Cipher

### Definition
The Playfair Cipher encrypts letters in pairs, called digraphs, using a 5x5 matrix.

### How It Works
1. Build a 5x5 matrix from a keyword.
2. Split the plaintext into pairs.
3. Apply one of three rules:
   - Same row: shift right
   - Same column: shift down
   - Rectangle: swap corners

### Example
With keyword PLAYFAIR, the plaintext HELLO is prepared and encrypted in digraphs.

### Advantages
- Stronger than single-letter substitution
- Uses pair-based structure

### Disadvantages
- Still vulnerable to digraph analysis
- More complicated than earlier ciphers

### Difficulty
- Medium-hard

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
- More complex than a standard Vigenère-like system

### Disadvantages
- Can be attacked if some plaintext is known
- Still not secure by modern standards

### Difficulty
- Medium

---

## Nihilist Cipher

### Definition
The Nihilist Cipher combines a Polybius square with a transposition-style process.

### How It Works
1. Convert letters to coordinates from a Polybius square.
2. Combine those values to form a numeric representation.
3. Use a keyword-based arrangement to create the ciphertext.

### Example
A letter such as A may be encoded as 11, while B becomes 12, and so on.

### Advantages
- More complex than simple substitution
- Shows how classical systems can be combined

### Disadvantages
- Vulnerable to cryptanalysis
- Historically not secure enough for modern needs

### Difficulty
- Medium-hard

---

## One-Time Pad Cipher

### Definition
The One-Time Pad uses a random key that is as long as the plaintext and is used only once.

### Formula

$$
C = (P + K) \bmod 26
$$

### Requirements
- The key must be random.
- The key must be at least as long as the plaintext.
- The key must never be reused.

### Advantages
- Theoretically unbreakable if used correctly
- Provides perfect secrecy in theory

### Disadvantages
- Key distribution is difficult
- Practical management of long random keys is hard

### Difficulty
- Medium

### Important Note
A one-time pad is secure only when the key is truly random, secret, and never reused.

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
- Classical ciphers are great for learning, but modern security requires modern cryptography.

---

## Summary

Substitution ciphers introduce the core ideas of cryptography: changing symbols, using keys, and protecting meaning. They are excellent for learning the foundations of encryption, but they are not suitable for protecting real data in modern systems. Modern solutions such as AES, RSA, and secure protocols build on these ideas with far stronger mathematics and key management.

Next, continue with the transposition lesson to see how rearranging letters can also create encryption.

