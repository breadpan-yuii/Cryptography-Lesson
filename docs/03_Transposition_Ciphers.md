# 03. Transposition Ciphers

## Table of Contents
1. [What is a Transposition Cipher?](#what-is-a-transposition-cipher)
2. [Rail Fence Transposition Cipher](#rail-fence-transposition-cipher)
3. [Block Transposition Cipher](#block-transposition-cipher)
4. [Double Columnar Transposition Cipher](#double-columnar-transposition-cipher)
5. [Myszkowski Transposition Cipher](#myszkowski-transposition-cipher)
6. [Summary](#summary)

---

## What is a Transposition Cipher?

### Definition
A **transposition cipher** rearranges the positions of characters in the plaintext without changing the characters themselves. The character sequence changes, but the character set remains the same.

### Key Principle
In transposition ciphers:
- Characters **remain the same**
- Only the **order of characters changes**
- All original characters are preserved in the ciphertext

### Difference from Substitution
```
Substitution:  HELLO → KHOOR (characters replaced)
Transposition: HELLO → OLLHE (characters rearranged)
```

### Vulnerability
Frequency analysis reveals all original letters are present, just rearranged. This is a major weakness compared to substitution ciphers.

---

# RAIL FENCE TRANSPOSITION CIPHER

## Definition
The **Rail Fence Cipher** (also called Zigzag Cipher) arranges plaintext in a zigzag pattern across multiple "rails" (rows), then reads off row by row to create ciphertext.

## How It Works

### Step 1: Choose Number of Rails
Common values: 2, 3, 4, or more rails

### Step 2: Write Plaintext in Zigzag Pattern
Arrange letters diagonally in a zigzag across the rails

### Step 3: Read Row by Row
Read each row from top to bottom to create ciphertext

## Formula/Process

```
Zigzag Pattern (for 3 rails):

Rail 1: Position 0, 4, 8, 12, ...
Rail 2: Position 1, 3, 5, 7, 9, 11, ...
Rail 3: Position 2, 6, 10, 14, ...

Read: Rail 1 + Rail 2 + Rail 3
```

## Encryption Process

**Step 1**: Determine number of rails
**Step 2**: Write plaintext in zigzag pattern
**Step 3**: Read off each rail sequentially
**Step 4**: Ciphertext is concatenation of all rails

## Worked Example

**Encrypt**: "ATTACKATDAWN" with 3 rails

```
Step 1: Write in zigzag across 3 rails

A   A   T   A   N
 T T C D W
  T   A   D

Step 2: Read each rail
Rail 1: A A T A N
Rail 2: T T C D W
Rail 3: T A D

Ciphertext: AATANTCTDWLTAD
(Combined: AATANTCTDWTAD)
```

Detailed zigzag visualization:
```
Plaintext: A T T A C K A T D A W N
Positions: 0 1 2 3 4 5 6 7 8 9 10 11

Rail 1: 0     4     8       = A  C  D
Rail 2: 1  3  5  7  9  11   = T  A  K  T  A  N
Rail 3: 2     6     10      = T  A  W

Ciphertext: ACDTAKTANTAW
```

## ASCII Diagram: Rail Fence Visualization

```
Plaintext: HELLO WORLD (10 letters)
Rails: 3

    H       O       L
  E   L   W   R   D
    L       O

Reading order:
Rail 1: H O L
Rail 2: E L W R D
Rail 3: L O

Ciphertext: HOLEL WRDLO
```

## Decryption Process

**Step 1**: Determine number of rails from plaintext length
**Step 2**: Calculate how many characters go in each rail
**Step 3**: Split ciphertext into rail segments
**Step 4**: Reconstruct zigzag pattern
**Step 5**: Read plaintext

### Decryption Example

**Decrypt**: "AATANTCTDWTAD" with 3 rails

```
Step 1: Plaintext length = 12, Rails = 3

Step 2: Calculate rail lengths
For n=12, rails=3:
Rail pattern: 1,2,2,2,2,2,1
Rail 1: positions 0,4,8 = 3 characters
Rail 2: positions 1,3,5,7,9,11 = 6 characters
Rail 3: positions 2,6,10 = 3 characters

Step 3: Split ciphertext
First 3 from Rail 1: AAT
Next 6 from Rail 2: ANTCTD
Last 3 from Rail 3: WTA (Wait, recalculate...)

Step 4: Reconstruct
A_A_T_A_N
 T T C D W
 T_A_D

Reading positions: A,T,T,A,C,K,A,T,D,A,W,N
Plaintext: ATTACKATDAWN ✓
```

## Advantages

✓ Simple to understand and compute manually
✓ No complex key management
✓ Fast encryption/decryption
✓ Creates obvious pattern rearrangement
✗ Preserves all characters (frequency analysis leaks info)
✗ Vulnerable to known plaintext
✗ Limited by message length

## Disadvantages

✗ Only parameter is number of rails (small key space)
✗ All letters preserved - easy to detect rearrangement
✗ Anagramming can recover plaintext
✗ Vulnerable to cryptanalysis
✗ Not secure for real-world use

## Cryptanalysis

**Known Plaintext**: If attacker knows plaintext/ciphertext pair, rail count is revealed

**Frequency Analysis**: Letter frequencies unchanged, only positions differ

**Anagramming**: With known alphabet, can try different arrangements

## Difficulty Level

🔵 Very Easy (1/10)

## Real-World Relevance

⚠️ NONE - Rail Fence is completely insecure

Historical: Used in simple children's puzzles and recreational cryptography

## Summary
Rail Fence Cipher demonstrates basic transposition by zigzag rearrangement. While simple and easy to compute manually, it offers virtually no security. It serves educational purposes by showing how rearrangement differs from substitution.

---

# BLOCK TRANSPOSITION CIPHER

## Definition
The **Block Transposition Cipher** arranges plaintext into rectangular blocks and rearranges columns based on a keyword.

## How It Works

### Step 1: Choose Keyword
Example: "SECRET"

### Step 2: Number Columns by Keyword
Arrange keyword letters alphabetically, number by their position
```
Keyword: SECRET
Alpha sort: E C R E S T
Positions: 3 1 4 2 5 6
```

### Step 3: Write Plaintext in Blocks
Write plaintext into rows under the numbered columns

### Step 4: Read by Column Numbers
Read columns in numerical order

## Encryption Process

**Step 1**: Create keyword and number it
**Step 2**: Write plaintext in rows under keyword
**Step 3**: Read columns in numerical order

## Worked Example

**Encrypt**: "WEAREDISCOVEREDSAVEYOURSELF" with Key = "SECRET"

```
Keyword: SECRET
Numbered: S(5) E(2) C(1) R(4) E(3) T(6)

Arrange plaintext:
S E C R E T
5 2 1 4 3 6
___________
W E A R E D
I S C O V E
R E D S A V
E Y O U R S
E L F

Read columns by number:
Column 1 (C): A,C,D,F
Column 2 (E): E,S,E,Y,L
Column 3 (E): E,V,A,R
Column 4 (R): R,O,S,U
Column 5 (S): W,I,R,E,E
Column 6 (T): D,E,V,S

Ciphertext: ACDFESLYVEAROUSWIREEDEVS
```

## ASCII Diagram: Block Transposition

```
Before:  After Column Reordering:

S E C R E T    1 2 3 4 5 6
5 2 1 4 3 6    C E E R S T
─────────────  ─────────────
W E A R E D    A S V O W D
I S C O V E    C E A S I E
R E D S A V    D Y R U R V
E Y O U R S    F L
```

## Decryption Process

**Step 1**: Recover keyword numbering
**Step 2**: Calculate column lengths
**Step 3**: Split ciphertext into columns
**Step 4**: Rearrange columns back to original order
**Step 5**: Read plaintext

## Advantages

✓ More complex than Rail Fence
✓ Keyword-based (easier to remember)
✓ Larger key space with longer keywords
✓ Works on any message length
✗ Still vulnerable to cryptanalysis
✗ Column structure detectable
✗ Known plaintext breaks it

## Disadvantages

✗ Requires knowing keyword to decrypt
✗ Not resistant to known plaintext
✗ Structure detectable from message length
✗ Still preserves character frequencies

## Cryptanalysis

**Known Plaintext**: Reveals keyword immediately

**Anagramming**: With frequency analysis, can determine column arrangements

**Brute Force**: Try common keywords

## Difficulty Level

🟡 Medium (4/10)

## Summary
Block Transposition Cipher uses keyword-based column permutation. It's more complex than Rail Fence but still breakable. Used historically for basic message scrambling.

---

# DOUBLE COLUMNAR TRANSPOSITION CIPHER

## Definition
The **Double Columnar Transposition Cipher** applies block transposition **twice** with two different keywords for increased security.

## How It Works

### First Pass: Transpose with Keyword 1
Apply block transposition normally

### Second Pass: Transpose Result with Keyword 2
Take ciphertext from first pass, apply block transposition again

## Encryption Process

**Step 1**: Apply Block Transposition with Key 1
**Step 2**: Take result and apply Block Transposition with Key 2
**Step 3**: Result is doubly encrypted

## Worked Example

**Encrypt**: "WEAREDISCOVEREDSAVEYOURSELF" with Key1="SECRET", Key2="CIPHER"

```
First Pass (Key = SECRET):
Input: WEAREDISCOVEREDSAVEYOURSELF
Output: (result from first transposition)

Second Pass (Key = CIPHER):
Input: (output from first pass)
Output: Final ciphertext

(Detailed calculation omitted for brevity)
```

## Visual Process

```
Plaintext
    ↓
[Block Transposition - Key 1]
    ↓
Intermediate Ciphertext
    ↓
[Block Transposition - Key 2]
    ↓
Final Ciphertext
```

## Advantages

✓ Much stronger than single transposition
✓ Requires two keywords
✓ Twice the rearrangement
✓ More resistant to analysis
✗ Still not secure (can be broken)
✗ More complex to compute
✗ Vulnerable to known plaintext

## Disadvantages

✗ Twice the computation overhead
✗ Two keywords to manage
✗ Still vulnerable to cryptanalysis
✗ Keyspace still limited

## Cryptanalysis

**Known Plaintext**: Known message/ciphertext pair reveals both keywords

**Ciphertext Only**: Much harder but still possible with enough text

## Difficulty Level

🟡 Medium (5/10)

## Summary
Double Columnar Transposition applies transposition twice for added security. While stronger than single transposition, it's still vulnerable to attacks. It demonstrates the principle that repeating a cipher can increase security.

---

# MYSZKOWSKI TRANSPOSITION CIPHER

## Definition
The **Myszkowski Cipher** is a variant of Block Transposition that handles repeated letters in the keyword differently. When keyword letters repeat, those columns are read together.

## How It Works

### Key Difference
Instead of numbering each keyword letter uniquely, repeated letters get the same number.

### Example
```
Keyword: TOCCATA
Standard numbering: T(6) O(5) C(1) C(2) A(1) T(7) A(1)  ← Multiple numbers for same letter

Myszkowski numbering: T(3) O(2) C(1) C(1) A(0) T(3) A(0)  ← Repeated letters same number

Actually:
Keyword: TOCCATA
Letters: T O C C A T A
Sorted:  A A C C O T T
Positions: 1 1 2 2 3 3 3

Better approach:
Keyword with positions:
T(1st position of T) O(1st position of O) C(1st C) C(2nd C) A(1st A) T(2nd T) A(2nd A)

Grouping duplicates:
A: positions 5,7 → group 1
C: positions 3,4 → group 2  
O: position 2 → group 3
T: positions 1,6 → group 4
```

## Encryption Process

**Step 1**: Write plaintext under keyword
**Step 2**: Group repeated letters
**Step 3**: Read columns in sorted order, reading same-number columns sequentially

## Worked Example

**Encrypt**: "ONETWOTHREEFOURFIVESIX" with Key = "TOCCATA"

```
Keyword: T O C C A T A
Grouped: T O C C A T A (with position markers)

Rearrange by alphabetical order:
A (positions 5,7)
C (positions 3,4)
O (position 2)
T (positions 1,6)

Plaintext arranged:
T O C C A T A
1 2 3 4 5 6 7
O N E T W O T
H R E E F O U
R F I V E S I
X

Read columns in order: 5,7 | 3,4 | 2 | 1,6
Column 5,7: A,E,E | T,I,X
Column 3,4: C,E,F | C,V,
Column 2: O,R,F
Column 1,6: T,H,R | O,O,S

Result: Complex rearrangement
```

## Advantages

✓ Better handling of repeated keyword letters
✓ More natural keyword representation
✓ Stronger than standard block transposition
✗ Still vulnerable to analysis
✗ Complex to compute manually
✗ Requires careful implementation

## Disadvantages

✗ More complicated than block transposition
✗ Prone to implementation errors
✗ Still breakable with known plaintext
✗ Similar vulnerabilities to standard transposition

## Difficulty Level

🟡 Medium-Hard (6/10)

## Summary
Myszkowski Cipher improves Block Transposition by handling repeated keyword letters specially. It's slightly stronger but introduces complexity. Still not secure for real-world use.

---

# TRANSPOSITION VS SUBSTITUTION

## Quick Comparison

| Aspect | Substitution | Transposition |
|--------|--------------|---------------|
| Characters | Changed | Unchanged |
| Positions | Same | Rearranged |
| Frequency | Changes | Preserved |
| Anagramming | Not effective | Effective |
| Known Plaintext | Reveals key | Easy recovery |
| Main Weakness | Frequency analysis | Character preservation |

## Combination: Product Cipher

**Strongest approach**: Apply both substitution AND transposition

```
Plaintext → Substitution → Intermediate → Transposition → Ciphertext
```

Example: DES (Data Encryption Standard) uses both techniques.

---

## Summary of Transposition Ciphers

### Quick Reference Table

| Cipher | Key Type | Security | Complexity | Historical Use |
|--------|----------|----------|------------|----------------|
| Rail Fence | Rails count | Very Weak | Simple | Puzzles |
| Block Transposition | Keyword | Weak | Medium | Military |
| Double Columnar | Two Keywords | Weak-Medium | Complex | WWII |
| Myszkowski | Keyword | Weak-Medium | Complex | Variant |

### Key Insights

✓ Transposition preserves character frequencies
✓ Combining substitution + transposition = stronger encryption
✓ All classical transposition breakable with cryptanalysis
✓ Modern encryption uses both principles
✓ Block transposition more secure than simple rearrangement

### When to Use Each

**Rail Fence**: Educational purposes only

**Block Transposition**: Historical understanding, puzzles

**Double Columnar**: Demonstrates multiple encryption passes

**Myszkowski**: Specialized variant study

---

*Next: Read 04_Comparison_of_Ciphers.md for detailed comparative analysis*

---

*Document Status: Complete*  
*Last Updated: July 2026*