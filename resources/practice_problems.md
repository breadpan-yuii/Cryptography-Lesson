# Practice Problems: Substitution Ciphers

## Caesar Cipher Practice Problems

### Practice Problems (3)

#### Problem 1.1
**Encrypt** the plaintext "DEFEND THE FORTRESS" using Caesar Cipher with key = 5

**Your Work**:
```
Plaintext:  D E F E N D T H E F O R T R E S S
Shift +5:   
Ciphertext: 
```

**Challenge**: Verify by decrypting your ciphertext with key = 5

---

#### Problem 1.2
**Decrypt** the ciphertext "WKPHVDUP EHQGV WLPH ZHOO" which was encrypted with Caesar Cipher key = 3

**Hint**: Try the reverse shift (key = -3)

**Your Work**:
```
Ciphertext: W K H P V U A P B H Q I V W L P G H
Shift -3:   
Plaintext:  
```

---

#### Problem 1.3
**Break** the following ciphertext using brute force (try all 26 keys):
```
MBTWFRLJ SFMRFYJK IXLNQ SFJ WQJIJ
```

**Hint**: Look for common English words (THE, AND, IS, etc.)

---

### Challenge Problems (3)

#### Challenge 1.1
**Analyze Frequency**: The ciphertext below was encrypted with Caesar Cipher. 
1. Count letter frequencies
2. Determine most common letter
3. Assume it's E (most common in English)
4. Calculate the key
5. Decrypt the message

```
KRFQ'V DXL IXVNJ VJDVJUV VYRFBV CURFZ KFDXDVK
```

**Questions**:
- What is the most frequent letter in the ciphertext?
- If that letter is E, what is the key?
- What is the plaintext message?

---

#### Challenge 1.2
**Create a Code**: 
- Choose a plaintext message (at least 20 characters)
- Choose a random key (5-25)
- Encrypt using Caesar Cipher
- Exchange with a partner
- Break partner's code using frequency analysis or brute force

**Evaluation Criteria**:
- Message is at least 20 characters
- Encryption is correct
- Can correctly break the code

---

#### Challenge 1.3
**Statistical Analysis**:
Given this encrypted text:
```
VJGH KU YKNNGD YKVJ ECFGU
```

1. Try different keys systematically
2. For each key, check if the result contains English words
3. Find the key that produces valid English
4. Explain why frequency analysis helps with longer texts

---

## Vigenère Cipher Practice Problems

### Practice Problems (3)

#### Problem 2.1
**Encrypt** "ATTACKATDAWN" using Vigenère Cipher with keyword "CIPHER"

**Step-by-step**:
```
Plaintext:  A T T A C K A T D A W N
Keyword:    C I P H E R C I P H E R
Key Values: 2 8 15 7 4 17 2 8 15 7 4 17

Calculate: (Plaintext + Key) mod 26
A + C = (0 + 2) mod 26 = 2 = C
T + I = (19 + 8) mod 26 = 27 mod 26 = 1 = B
...
Ciphertext: 
```

---

#### Problem 2.2
**Decrypt** the ciphertext "XQVLRVTM" which was encrypted with Vigenère using keyword "CIPHER"

**Step-by-step**:
```
Ciphertext: X Q V L R V T M
Keyword:    C I P H E R C I
Key Values: 2 8 15 7 4 17 2 8

Calculate: (Ciphertext - Key) mod 26
X - C = (23 - 2) mod 26 = 21 = V
Q - I = (16 - 8) mod 26 = 8 = I
...
Plaintext: 
```

---

#### Problem 2.3
**Find Repeated Sequences**: 
Given this Vigenère ciphertext:
```
BVYYQECXGLEACZHJKBVYYQPIVNIFMPL
```

1. Identify repeated sequences
2. Calculate distances between them
3. Find GCD of distances (Kasiski Examination)
4. This gives probable key length

**Your Work**:
```
Repeated Sequence 1: 
Distance: 
Repeated Sequence 2: 
Distance: 
GCD: 
Probable Key Length: 
```

---

### Challenge Problems (3)

#### Challenge 2.1
**Kasiski Examination**:
Given the ciphertext:
```
ALHXYPKALHGJSFGPALHNQVMLP
```

1. Find all repeated sequences of 3+ letters
2. Calculate distances
3. Find GCD
4. Determine probable key length
5. For each probable key length, test if standard frequency analysis reveals English

**Hint**: Look for 3-letter sequences like "ALH"

---

#### Challenge 2.2
**Break with Partial Key Knowledge**:
You know:
- Cipher is Vigenère
- Plaintext starts with "THEQUICKBROWNFOX"
- Ciphertext: "VPNQJUQOZKJFVFG..." (continue with your own)

Use this known plaintext to find the keyword.

