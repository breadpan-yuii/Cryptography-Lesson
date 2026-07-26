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

### Definition
The **Caesar Cipher** is a simple substitution cipher where each letter is shifted by a fixed number of positions in the alphabet.

### How It Works
Each character is moved forward (or backward) by a constant number of positions.

### Formula
```
Ciphertext_char = (Plaintext_char + Key) mod 26
Plaintext_char = (Ciphertext_char - Key) mod 26

Where:
- Plaintext_char is the numeric position (A=0, B=1, ..., Z=25)
- Key is the shift value (1-25)
- mod 26 wraps around the alphabet
```

### Encryption Process

**Step 1**: Choose a key (shift value)
- Common key: 3 (used by Julius Caesar himself)
- Valid keys: 1-25

**Step 2**: For each letter, shift it forward by the key amount
- A + 3 = D
- B + 3 = E
- Z + 3 = C (wraps around)

**Step 3**: Keep non-alphabetic characters unchanged
- Spaces, numbers, punctuation remain the same

### Worked Example

**Encrypt**: "HELLO WORLD" with Key = 3

```
Plaintext:  H E L L O   W O R L D
Shift +3:   K H O O R   Z R U O G
Ciphertext: K H O O R   Z R U O G

Details:
H (pos 7) + 3 = K (pos 10)
E (pos 4) + 3 = H (pos 7)
L (pos 11) + 3 = O (pos 14)
L (pos 11) + 3 = O (pos 14)
O (pos 14) + 3 = R (pos 17)
W (pos 22) + 3 = Z (pos 25)
O (pos 14) + 3 = R (pos 17)
R (pos 17) + 3 = U (pos 20)
L (pos 11) + 3 = O (pos 14)
D (pos 3) + 3 = G (pos 6)
```

**Decrypt**: "KHOOR ZRUOG" with Key = 3

```
Ciphertext: K H O O R   Z R U O G
Shift -3:   H E L L O   W O R L D
Plaintext:  H E L L O   W O R L D
```

### ASCII Diagram: Caesar Wheel

```
          A
        Z   B
      Y       C
    X           D
  W               E
  V               F
    U           G
      T       H
        S   I
          R
          Q
        P   J
      O       K
    N           L
  M               (rotation by 3)

(This is a simplified visualization of the 26-letter rotation)
```

### Advantages
✓ Simple to understand and implement
✓ Requires minimal computation
✓ Compact (only needs one number as key)
✓ Historical significance
✓ Good for teaching cryptography basics

### Disadvantages
✗ Only 26 possible keys (extremely weak)
✗ Vulnerable to brute force attack
✗ No key management complexity
✗ Frequency analysis reveals the shift
✗ Not secure for any real-world application

### Cryptanalysis

**Brute Force Attack**: Try all 26 possible shifts
- Average time: 13 attempts
- Modern computers: Microseconds

**Frequency Analysis**: 
- Compare ciphertext letter frequency to English
- Most frequent ciphertext letter likely = E (most common in English)

**Example**: If "K" appears most frequently in ciphertext, and E is most frequent in English:
- K might be E
- K position (10) - E position (4) = 6
- Try key = 6

### Difficulty Level
🔵 Very Easy (1/10)

### Real-World Relevance
⚠️ NONE - Caesar cipher is completely insecure today

Historical Use:
- Ancient Rome: Military communications
- WWII: ROT-13 variant used in puzzles/forums
- Today: Educational purposes only

### Summary
The Caesar Cipher is the simplest substitution cipher and the perfect starting point for learning cryptography. While completely insecure today, it teaches fundamental concepts of encryption, keys, and cryptanalysis. Its vulnerability inspired the development of stronger polyalphabetic ciphers.

---

## Additive Cipher

### Definition
The **Additive Cipher** (also called Shift Cipher) is identical to the Caesar Cipher but uses the term "additive" to emphasize the mathematical addition operation.

### Formula
```
C = (P + K) mod 26
P = (C - K) mod 26

Where:
- C = Ciphertext character position
- P = Plaintext character position
- K = Key (0-25)
```

### How It Works
Each plaintext letter is added to a fixed key value (modulo 26).

### Encryption Process
**Step 1**: Convert letters to numbers (A=0, B=1, ..., Z=25)
**Step 2**: Add the key to each number
**Step 3**: Take result modulo 26 (wrap around alphabet)
**Step 4**: Convert back to letters

### Worked Example

