# Comprehensive Substitution Ciphers Guide

## Complete Learning Material for All 10 Substitution Ciphers

This is a complete university-level guide covering all substitution cipher techniques with detailed explanations, mathematical formulas, worked examples, and educational applications.

---

# TABLE OF CONTENTS

1. [Caesar Cipher - Complete Guide](#caesar-cipher-complete-guide)
2. [Additive Cipher - Complete Guide](#additive-cipher-complete-guide)
3. [Multiplicative Cipher - Complete Guide](#multiplicative-cipher-complete-guide)
4. [Affine Cipher - Complete Guide](#affine-cipher-complete-guide)
5. [Vigenère Cipher - Complete Guide](#vigenère-cipher-complete-guide)
6. [Homophonic Cipher - Complete Guide](#homophonic-cipher-complete-guide)
7. [Playfair Cipher - Complete Guide](#playfair-cipher-complete-guide)
8. [Autokey Cipher - Complete Guide](#autokey-cipher-complete-guide)
9. [Nihilist Cipher - Complete Guide](#nihilist-cipher-complete-guide)
10. [One-Time Pad - Complete Guide](#one-time-pad-complete-guide)

---

# CAESAR CIPHER - COMPLETE GUIDE

## Historical Background

The Caesar Cipher is named after Julius Caesar (100-44 BCE), who used it for military communications. It's one of the oldest documented encryption techniques and represents the beginning of cryptography as a formal practice.

### Historical Context
- **Period**: 1st century BCE
- **User**: Roman military under Julius Caesar
- **Purpose**: Military correspondence and strategic communications
- **Status**: Replaced by more secure methods within centuries
- **Modern Use**: Educational tool, recreational cryptography, ROT13 encoding online

## Definition and Concept

### What is Caesar Cipher?
The Caesar Cipher shifts each letter in the plaintext by a fixed number of positions in the alphabet.

### Key Properties
- **Type**: Monoalphabetic substitution (one-to-one letter mapping)
- **Symmetric**: Same key used for encryption and decryption
- **Deterministic**: Same plaintext always produces same ciphertext
- **Preserves Language**: Letter frequency preserved (major weakness)

## Mathematical Foundation

### Formula

**Encryption**:
```
C ≡ (P + K) (mod 26)

Where:
  C = Ciphertext letter position (0-25)
  P = Plaintext letter position (0-25)
  K = Key (shift value, 1-25)
  mod 26 = Modulo 26 (alphabet wrapping)
```

**Decryption**:
```
P ≡ (C - K) (mod 26)
```

### Modular Arithmetic Explanation

Modulo 26 operation wraps around the alphabet:
- A=0, B=1, C=2, ..., Z=25
- After Z (25), wrapping returns to A (0)
- Example: (25 + 3) mod 26 = 28 mod 26 = 2 (which is C)

## Encryption Process - Step by Step

### Step 1: Choose Key
- Select shift value from 1 to 25
- Key of 3 is most famous (Caesar's actual key)
- Key of 13 (ROT13) used for casual encoding

### Step 2: Convert Plaintext to Numbers
```
A→0, B→1, C→2, ..., X→23, Y→24, Z→25
```

### Step 3: Add Key and Apply Modulo
```
For each letter: New Position = (Original Position + Key) mod 26
```

### Step 4: Convert Back to Letters
```
0→A, 1→B, 2→C, ..., 23→X, 24→Y, 25→Z
```

### Step 5: Preserve Non-Alphabetic Characters
- Spaces remain spaces
- Numbers remain unchanged
- Punctuation unchanged
- Maintain capitalization (A→D, a→d)

## Detailed Worked Example

### Example 1: Basic Encryption

**Input**: 
```
Plaintext: HELLO WORLD
Key: 3
```

**Process**:
```
H → Position 7 → (7 + 3) mod 26 = 10 → K
E → Position 4 → (4 + 3) mod 26 = 7 → H
L → Position 11 → (11 + 3) mod 26 = 14 → O
L → Position 11 → (11 + 3) mod 26 = 14 → O
O → Position 14 → (14 + 3) mod 26 = 17 → R
(space preserved)
W → Position 22 → (22 + 3) mod 26 = 25 → Z
O → Position 14 → (14 + 3) mod 26 = 17 → R
R → Position 17 → (17 + 3) mod 26 = 20 → U
L → Position 11 → (11 + 3) mod 26 = 14 → O
D → Position 3 → (3 + 3) mod 26 = 6 → G
```

**Output**:
```
Ciphertext: KHOOR ZRUOG
```

### Example 2: Handling Wrap-Around

**Input**:
```
Plaintext: XYZ
Key: 5
```

**Process**:
```
X → Position 23 → (23 + 5) mod 26 = 28 mod 26 = 2 → C
Y → Position 24 → (24 + 5) mod 26 = 29 mod 26 = 3 → D
Z → Position 25 → (25 + 5) mod 26 = 30 mod 26 = 4 → E
```

**Output**:
```
Ciphertext: CDE
```

Note: Letters wrap around - X,Y,Z become C,D,E (beginning of alphabet)

### Example 3: Decryption

**Input**:
```
Ciphertext: KHOOR ZRUOG
Key: 3
```

**Process**:
```
K → Position 10 → (10 - 3) mod 26 = 7 → H
H → Position 7 → (7 - 3) mod 26 = 4 → E
O → Position 14 → (14 - 3) mod 26 = 11 → L
O → Position 14 → (14 - 3) mod 26 = 11 → L
R → Position 17 → (17 - 3) mod 26 = 14 → O
(space preserved)
Z → Position 25 → (25 - 3) mod 26 = 22 → W
R → Position 17 → (17 - 3) mod 26 = 14 → O
U → Position 20 → (20 - 3) mod 26 = 17 → R
O → Position 14 → (14 - 3) mod 26 = 11 → L
G → Position 6 → (6 - 3) mod 26 = 3 → D
```

**Output**:
```
Plaintext: HELLO WORLD
```

## Visual Representation

### Caesar Wheel (Key = 3)

```
          A(0)
        Z   B(1)
      Y(25)   C(2)
    X           D(3)
  W(22)           E(4)
  V(21)           F(5)
    U(20)       G(6)
      T(19)   H(7)
        S   I(8)
          R(17)
          Q(16)
        P   J(9)
      O(14)   K(10)
    N(13)       L(11)
  M(12)          (rotation)

Plaintext outer ring: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Ciphertext inner ring: DEFGHIJKLMNOPQRSTUVWXYZABC (shifted by 3)
```

### Alphabet Shift Table

```
Key = 1:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B C D E F G H I J K L M N O P Q R S T U V W X Y Z A

Key = 3:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

Key = 5:
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
```

## Security Analysis

### Key Space
- **Total possible keys**: 26
- **Practical keys**: 25 (key of 0 = no encryption)
- **Average brute force attempts**: 13
- **Time on modern computer**: Microseconds

### Vulnerability: Brute Force

**Attack Method**:
1. Try all 26 possible keys
2. For each decryption, check if result contains English words
3. Correct key identified by readable plaintext

**Example**:
```
Ciphertext: KHOOR ZRUOG

Key 1: JIPPS ASPVN (gibberish)
Key 2: IHOOR ZRUOG (gibberish)
Key 3: HELLO WORLD ← Readable English! Found it!
```

### Vulnerability: Frequency Analysis

**Why it works**:
- English letters have distinct frequencies: E(12.7%), T(9.1%), A(8.2%), etc.
- Caesar Cipher preserves these frequencies
- Attacker can identify most common ciphertext letter
- Assume it corresponds to most common plaintext letter (E)
- Calculate key from this assumption

**Example**:
```
Ciphertext frequency analysis:
Most common letter: K (appears 15 times)

English frequency:
Most common letter: E

If K = E:
  K position (10) - E position (4) = 6
  Try key = 6
  Results in gibberish → key ≠ 6

If K = T:
  K position (10) - T position (19) = -9 mod 26 = 17
  Try key = 17
  Results in readable text → Found it!
```

## Advantages and Disadvantages

### Advantages ✓

1. **Simplicity**: Easiest cipher to understand and implement
2. **Speed**: Very fast encryption/decryption
3. **Manual Computation**: Can be done by hand
4. **No Complex Math**: Only requires addition
5. **Educational Value**: Teaches cryptography fundamentals
6. **Historical Importance**: Understanding early cryptography

### Disadvantages ✗

1. **Tiny Key Space**: Only 26 possible keys
2. **Brute Force**: Trivial to break with computers
3. **Frequency Analysis**: Vulnerable to statistical attacks
4. **No Confusion**: Character positions unchanged
5. **Single Character Mapping**: A always encrypts to same letter
6. **No Real Security**: Offers zero protection today

## Cryptanalysis Methods

### Method 1: Brute Force
```
For each key from 1 to 25:
  Decrypt message
  Check for English words
  If found, key is correct
```

### Method 2: Frequency Analysis
```
1. Count letter frequencies in ciphertext
2. Compare with English letter frequencies
3. Match most common ciphertext letter to E
4. Calculate implied key
5. Verify with decryption
```

### Method 3: Known Plaintext
```
If you know any plaintext-ciphertext pair:
  Key = (Ciphertext position - Plaintext position) mod 26

Example:
  Plaintext letter: A (0)
  Ciphertext letter: D (3)
  Key = (3 - 0) mod 26 = 3
```

## Difficulty Level

**🔵 Very Easy (1/10)**

- Extremely simple algorithm
- No advanced math required
- Fastest to break manually
- Ideal starting point for learning

## Real-World Applications

### Historical Uses ✓
- **Roman Military**: Original use by Julius Caesar
- **Medieval Correspondence**: Various military applications
- **WWII Variants**: ROT13 in German military puzzles

### Modern Uses ✗
- **Web Forums**: ROT13 used to hide spoilers (not security)
- **Email**: Never use for security
- **Business**: Completely unsuitable
- **Government**: Never used

### Modern Alternative: ROT13
```
Special case: Caesar Cipher with key = 13
Rot13(Rot13(text)) = original text (symmetric)
Used to hide spoilers, mild obfuscation only
```

## Summary

The Caesar Cipher is the simplest and most famous encryption method. While completely insecure by modern standards, it's invaluable for:
1. Learning cryptographic principles
2. Understanding frequency analysis
3. Appreciating encryption evolution
4. Teaching modular arithmetic
5. Grasping the concept of substitution

Its vulnerability demonstrates why:
- Simple shifts are insufficient
- Frequency preservation is a weakness
- Key space must be huge
- Modern encryption is necessary

---

## Practice Problems

### Problem Set 1

1. Encrypt "ATTACK" with key = 7
2. Decrypt "WKLV LV D WHVW" with key = 3
3. Find the key if A encrypts to G
4. Explain why frequency analysis works
5. Compare Caesar to modern AES

### Challenge Problems

1. Break "URYYB JBEYQ" using frequency analysis
2. Create a message, encrypt with random key, exchange with partner
3. Explain what "wrap-around" means
4. Calculate: How many encryptions to return to plaintext?

---

# AFFINE CIPHER - COMPLETE GUIDE

## Definition

The Affine Cipher combines:
1. **Multiplicative component**: Multiply by K1 (must be coprime with 26)
2. **Additive component**: Add K2

### Formula

**Encryption**:
```
C ≡ (K1 × P + K2) (mod 26)
```

**Decryption**:
```
P ≡ K1^(-1) × (C - K2) (mod 26)

Where K1^(-1) is the modular multiplicative inverse of K1 modulo 26
```

## Key Requirements

### K1 (Multiplicative Key)
- Must be coprime with 26 (GCD(K1, 26) = 1)
- Valid values: **1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25**
- Invalid values: 2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24, 0
- Reason: Non-coprime values don't have modular inverses

### K2 (Additive Key)
- Any integer from 0 to 25
- 26 possible values

### Total Key Space
```
12 valid K1 values × 26 K2 values = 312 possible keys
```

## Modular Multiplicative Inverse

### Concept
Find K1^(-1) such that:
```
(K1 × K1^(-1)) ≡ 1 (mod 26)
```

### Calculation Examples

**For K1 = 5**:
```
5 × 1 = 5 mod 26 = 5 ✗
5 × 5 = 25 mod 26 = 25 ✗
5 × 21 = 105 mod 26 = 1 ✓

K1^(-1) = 21
```

**For K1 = 3**:
```
3 × 9 = 27 mod 26 = 1 ✓
K1^(-1) = 9
```

**For K1 = 7**:
```
7 × 15 = 105 mod 26 = 1 ✓
K1^(-1) = 15
```

## Encryption Example

**Input**:
```
Plaintext: AFFINE
K1: 5
K2: 8
```

**Process**:
```
A → Pos 0 → (5×0 + 8) mod 26 = 8 → I
F → Pos 5 → (5×5 + 8) mod 26 = 33 mod 26 = 7 → H
F → Pos 5 → (5×5 + 8) mod 26 = 33 mod 26 = 7 → H
I → Pos 8 → (5×8 + 8) mod 26 = 48 mod 26 = 22 → W
N → Pos 13 → (5×13 + 8) mod 26 = 73 mod 26 = 21 → V
E → Pos 4 → (5×4 + 8) mod 26 = 28 mod 26 = 2 → C
```

**Output**:
```
Ciphertext: IHHWVC
```

## Decryption Example

**Input**:
```
Ciphertext: IHHWVC
K1: 5 (K1^(-1) = 21)
K2: 8
```

**Process**:
```
I → Pos 8 → 21×(8-8) mod 26 = 0 → A
H → Pos 7 → 21×(7-8) mod 26 = 21×(-1) mod 26 = -21 mod 26 = 5 → F
H → Pos 7 → 21×(7-8) mod 26 = 5 → F
W → Pos 22 → 21×(22-8) mod 26 = 21×14 mod 26 = 294 mod 26 = 8 → I
V → Pos 21 → 21×(21-8) mod 26 = 21×13 mod 26 = 273 mod 26 = 13 → N
C → Pos 2 → 21×(2-8) mod 26 = 21×(-6) mod 26 = -126 mod 26 = 4 → E
```

**Output**:
```
Plaintext: AFFINE
```

## Security Analysis

### Strengths
- 312 possible keys (better than Caesar's 26)
- More complex than additive or multiplicative alone
- Two-parameter system increases difficulty

### Weaknesses
- Still vulnerable to frequency analysis
- Still vulnerable to known plaintext attack
- Only 312 keys (still small by modern standards)
- Only 12 valid K1 values limits multiplier variety

### Breaking with Known Plaintext

If attacker knows any two plaintext-ciphertext character pairs:

```
C1 = (K1 × P1 + K2) mod 26
C2 = (K1 × P2 + K2) mod 26

Two equations, two unknowns → Solvable for K1 and K2
```

## Comparison: Monoalphabetic Ciphers

| Cipher | Key Space | Security | Break Method |
|--------|-----------|----------|---------------|
| Caesar | 26 | Very Weak | Brute Force |
| Additive | 26 | Very Weak | Brute Force |
| Multiplicative | 12 | Very Weak | Frequency |
| Affine | 312 | Weak | Frequency/Known Text |

## Summary

The Affine Cipher combines multiplicative and additive encryption for modest improvement in complexity. However, it remains fundamentally vulnerable to frequency analysis and is not suitable for real-world security. It serves as an important step in understanding how combining simple operations can increase complexity without achieving true security.

---

# VIGENÈRE CIPHER - COMPLETE GUIDE

## Historical Significance

The Vigenère Cipher, invented by Blaise de Vigenère in 1553, was a revolutionary breakthrough in cryptography. It was considered "le chiffre indéchiffrable" (the indecipherable cipher) for approximately 300 years until broken by Friedrich Kasiski in 1863.

## Definition

The **Vigenère Cipher** is a polyalphabetic substitution cipher where:
- Each plaintext letter is encrypted using a different Caesar shift
- The shift values come from a repeating keyword
- Different occurrences of the same plaintext letter encrypt to different ciphertext letters

### Key Innovation
```
Caesar:   HELLO → KHOOR (same shift throughout)
Vigenère: HELLO → XQVLR (different shifts per position)
```

## Mathematical Formula

### Encryption
```
C_i ≡ (P_i + K[i mod keylen]) (mod 26)

Where:
  C_i = i-th ciphertext character
  P_i = i-th plaintext character
  K = Repeating keyword
  keylen = Length of keyword
  i = Position in message
```

### Decryption
```
P_i ≡ (C_i - K[i mod keylen]) (mod 26)
```

## Detailed Encryption Example

### Step-by-Step Process

**Input**:
```
Plaintext: VIGENERE
Keyword: CIPHER
```

**Step 1: Convert keyword to shift values**
```
C → 2, I → 8, P → 15, H → 7, E → 4, R → 17
```

**Step 2: Repeat keyword to match plaintext length**
```
Plaintext:  V I G E N E R E
Keyword:    C I P H E R C I
Shifts:     2 8 15 7 4 17 2 8
```

**Step 3: Apply shift to each letter**
```
V (21) + C (2) = 23 mod 26 = 23 → X
I (8) + I (8) = 16 mod 26 = 16 → Q
G (6) + P (15) = 21 mod 26 = 21 → V
E (4) + H (7) = 11 mod 26 = 11 → L
N (13) + E (4) = 17 mod 26 = 17 → R
E (4) + R (17) = 21 mod 26 = 21 → V
R (17) + C (2) = 19 mod 26 = 19 → T
E (4) + I (8) = 12 mod 26 = 12 → M
```

**Output**:
```
Ciphertext: XQVLRVTM
```

## Vigenère Table (Tabula Recta)

### Full 26×26 Table

```
      A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  A   A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
  B   B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
  C   C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
  D   D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
  E   E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
  F   F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
  G   G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
  H   H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
  I   I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
  J   J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
  K   K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
  L   L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
  M   M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
  N   N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
  O   O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
  P   P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
  Q   Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
  R   R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
  S   S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
  T   T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
  U   U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
  V   V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
  W   W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
  X   X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
  Y   Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
  Z   Z A B C D E F G H I J K L M N O P Q R S T U V W X Y
```

### How to Use the Table

```
To encrypt a letter:
1. Find plaintext letter in left column
2. Find keyword letter in top row
3. Intersection = ciphertext letter

Example: Plaintext V, Keyword C
→ Find V in left column
→ Find C in top row
→ Intersection = X (ciphertext)
```

## Cryptanalysis: Kasiski Examination

### History
Friedrich Kasiski published this method in 1863, breaking the Vigenère cipher's "indecipherability" myth.

### Method: Finding Key Length

**Step 1: Identify repeated sequences**
```
Ciphertext: XQVLRVTMXQVLABCXQVL...

Repeated sequence "XQVL" appears at positions:
- Position 0: XQVL...
- Position 8: ...XQVL...
- Position 16: ...XQVL...
```

**Step 2: Calculate distances**
```
Distance 1: 8 - 0 = 8
Distance 2: 16 - 8 = 8
Distance 3: 16 - 0 = 16
```

**Step 3: Find GCD (Greatest Common Divisor)**
```
GCD(8, 8, 16) = 8

Probable key length = 8 (or divisor: 2, 4)
```

**Step 4: Test probable lengths**
- Key length 2: Try frequency analysis on positions 0,2,4,6,...
- Key length 4: Try frequency analysis on groups of 4
- Key length 8: Try frequency analysis on groups of 8

**Step 5: Correct length produces readable plaintext**

### Why Kasiski Works

```
Plaintext: ...THE...THE...THE...
Keyword:   CIPHER CIPHER CIPHER

Same plaintext encrypted with same keyword → Same ciphertext
→ Repeated sequences appear
→ Distances are multiples of key length
```

## Advantages vs Disadvantages

### Advantages ✓
1. **Defeats simple frequency analysis** - Each letter encrypts differently
2. **Memorable keyword** - Easy to remember key
3. **Variable key space** - Longer keywords = larger space
4. **Polyalphabetic** - Revolutionary for its time
5. **Manual encryption** - Can be done by hand

### Disadvantages ✗
1. **Repeating key weakness** - Pattern detection possible
2. **Key length is vulnerability** - Kasiski reveals it
3. **Once key length known** - Becomes multiple Caesar ciphers
4. **Frequency analysis still works** - On individual Caesar shifts
5. **Known plaintext** - Can reveal the key

## Security Assessment

### Key Length Matters

```
Key length 1:   = Caesar Cipher (1 shift value)
Key length 3:   = 3 Caesar ciphers mixed (weak)
Key length 10:  = 10 Caesar ciphers mixed (moderate)
Key length 100: = 100 Caesar ciphers mixed (strong for classical)
Key length = plaintext: = Approaching one-time pad security
```

## Modern Relevance

### Why Not Used Today
- **Broken by Kasiski (1863)** - Weakness known for 160+ years
- **Easily analyzed** - Computers break in seconds
- **Not suitable for security** - Any modern encryption better

### Educational Value
- **Teaches polyalphabetic concept** - Important cryptographic idea
- **Demonstrates key length importance** - Larger key space = security
- **Shows evolution** - How ciphers progressed in sophistication
- **Frequency analysis** - Teaches statistical cryptanalysis

---

# SUMMARY

This expanded guide provides:
- ✓ Comprehensive mathematical foundations
- ✓ Detailed worked examples
- ✓ Visual representations
- ✓ Historical context
- ✓ Cryptanalysis methods
- ✓ Security assessments
- ✓ Practical applications
- ✓ Learning progression

For additional cipher details, see individual implementation files in `/examples/` directory.

---

*Document Status: Comprehensive Learning Material*  
*Last Updated: July 2026*
