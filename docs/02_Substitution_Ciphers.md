# 02. Substitution Ciphers

Navigation: [Previous: 01. Introduction to Cryptography](01_Introduction_to_Cryptography.md) | [Next: 03. Transposition Ciphers](03_Transposition_Ciphers.md)

This chapter combines the main lesson overview with the richer extended guide so that the full substitution cipher material is available in one place.

## Table of Contents
1. [What is a Substitution Cipher?](#what-is-a-substitution-cipher)
2. [Visual Overview](#visual-overview)
3. [Monoalphabetic Ciphers](#monoalphabetic-ciphers)
   - [Caesar Cipher](#caesar-cipher)
   - [Additive Cipher](#additive-cipher)
   - [Multiplicative Cipher](#multiplicative-cipher)
   - [Affine Cipher](#affine-cipher)
4. [Polyalphabetic Ciphers](#polyalphabetic-ciphers)
   - [Vigenère Cipher](#vigenère-cipher)
   - [Homophonic Cipher](#homophonic-cipher)
5. [Block Substitution Ciphers](#block-substitution-ciphers)
   - [Playfair Cipher](#playfair-cipher)
   - [Autokey Cipher](#autokey-cipher)
   - [Nihilist Cipher](#nihilist-cipher)
   - [One-Time Pad Cipher](#one-time-pad-cipher)
6. [Comparison and Learning Path](#comparison-and-learning-path)
7. [Summary](#summary)

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

## Visual Overview

Substitution ciphers can be grouped by how many alphabets or symbols they use. This helps explain why some are easier to break than others.

```text
Substitution Ciphers
|
+-- Monoalphabetic
|   |
|   +-- Caesar
|   +-- Additive
|   +-- Multiplicative
|   +-- Affine
|
+-- Polyalphabetic
|   |
|   +-- Vigenère
|   +-- Autokey
|   +-- One-Time Pad
|
+-- Multiple-symbol or block methods
    |
    +-- Homophonic
    +-- Playfair
    +-- Nihilist
```

### Substitution vs. Transposition

| Feature | Substitution Cipher | Transposition Cipher |
|---------|---------------------|----------------------|
| Main action | Replaces symbols | Rearranges symbols |
| Letter order | Usually stays the same | Changes position |
| Letter identity | Changes | Usually stays the same |
| Example | HELLO -> KHOOR | HELLO -> HLOEL |
| Common weakness | Frequency patterns may remain | Position patterns may remain |

### Encryption Flow

```text
Plaintext
   |
   v
Choose substitution rule + key
   |
   v
Replace each letter or letter group
   |
   v
Ciphertext
```

### Letter-to-Number Reference

Many examples use modular arithmetic, so letters are treated as numbers from 0 to 25.

| Letter | A | B | C | D | E | F | G | H | I | J | K | L | M |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |

| Letter | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|--------|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |

### Frequency Analysis Idea

Substitution ciphers often preserve language patterns. In English, letters such as E, T, A, O, I, and N appear more often than letters such as Q, X, and Z. A cryptanalyst can compare ciphertext letter counts with normal English frequencies.

```text
Typical English frequency, simplified

E | ###########
T | #########
A | ########
O | #######
I | #######
N | #######
S | ######
H | ######
R | ######
Q | #
X | #
Z | #
```

For a simple substitution cipher, the most common ciphertext letter may represent E, T, or A. This does not solve the cipher by itself, but it gives a strong clue.

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

### Visual Alphabet Shift

```text
Plain:  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
Shift:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

### Full Mapping Table

For key 3, every plaintext letter maps to the ciphertext letter three positions ahead.

| Plain | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |

### Step-by-Step Table

| Plain letter | Number | Add key 3 | Mod 26 result | Cipher letter |
|--------------|--------|-----------|---------------|---------------|
| H | 7 | 10 | 10 | K |
| E | 4 | 7 | 7 | H |
| L | 11 | 14 | 14 | O |
| L | 11 | 14 | 14 | O |
| O | 14 | 17 | 17 | R |

### Brute Force Visual

Because Caesar has only 26 possible shifts, an attacker can simply try every key.

| Key | Decryption Attempt |
|-----|--------------------|
| 1 | JGNNQ |
| 2 | IFMMP |
| 3 | HELLO |
| 4 | GDKKN |
| 5 | FCJJM |

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

### Additive Mapping Example

With key 5, every value moves forward by five positions.

| Plain | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Value | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 |
| + 5 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
| Mod 26 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 0 | 1 | 2 | 3 | 4 |
| Cipher | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C | D | E |

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

### Why Only Some Keys Work

A multiplicative key must have no common factor with 26 except 1. If it shares a factor with 26, two different plaintext letters may encrypt to the same ciphertext letter, making decryption impossible.

| Key | Shares factor with 26? | Valid? | Reason |
|-----|------------------------|--------|--------|
| 2 | Yes | No | 2 divides 26 |
| 5 | No | Yes | Has a modular inverse |
| 13 | Yes | No | 13 divides 26 |
| 15 | No | Yes | Has a modular inverse |
| 25 | No | Yes | Has a modular inverse |

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

### Multiplication Table

| Plain letter | Value | x 5 | Mod 26 | Cipher letter |
|--------------|-------|-----|--------|---------------|
| H | 7 | 35 | 9 | J |
| E | 4 | 20 | 20 | U |
| L | 11 | 55 | 3 | D |
| L | 11 | 55 | 3 | D |
| O | 14 | 70 | 18 | S |

### Full Mapping Table

For key 5, the multiplicative mapping is:

| Plain | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher | A | F | K | P | U | Z | E | J | O | T | Y | D | I | N | S | X | C | H | M | R | W | B | G | L | Q | V |

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

### Affine Operation Diagram

```text
Plain value P
     |
     v
Multiply by a
     |
     v
Add b
     |
     v
Take mod 26
     |
     v
Cipher value C
```

### Worked Calculation Table

Using $a = 5$ and $b = 8$:

| Plain | P | 5P + 8 | Mod 26 | Cipher |
|-------|---|--------|--------|--------|
| A | 0 | 8 | 8 | I |
| F | 5 | 33 | 7 | H |
| F | 5 | 33 | 7 | H |
| I | 8 | 48 | 22 | W |
| N | 13 | 73 | 21 | V |
| E | 4 | 28 | 2 | C |

### Full Mapping Table

For $a = 5$ and $b = 8$, the complete Affine substitution is:

| Plain | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cipher | I | N | S | X | C | H | M | R | W | B | G | L | Q | V | A | F | K | P | U | Z | E | J | O | T | Y | D |

### Key Space

The Affine Cipher has 12 valid choices for $a$ and 26 choices for $b$.

```text
12 valid multipliers x 26 shifts = 312 possible keys
```

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

### Repeating Keyword Table

| Position | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|----------|---|---|---|---|---|---|---|---|
| Plaintext | V | I | G | E | N | E | R | E |
| Plain value | 21 | 8 | 6 | 4 | 13 | 4 | 17 | 4 |
| Keyword | C | I | P | H | E | R | C | I |
| Key value | 2 | 8 | 15 | 7 | 4 | 17 | 2 | 8 |
| Cipher value | 23 | 16 | 21 | 11 | 17 | 21 | 19 | 12 |
| Ciphertext | X | Q | V | L | R | V | T | M |

### Shift Pattern Visual

The Vigenère Cipher is stronger than Caesar because the shift changes at each position.

```text
Plaintext:  V I G E N E R E
Keyword:    C I P H E R C I
Shift:      2 8 15 7 4 17 2 8
Ciphertext: X Q V L R V T M
```

### Caesar vs. Vigenère

| Feature | Caesar | Vigenère |
|---------|--------|----------|
| Number of alphabets | 1 | Many |
| Key type | Number shift | Keyword |
| Same plaintext letter always encrypts the same way? | Yes | Not always |
| Main weakness | Brute force | Key length discovery |

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

### Sample Homophonic Table

Common letters receive more possible symbols to flatten frequency patterns.

| Plain letter | Possible ciphertext symbols |
|--------------|-----------------------------|
| E | 17, 42, 68, 91, 15, 73 |
| T | 19, 54, 88, 32 |
| A | 07, 26, 58, 90 |
| O | 11, 39, 64 |
| Q | 44 |
| Z | 02 |

### Frequency Flattening Visual

```text
Before homophonic substitution:
E | ###########
T | #########
A | ########
Q | #
Z | #

After symbols are spread out:
17 | ###
42 | ##
68 | ##
91 | ##
15 | #
73 | #
19 | ##
54 | ##
88 | ##
32 | #
```

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

### Example Playfair Matrix

Using the keyword PLAYFAIR and combining I/J:

|   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | P | L | A | Y | F |
| 2 | I/J | R | B | C | D |
| 3 | E | G | H | K | M |
| 4 | N | O | Q | S | T |
| 5 | U | V | W | X | Z |

### Digraph Preparation

| Original text | Prepared pairs | Note |
|---------------|----------------|------|
| HELLO | HE LX LO | Repeated L is separated with X |
| BALLOON | BA LX LO ON | Repeated L is separated |
| GOLD | GO LD | Already valid pairs |

### Rule Visuals

```text
Same row: choose the letter to the right

P L A Y F
    ^   ^
    A -> Y

Same column: choose the letter below

A
B
H
Q
W

A -> B

Rectangle: swap columns

H . K
. . .
Q . S

H with S becomes K with Q
```

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

### Key Extension Table

| Plaintext | A | U | T | O | K | E | Y |
|-----------|---|---|---|---|---|---|---|
| Starting keyword | S | E | C | R | E | T |   |
| Extended key | S | E | C | R | E | T | A |

After the keyword is used, plaintext letters begin feeding into the key stream.

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

### Polybius Square Example

|   | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| 1 | A | B | C | D | E |
| 2 | F | G | H | I/J | K |
| 3 | L | M | N | O | P |
| 4 | Q | R | S | T | U |
| 5 | V | W | X | Y | Z |

### Coordinate Examples

| Letter | Row | Column | Coordinate |
|--------|-----|--------|------------|
| A | 1 | 1 | 11 |
| H | 2 | 3 | 23 |
| T | 4 | 4 | 44 |
| Z | 5 | 5 | 55 |

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

### One-Time Pad Table

| Plaintext | A | T | T | A | C | K |
|-----------|---|---|---|---|---|---|
| Plain value | 0 | 19 | 19 | 0 | 2 | 10 |
| Random key | X | M | C | K | L | P |
| Key value | 23 | 12 | 2 | 10 | 11 | 15 |
| Cipher value | 23 | 5 | 21 | 10 | 13 | 25 |
| Ciphertext | X | F | V | K | N | Z |

### Perfect Secrecy Conditions

```text
Secure one-time pad
|
+-- Key is truly random
+-- Key is as long as the message
+-- Key is kept secret
+-- Key is used exactly once

If any condition fails, the security claim fails.
```

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

### Visual Strength Scale

This scale shows educational strength, not modern production security.

```text
Very weak       Weak             Medium             Perfect if correct
|---------------|----------------|------------------|
Caesar
Additive
Multiplicative
Affine
                Vigenère
                Homophonic
                                  Playfair
                                  Autokey
                                  Nihilist
                                                     One-Time Pad
```

### Concept Comparison Table

| Cipher | Main idea | Best lesson it teaches | Main attack idea |
|--------|-----------|------------------------|------------------|
| Caesar | Fixed shift | Modulo arithmetic | Try all shifts |
| Additive | Numeric Caesar model | Addition mod 26 | Try all keys |
| Multiplicative | Multiply positions | Modular inverses | Test valid multipliers |
| Affine | Multiply then add | Combining operations | Frequency analysis |
| Vigenère | Repeating keyword shifts | Polyalphabetic substitution | Find key length |
| Homophonic | Many symbols per common letter | Hiding frequency | Pattern and symbol analysis |
| Playfair | Encrypt pairs | Digraph substitution | Digraph frequency analysis |
| Autokey | Key grows from plaintext | Key stream design | Known plaintext |
| Nihilist | Coordinates plus keywords | Hybrid classical design | Statistical analysis |
| One-Time Pad | Random one-use key | Perfect secrecy | Key reuse or bad randomness |

### Common Weaknesses Chart

| Weakness | Affects | Why it matters |
|----------|---------|----------------|
| Small key space | Caesar, Additive, Multiplicative, Affine | Attackers can test every key quickly |
| Letter frequency leaks | Most monoalphabetic ciphers | Common plaintext letters create patterns |
| Repeated key pattern | Vigenère | Repetition can reveal key length |
| Known plaintext | Autokey, Vigenère, many classical ciphers | Some known message text can expose key material |
| Key management | One-Time Pad | The method is only perfect when the key rules are followed exactly |

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