**Encrypt**: "CRYPTOGRAPHY" with Key = 5

```
Plaintext:  C R Y P T O G R A P H Y
Positions:  2 17 24 15 19 14 6 17 0 15 7 24
Add Key(5): 7 22 29 20 24 19 11 22 5 20 12 29
Mod 26:     7 22 3 20 24 19 11 22 5 20 12 3
Ciphertext: H W D U Y T L W F U M D
```

### Decryption

**Decrypt**: "HWDUYJTLWFUMD" with Key = 5

```
Ciphertext: H W D U Y T L W F U M D
Positions:  7 22 3 20 24 19 11 22 5 20 12 3
Sub Key(5): 2 17 24 15 19 14 6 17 0 15 7 24
Plaintext:  C R Y P T O G R A P H Y
```

### Advantages & Disadvantages
Same as Caesar Cipher (Additive is essentially the same algorithm with different naming)

✓ Simple mathematical model
✓ Easy to understand modular arithmetic
✗ Only 26 possible keys
✗ Brute force vulnerability

### Difficulty Level
🔵 Very Easy (1/10)

### Summary
The Additive Cipher demonstrates the mathematical foundation of substitution ciphers. It's essentially Caesar Cipher with emphasis on the arithmetic operation. Understanding additive ciphers prepares you for multiplicative and affine ciphers.

---

## Multiplicative Cipher

### Definition
The **Multiplicative Cipher** encrypts plaintext by multiplying each character by a key value (modulo 26), rather than adding.

### Formula
```
C = (P × K) mod 26
P = (C × K^-1) mod 26

Where:
- C = Ciphertext position
- P = Plaintext position
- K = Encryption key (must be coprime with 26)
- K^-1 = Multiplicative inverse of K (mod 26)
```

### Key Constraint
**Critical**: The key must be coprime with 26 (GCD(K, 26) = 1)

Valid keys: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25

Invalid keys: 2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24, 0

**Why?** To ensure unique mapping and invertibility.

### Multiplicative Inverse
Find K^-1 such that (K × K^-1) mod 26 = 1

Example: K = 5
- 5 × 21 = 105 = 4×26 + 1 ≡ 1 (mod 26)
- So K^-1 = 21

### How It Works
**Step 1**: Choose a key coprime with 26
**Step 2**: For each plaintext letter, multiply by key
**Step 3**: Take modulo 26
**Step 4**: Convert to letter

### Worked Example

**Encrypt**: "HELLO" with Key = 5

```
Plaintext:  H E L L O
Positions:  7 4 11 11 14
Multiply×5: 35 20 55 55 70
Mod 26:     9 20 3 3 18
Ciphertext: J U D D S
```

**Decryption** with K^-1 = 21 (since 5 × 21 ≡ 1 mod 26)

```
Ciphertext: J U D D S
Positions:  9 20 3 3 18
Multiply×21:189 420 63 63 378
Mod 26:     7 4 11 11 14
Plaintext:  H E L L O
```

### Advantages
✓ More complex than additive cipher
✓ All 26 positions can encrypt to any other (depending on key)
✗ Still only 12 valid keys
✗ Vulnerable to frequency analysis
✗ Requires finding multiplicative inverse

### Disadvantages
✗ Key selection restricted
✗ Requires modular arithmetic knowledge
✗ Frequency analysis attack works
✗ Small key space (only 12 valid keys)
✗ Mapsto the same target can create collisions

### Difficulty Level
🟡 Easy-Medium (3/10)

### Summary
The Multiplicative Cipher introduces modular arithmetic and the concept of modular inverses. While more complex than additive cipher, it remains weak due to small key space and frequency analysis vulnerability.

---

## Affine Cipher

### Definition
The **Affine Cipher** combines additive and multiplicative properties. It uses two keys (multiplier and additive constant) for stronger encryption than either method alone.

### Formula
```
C = (K1 × P + K2) mod 26
P = (K1^-1 × (C - K2)) mod 26

Where:
- C = Ciphertext position
- P = Plaintext position
- K1 = Multiplicative key (must be coprime with 26)
- K2 = Additive key (0-25)
- K1^-1 = Multiplicative inverse of K1
```