**Method**:
```
Plaintext:  T H E Q U I C K B R O W N F O X
Ciphertext: V P N Q J U Q O Z K J F V G T ? (partial)

Key = (Ciphertext - Plaintext) mod 26
V - T = (21 - 19) mod 26 = 2 = C
P - H = (15 - 7) mod 26 = 8 = I
...
Keyword: 
```

---

#### Challenge 2.3
**Create Secure Message**:
1. Write a 50+ character plaintext message
2. Choose a long keyword (8+ letters)
3. Encrypt using Vigenère
4. Share only the ciphertext and cipher type
5. Challenge someone to break it
6. Explain why longer keys make cryptanalysis harder

---

## Playfair Cipher Practice Problems

### Practice Problems (3)

#### Problem 3.1
**Create Playfair Matrix**:
Create a 5×5 Playfair matrix using keyword "CRYPTOGRAPHY"

**Steps**:
1. Remove duplicates: CRYPOGAH
2. Add remaining letters (skip J)
3. Arrange in 5×5 grid

**Your Grid**:
```
     1 2 3 4 5
  ┌─────────────────┐
1 │ ? ? ? ? ?       │
2 │ ? ? ? ? ?       │
3 │ ? ? ? ? ?       │
4 │ ? ? ? ? ?       │
5 │ ? ? ? ? ?       │
  └─────────────────┘
```

---

#### Problem 3.2
**Encrypt Digraphs**:
Using matrix from Problem 3.1, encrypt "HELLO" with Playfair

**Prepare plaintext**:
- HELLO → HE LX LO (pair letters, insert X for doubles, add X if odd)

**Encrypt each pair**:
- HE: Find H and E in matrix, apply rule → ??
- LX: Find L and X in matrix, apply rule → ??
- LO: Find L and O in matrix, apply rule → ??

**Rules**:
- Same row: shift right
- Same column: shift down
- Rectangle: swap corners

---

#### Problem 3.3
**Decrypt Playfair**:
Using the same matrix, decrypt "KHUL" encrypted with Playfair "CRYPTOGRAPHY"

**Process**:
- Take pairs: KH, UL
- Apply REVERSE rules (left, up, swap corners)
- Result: ??

---

### Challenge Problems (3)

#### Challenge 3.1
**Break Playfair with Known Plaintext**:
You intercept:
- Ciphertext: "IIHCXPXFX"
- You know plaintext starts with "SECRETM..."

1. Use known plaintext to find some matrix positions
2. Attempt to reconstruct keyword
3. Decrypt entire message

---

#### Challenge 3.2
**Analyze Digraph Frequency**:
Break the following Playfair ciphertext using digraph frequency analysis:
```
GTHGPCOLYEFORHXSNMPCOLYEFXXYL
```

1. Find most common digraphs in ciphertext
2. Assume they correspond to common English digraphs (TH, HE, IN, etc.)
3. Use matrix structure to constrain possibilities
4. Test combinations

---

#### Challenge 3.3
**Create Secure Message**:
1. Write 50-character message
2. Choose unique keyword (12+ letters)
3. Create matrix and encrypt
4. Challenge classmates to break it
5. Award points for speed/method

---

## Affine Cipher Practice Problems

### Practice Problems (3)

#### Problem 4.1
**Encrypt with Affine**:
Encrypt "CRYPTOGRAPHY" with K1=5, K2=8

**Formula**: C = (K1 × P + K2) mod 26

**Your Work**:
```
Plaintext:  C  R  Y  P  T  O  G  R  A  P  H  Y
Positions:  2  17 24 15 19 14 6  17 0  15 7  24

C = (5 × pos + 8) mod 26:
5 × 2 + 8 = 18 mod 26 = 18 = S
5 × 17 + 8 = 93 mod 26 = 15 = P
...
Ciphertext: 
```

---

#### Problem 4.2
**Find Multiplicative Inverse**:
Find K1^-1 for K1 = 5 (mod 26)

**Method**: Find number that satisfies (5 × K1^-1) mod 26 = 1

**Test values**:
- 5 × 1 = 5 mod 26 ≠ 1
- 5 × 5 = 25 mod 26 ≠ 1
- 5 × 21 = 105 mod 26 = 1 ✓

**K1^-1 = 21**

Now find K1^-1 for these values:
- K1 = 3: K1^-1 = ?
- K1 = 7: K1^-1 = ?
- K1 = 9: K1^-1 = ?

---

#### Problem 4.3
**Decrypt Affine**:
Decrypt "SPYQZNRSPUGRG" with K1=5, K2=8

**Formula**: P = (K1^-1 × (C - K2)) mod 26