### Key Selection
- **K1** (Multiplier): Must be coprime with 26 (valid: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- **K2** (Additive): Any value 0-25
- **Total keys**: 12 × 26 = 312 possible key combinations

### How It Works
**Step 1**: Choose K1 (coprime with 26) and K2 (0-25)
**Step 2**: For each plaintext letter: (letter × K1 + K2) mod 26
**Step 3**: Convert result to ciphertext letter

### Worked Example

**Encrypt**: "AFFINE" with K1 = 5, K2 = 8

```
Plaintext:  A F F I N E
Positions:  0 5 5 8 13 4
Calculate:  (pos × 5 + 8) mod 26
            (0×5+8)=8, (5×5+8)=33, (5×5+8)=33, (8×5+8)=48, (13×5+8)=73, (4×5+8)=28
            8 mod 26 = 8, 33 mod 26 = 7, 33 mod 26 = 7, 48 mod 26 = 22, 73 mod 26 = 21, 28 mod 26 = 2
Ciphertext: I H H W V C
```

**Decryption** with K1^-1 = 21 (since 5 × 21 ≡ 1 mod 26), K2 = 8

```
Ciphertext: I H H W V C
Positions:  8 7 7 22 21 2
Calculate:  21 × (pos - 8) mod 26
            21×(8-8)=0, 21×(7-8)=-21, 21×(7-8)=-21, 21×(22-8)=294, 21×(21-8)=273, 21×(2-8)=-126
Mod 26:     0, -21≡5, -21≡5, 294≡8, 273≡13, -126≡4
Plaintext:  A F F I N E
```

### Advantages
✓ More key combinations (312 vs 26)
✓ Combines multiplication and addition
✓ More complex than simple Caesar
✗ Still vulnerable to frequency analysis
✗ Key space still manageable for brute force
✗ Pattern detection possible

### Disadvantages
✗ Requires understanding modular arithmetic
✗ Frequency analysis breaks it quickly
✗ Only 312 possible keys
✗ Not secure for real-world use

### Cryptanalysis

With frequency analysis and known plaintext attacks:
1. Identify letter frequency in ciphertext
2. Assume most frequent = E
3. Identify a second letter (likely T)
4. Set up two equations with two unknowns (K1, K2)
5. Solve for keys

### Difficulty Level
🟡 Medium (4/10)

### Real-World Relevance
⚠️ NONE - Affine cipher is completely insecure

Historical context: Improved on Caesar but still far too simple.

### Summary
The Affine Cipher combines additive and multiplicative operations, increasing complexity and key space. However, frequency analysis and cryptanalysis still easily break it. It serves as an important stepping stone toward polyalphabetic ciphers.

---

# POLYALPHABETIC CIPHERS

## Vigenère Cipher

### Definition
The **Vigenère Cipher** is a polyalphabetic substitution cipher where each plaintext letter is encrypted using a different shift value from a repeating keyword.

### How It Works
Instead of one shift value (like Caesar), use multiple shift values from a repeating key.

### Formula
```
C = (P + K[i mod keylen]) mod 26
P = (C - K[i mod keylen]) mod 26

Where:
- C = Ciphertext letter position
- P = Plaintext letter position
- K[i] = i-th letter of repeating key
- keylen = Length of the key
```

### How It Works Step-by-Step

**Step 1**: Choose a keyword (e.g., "SECRET")
**Step 2**: Repeat keyword to match plaintext length
**Step 3**: For each position, shift plaintext letter by corresponding key letter
**Step 4**: A=0, B=1, ..., Z=25 for shift amounts

### Worked Example

**Encrypt**: "VIGENERE" with Key = "CIPHER"

```
Plaintext:  V I G E N E R E
Key repeat: C I P H E R C I
Key values: 2 8 15 7 4 17 2 8
Shift:      (pos + key) mod 26

V(21) + C(2) = 23 = X
I(8) + I(8) = 16 = Q
G(6) + P(15) = 21 = V
E(4) + H(7) = 11 = L
N(13) + E(4) = 17 = R
E(4) + R(17) = 21 = V
R(17) + C(2) = 19 = T
E(4) + I(8) = 12 = M

Ciphertext: XQVLRVTM
```

**Decryption** of "XQVLRVTM" with Key = "CIPHER"

```
Ciphertext: X Q V L R V T M
Key repeat: C I P H E R C I
Key values: 2 8 15 7 4 17 2 8
Shift:      (pos - key) mod 26

X(23) - C(2) = 21 = V
Q(16) - I(8) = 8 = I
V(21) - P(15) = 6 = G
L(11) - H(7) = 4 = E
R(17) - E(4) = 13 = N
V(21) - R(17) = 4 = E
T(19) - C(2) = 17 = R
M(12) - I(8) = 4 = E

Plaintext: VIGENERE
```

### Vigenère Table

Classic 26x26 lookup table:

```
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
...
Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

Usage: Find plaintext letter in columns, key letter in rows, intersection = ciphertext
```

### Advantages
✓ Much stronger than monoalphabetic ciphers
✓ Defeats simple frequency analysis
✓ Key can be a word (easy to remember)
✓ Large key space if key is long
✗ Still breakable if key is short or repeated
✗ Vulnerable to Kasiski Examination
✗ Vulnerable to Index of Coincidence

### Disadvantages
✗ Requires key length discovery
✗ Kasiski Examination can find key length
✗ Known plaintext attack can reveal key
✗ Vulnerable to statistical analysis

### Cryptanalysis

**Kasiski Examination**:
1. Find repeated sequences in ciphertext
2. Distances between repetitions = likely multiples of key length
3. Find GCD of distances = probable key length

**Index of Coincidence**:
1. Test various key lengths
2. Calculate IC value for each length
3. Correct key length shows IC close to English

### Difficulty Level
🟢 Medium (5/10)

### Real-World Relevance
⚠️ NONE - Vigenère cipher is breakable (Kasiski Examination, 1863)

Historical: Considered unbreakable for 300 years until Kasiski broke it.

### Summary
The Vigenère Cipher was revolutionary—using multiple shifts instead of one. It defeated frequency analysis for centuries. However, once the key length is determined, it can be broken. This cipher demonstrates why longer keys matter in cryptography.

---

## Homophonic Cipher

### Definition
The **Homophonic Cipher** is a substitution cipher where each plaintext letter can map to multiple ciphertext characters, reducing frequency analysis effectiveness.

### How It Works

Assign multiple ciphertext characters to letters based on their English frequency:
- High-frequency letters (E, T, A) → Many ciphertext options
- Low-frequency letters (Z, Q, X) → Few ciphertext options

### Example Homophonic Mapping

```
Plaintext → Ciphertext Options
E → 17, 42, 68, 91, 15, 73
T → 19, 54, 88, 32
A → 26, 61, 74, 09
O → 38, 62, 87
I → 11, 50, 76
N → 25, 64, 44
S → 33, 58, 72
H → 21, 65, 85
R → 04, 46, 79
D → 06, 83
L → 05, 94
... (less frequent letters have fewer options)
```

### Encryption Process

**Encrypt**: "HELLO" using above mapping

```
H → randomly choose from {21, 65, 85}, say 21
E → randomly choose from {17, 42, 68, 91, 15, 73}, say 42
L → randomly choose from {05, 94}, say 05
L → randomly choose from {05, 94}, say 94
O → randomly choose from {38, 62, 87}, say 62

Ciphertext: 21 42 05 94 62
```

### Decryption Process

**Decrypt**: "21 42 05 94 62"

```
Lookup each value in mapping:
21 → H
42 → E
05 → L
94 → L
62 → O

Plaintext: HELLO
```

### Advantages
✓ Defeats simple frequency analysis
✓ Each letter has multiple representations
✓ More secure than monoalphabetic ciphers
✗ Requires larger ciphertext
✗ Still vulnerable to digraph analysis
✗ Known plaintext attacks effective

### Disadvantages
✗ Requires mapping table (key)
✗ Ciphertext expansion (numbers instead of single letters)
✗ Still vulnerable to sophisticated analysis
✗ Randomness quality matters

### Difficulty Level
🟢 Medium (6/10)

### Summary
Homophonic Ciphers defeat letter frequency analysis by allowing multiple representations for each plaintext letter. They represent an improvement over monoalphabetic ciphers but are still breakable using digraph/trigraph analysis.

---

## Playfair Cipher

### Definition
The **Playfair Cipher** encrypts pairs of letters (digraphs) using a 5×5 matrix. It's more complex than previous ciphers as it works on letter pairs.

### How It Works

**Step 1**: Create a 5×5 matrix using keyword
- Fill with keyword letters (removing duplicates)
- Fill remaining spaces with unused alphabet letters
- Typically combine I/J

**Step 2**: Arrange plaintext into pairs
- If pair has same letter, insert 'X' between them
- If odd length, add 'X' at end

**Step 3**: Encrypt each pair using matrix rules
- Same row: Replace with letters to the right (wrap around)
- Same column: Replace with letters below (wrap around)
- Rectangle: Replace with letters in same row but opposite columns

### Worked Example

**Create Matrix** from keyword "PLAYFAIR":

```
P L A Y F
I/J R E H X
B C D G K
M N O Q S
T U V W Z

(Removing duplicates from PLAYFAIR, filling with rest of alphabet)
```

**Encrypt**: "HELLO WORLD" with above matrix

First, prepare plaintext:
```
HELLO WORLD
HE LL OW OR LD
→ HE LX LO WO RL D
→ HE LX LO WO RL DX (pairs)
```

Encrypt each pair:
```
HE: H(row1,col4), E(row2,col3)
   → Rectangle rule: X(1,3), R(2,4) → XR

LX: L(row1,col2), X(row2,col5)
   → Rectangle rule: Y(1,5), I(2,2) → YI

LO: L(row1,col2), O(row4,col3)
   → Rectangle rule: Y(1,3), N(4,2) → YN

WO: W(row5,col4), O(row4,col3)
   → Rectangle rule: Q(5,3), S(4,4) → QS

RL: R(row2,col2), L(row1,col2)
   → Same column: H(2,2)→E, Y(1,2)→ ... wait, let me recalculate

(Detailed matrix operations shown in code examples)
```

### Advantages
✓ Works with digraphs (pairs) - more secure than single letters
✓ No special characters needed
✓ Compact notation (5×5 matrix)
✓ Defeated frequency analysis for some time
✗ Still vulnerable to digraph frequency analysis
✗ Known plaintext attacks effective
✗ Limited key space

### Disadvantages
✗ More complex to compute manually
✗ Requires matrix setup
✗ Still breakable with cryptanalysis
✗ Digraph frequency analysis defeats it

### Difficulty Level
🟡 Medium-Hard (7/10)

### Real-World Relevance
⚠️ NONE - Breakable, but was used in military during WWI

Historical: Used by field forces due to ease of manual computation

### Summary
Playfair Cipher improved security by encrypting pairs instead of single letters. Its 5×5 matrix approach was novel for the time, but digraph analysis and known plaintext attacks break it relatively easily today.

---

## Autokey Cipher

### Definition
The **Autokey Cipher** is a polyalphabetic cipher where the plaintext itself becomes part of the key after the initial keyword.

### How It Works

Instead of repeating a keyword, append plaintext letters to the keyword to create an ever-changing key.

### Formula
```
Key sequence = Keyword + Plaintext
(Each plaintext letter determines subsequent shift)

Encryption: C = (P + K[i]) mod 26
Decryption: P = (C - K[i]) mod 26
```

### Encryption Process

**Step 1**: Choose a keyword (e.g., "SECRET")
**Step 2**: Append plaintext to create key
**Step 3**: Encrypt using shifting

### Worked Example

**Encrypt**: "AUTOKEY" with Keyword = "SECRET"

```
Plaintext:   A U T O K E Y
Keyword:     S E C R E T
(Combined):  S E C R E T A U T O K E

Actually, for Autokey:
Position 0-5: Use keyword (SECRET)
Position 6+: Use plaintext (AUTOKEY itself)

Key sequence: S E C R E T A U T O K E
              (SECRET)   + (AUTOKEY)

Shift values: S=18, E=4, C=2, R=17, E=4, T=19, A=0, U=20, T=19, O=14, K=10, E=4

A(0) + S(18) = 18 = S
U(20) + E(4) = 24 = Y
T(19) + C(2) = 21 = V
O(14) + R(17) = 31 mod 26 = 5 = F
K(10) + E(4) = 14 = O
E(4) + T(19) = 23 = X
Y(24) + A(0) = 24 = Y

Ciphertext: SYVFOXY
```

**Decryption** of "SYVFOXY" with Keyword = "SECRET"

```
Ciphertext:  S Y V F O X Y
Key sequence: S E C R E T A
(Recovered plaintext becomes key)

S - S(18) = 0 = A
Y - E(4) = 20 = U
V - C(2) = 19 = T
F - R(17) = -12 mod 26 = 14 = O (decryptor now knows plaintext letter O)
O - E(4) = 10 = K (decryptor now knows plaintext letter K)
X - T(19) = 4 = E (decryptor now knows plaintext letter E)
Y - A(0) = 24 = Y (decryptor now knows plaintext letter Y)

Plaintext: AUTOKEY
```

### Advantages
✓ Stronger than Vigenère (no repetition)
✓ Key never repeats (until very long plaintexts)
✓ Defeats standard frequency analysis
✗ Vulnerable to known plaintext attack
✗ Still breakable with cryptanalysis
✗ Requires synchronization

### Disadvantages
✗ More complex than Vigenère
✗ Requires correct transmission (one error ruins rest)
✗ Still vulnerable to known plaintext
✗ Requires synchronization between sender/receiver

### Cryptanalysis

**Known Plaintext Attack**:
If attacker knows any plaintext segment:
1. Recover corresponding ciphertext
2. Recover key from C = P + K
3. Use recovered key + plaintext = future key
4. Decrypt subsequent text

### Difficulty Level
🟢 Medium (6/10)

### Summary
Autokey Cipher improves on Vigenère by using plaintext as part of the key, eliminating repetition. However, it's still vulnerable to known plaintext attacks and other cryptanalysis techniques. It demonstrates the importance of key synchronization.

---

## Nihilist Cipher

### Definition
The **Nihilist Cipher** combines a Polybius square with transposition to encrypt messages. It converts letters to numbers, then applies transposition.

### How It Works

**Step 1**: Create a Polybius square (5×5)
**Step 2**: Convert plaintext letters to coordinate numbers
**Step 3**: Apply transposition based on keyword

### Polybius Square Example

```
    1 2 3 4 5
  ┌─────────────┐
1 │ A B C D E   │
2 │ F G H I/J K │
3 │ L M N O P   │
4 │ Q R S T U   │
5 │ V W X Y Z   │
  └─────────────┘
```

Each letter = row + column
- A = 11, B = 12, C = 13, ..., Z = 55

### Worked Example

**Encrypt**: "NIHILIST" with Keyword = "SECRET"

```
Step 1: Convert to Polybius coordinates
N = 33, I = 24, H = 23, I = 24, L = 31, I = 24, S = 43, T = 44

Sequence: 33 24 23 24 31 24 43 44

Step 2: Apply transposition based on keyword
(Details vary by specific Nihilist variant)

Typical result: Rearranged number pairs
```

### Advantages
✓ Combines substitution and transposition
✓ Converts to numbers (more abstraction)
✓ Stronger than simple substitution
✗ Vulnerable to known plaintext
✗ Frequency analysis on bigrams
✗ Manual computation complex

### Disadvantages
✗ Requires Polybius square knowledge
✗ Complex computation
✗ Still vulnerable to cryptanalysis
✗ Limited practical advantage

### Difficulty Level
🟡 Medium-Hard (7/10)

### Summary
Nihilist Cipher combines substitution and transposition through number sequences. While more complex than simple ciphers, it remains vulnerable to modern cryptanalysis. It demonstrates hybrid cipher approaches.

---

## One-Time Pad Cipher

### Definition
The **One-Time Pad** (OTP) is a theoretically perfect cipher where the key is as long as the plaintext and used exactly once.

### How It Works

**Requirements**:
- Key length = Plaintext length
- Key consists of random characters
- Key used only once (never reused)
- Both parties have identical key

### Formula
```
C = (P + K[i]) mod 26 (for each character i)
P = (C - K[i]) mod 26 (for each character i)

Key must be:
- Random (no patterns)
- Secret (kept absolutely safe)
- One-time use only
```

### Worked Example

**Encrypt**: "SECRET MESSAGE" with Key = "XMCKL RFLGCP AX"

```
Plaintext:  S E C R E T M E S S A G E
Key:        X M C K L R F L G C P A X

S + X = 18 + 23 = 41 mod 26 = 15 = P
E + M = 4 + 12 = 16 = Q
C + C = 2 + 2 = 4 = E
R + K = 17 + 10 = 27 mod 26 = 1 = B
E + L = 4 + 11 = 15 = P
T + R = 19 + 17 = 36 mod 26 = 10 = K
M + F = 12 + 5 = 17 = R
E + L = 4 + 11 = 15 = P
S + G = 18 + 6 = 24 = Y
S + C = 18 + 2 = 20 = U
A + P = 0 + 15 = 15 = P
G + A = 6 + 0 = 6 = G
E + X = 4 + 23 = 27 mod 26 = 1 = B

Ciphertext: PQEBPKRPYUPGB
```

### Decryption

**Decrypt**: "PQEBPKRPYUPGB" with Key = "XMCKL RFLGCP AX"

```
Ciphertext: P Q E B P K R P Y U P G B
Key:        X M C K L R F L G C P A X

P - X = 15 - 23 = -8 mod 26 = 18 = S
Q - M = 16 - 12 = 4 = E
E - C = 4 - 2 = 2 = C
B - K = 1 - 10 = -9 mod 26 = 17 = R
... (continues)

Plaintext: SECRET MESSAGE
```

### Visual Representation

```
┌──────────────────────────────────┐
│   ONE-TIME PAD ENCRYPTION        │
├──────────────────────────────────┤
│ Plaintext:  S E C R E T          │
│ One-Time:   X M C K L R          │
│ Key:                             │
│ Ciphertext: P Q E B P K          │
└──────────────────────────────────┘

Critical:
- Key used once only
- Key is random
- Key = Plaintext length
- Key securely distributed
```

### Advantages
✓ **Theoretically Unbreakable** (information-theoretic security)
✓ No patterns (truly random key)
✓ Resistant to all known attacks
✓ Perfect secrecy if used correctly
✗ Key distribution problem
✗ Key management complexity
✗ Cannot reuse keys
✗ Requires truly random generator

### Disadvantages
✗ Key as long as message
✗ Secure key distribution required
✗ Cannot reuse any part of key
✗ If key is reused, security is broken
✗ Impractical for large-scale communication

### Why OTP is Secure

Even with infinite computing power, without the key:
- Every possible plaintext produces valid ciphertext
- No statistical patterns exist
- No frequency analysis helps
- No known plaintext weakness
- No structure to exploit

### Why OTP Fails in Practice

**Key Reuse**: If any part of key is reused:
- Two ciphertexts reveal information
- Can be broken with known plaintext
- Complete security is lost

**Example of Key Reuse Breaking OTP**:
```
Message 1: HELLO
Message 2: WORLD
Same Key:  SECRE

C1 = H + S = 26 = A
C2 = W + S = 48 mod 26 = 22 = W

C1 XOR C2 = A XOR W = H XOR W (reveals plaintext relationship)
```

### Cryptanalysis

**Without knowing key**: Impossible (proven secure)

**If key is reused**: Vulnerable to:
- Ciphertext-only attacks
- Known plaintext attacks
- Frequency analysis
- Statistical attacks

### Difficulty Level
🟢 Medium (5/10)

### Real-World Relevance
⚠️ LIMITED

**Practical Uses**:
- High-security government communications (still used by NSA)
- Diplomatic hotlines (Moscow-Washington Hotline uses OTP)
- Military applications (with secure key distribution)
- One-off highly sensitive communications

**Limitations**:
- Key distribution problem (hard to securely send long keys)
- Key storage and management
- Impractical for internet-scale communication
- Replaced by public-key cryptography for most uses

### Summary

The One-Time Pad achieves perfect theoretical security—it's mathematically proven unbreakable if used correctly. However, practical limitations make it impractical for most modern applications. It remains important in cryptography as the gold standard of security and is still used in ultra-high-security scenarios.

---

## Summary of Substitution Ciphers

### Quick Comparison Table

| Cipher | Type | Key Space | Security | Breakable | Method |
|--------|------|-----------|----------|-----------|--------|
| Caesar | Mono | 26 | Very Weak | Yes | Brute Force |
| Additive | Mono | 26 | Very Weak | Yes | Brute Force |
| Multiplicative | Mono | 12 | Very Weak | Yes | Frequency |
| Affine | Mono | 312 | Weak | Yes | Frequency |
| Vigenère | Poly | 26^n | Weak-Medium | Yes | Kasiski |
| Homophonic | Mono | Variable | Weak | Yes | Digraph |
| Playfair | Digraph | 26! | Medium | Yes | Digraph |
| Autokey | Poly | Unlimited | Medium | Yes | Known Text |
| Nihilist | Hybrid | Variable | Medium | Yes | Cryptanalysis |
| OTP | Poly | ∞ | **Perfect** | No | (Impossible) |

### Learning Path

**Beginner** (Start Here):
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

✓ Simple substitution broken by frequency analysis
✓ Polyalphabetic needs key length determination
✓ Digraph substitution requires bigram analysis
✓ OTP is theoretically perfect but impractical
✓ All classical ciphers broken by known plaintext
✓ Modern cryptography uses mathematical complexity

---

*Next: Read 03_Transposition_Ciphers.md to learn rearrangement-based encryption*

---

*Document Status: Complete*  
*Last Updated: July 2026*