**Using K1^-1 = 21** (from above):
```
Ciphertext: S  P  Y  Q  Z  N  R  S  P  U  G  R  G
Positions:  18 15 24 16 25 13 17 18 15 20 6  17 6

P = (21 × (pos - 8)) mod 26:
21 × (18 - 8) = 21 × 10 = 210 mod 26 = 2 = C
...
Plaintext: 
```

---

### Challenge Problems (3)

#### Challenge 4.1
**Find Valid Keys**:
List all valid (K1, K2) pairs where:
- K1 is coprime with 26
- K2 is between 0-5

**Valid K1 values**: 1,3,5,7,9,11,15,17,19,21,23,25

**Your List**:
```
(1,0), (1,1), (1,2), (1,3), (1,4), (1,5),
(3,0), (3,1), ...

Total: ? pairs
```

---

#### Challenge 4.2
**Break with Frequency Analysis**:
Given ciphertext:
```
ULYYH DYEUP PULY
```

1. Assume most frequent ciphertext letter = E
2. Identify a second letter (assume = T)
3. Set up two equations with two unknowns (K1, K2)
4. Solve for K1 and K2
5. Decrypt

**Frequency**:
- U appears 2 times (assume = E)
- Y appears 3 times (assume = T)

**Equations**:
- E (4): (K1 × 4 + K2) mod 26 = U (20)
- T (19): (K1 × 19 + K2) mod 26 = Y (24)

**Solve**: K1 = ?, K2 = ?

---

#### Challenge 4.3
**Compare Security**:
Which is more secure against frequency analysis?
- Caesar Cipher (Key space: 26)
- Affine Cipher (Key space: 312)

Why? Explain the security difference.

---

## One-Time Pad Practice Problems

### Practice Problems (3)

#### Problem 5.1
**Encrypt with OTP**:
Encrypt "SECRET" with random OTP key "XMCKLY"

**Formula**: C = (P + K) mod 26

```
Plaintext: S E C R E T
Key:       X M C K L Y

S + X = 18 + 23 = 41 mod 26 = 15 = P
E + M = 4 + 12 = 16 mod 26 = 16 = Q
C + C = 2 + 2 = 4 mod 26 = 4 = E
R + K = 17 + 10 = 27 mod 26 = 1 = B
E + L = 4 + 11 = 15 mod 26 = 15 = P
T + Y = 19 + 24 = 43 mod 26 = 17 = R

Ciphertext: PQEBPR
```

Now decrypt PQEBPR with same key to verify

---

#### Problem 5.2
**The Key Reuse Problem**:
Two messages encrypted with OTP using same key:

```
Message 1 ciphertext: PQEBC
Message 2 ciphertext: RSDOP
```

Demonstrate why this is a problem:

```
C1 ⊕ C2 = P1 ⊕ P2 (XOR operation)

Even though individual messages are secure,
XORing them together reveals the plaintext relationship.
```

---

#### Problem 5.3
**Verify Perfect Secrecy**:
Given ciphertext "PQEBPR"

Show that WITHOUT the key, you cannot determine if plaintext is:
- "SECRET" or
- "ATTACK" or  
- any other 6-letter word

**Why**: Every plaintext maps to this ciphertext for some key

---

### Challenge Problems (3)

#### Challenge 5.1
**Key Distribution Problem**:
You need to send a 1000-character message securely using OTP.

**Challenge Questions**:
1. How large must the key be?
2. How do you securely send this key to recipient?
3. What happens if you use the same key twice?
4. Why is OTP impractical for everyday communication?

**Your Analysis**: (write 100-200 words)

---

#### Challenge 5.2
**Historical Context**:
Research the Moscow-Washington Hotline ("Red Phone").

**Questions**:
1. When was it established?
2. What encryption was used?
3. Why OTP for government communications?
4. What key management procedures were needed?

---

#### Challenge 5.3
**Compare All Ciphers**:
Create comparison table:

| Property | Caesar | Affine | Vigenère | OTP |
|----------|--------|--------|----------|-----|
| Key Space | 26 | 312 | 26^n | ∞ |
| Security | Very Weak | Weak | Medium | Perfect |
| Practical | Yes | Yes | Yes | No |
| Real Use | No | No | No | Yes |

**Analysis**: Why do we use complex modern encryption (AES) instead of OTP?

---

## Answer Key

### Caesar Cipher Answers

**1.1**: IJGITM YMJ GSVYJIVYJ

**1.2**: THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG

**1.3**: Key = 7 → FREQUENCY ANALYSIS WORKS WELL FOR OLD

### Vigenère Cipher Answers

**2.1**: CIBZWIRH (detailed in practice)

**2.2**: VIGENERE

**2.3**: Key length ≈ 8 (based on GCD analysis)

---

*Last Updated: July 2026*
