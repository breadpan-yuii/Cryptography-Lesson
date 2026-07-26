# 05. Applications of Cryptography

## Modern Cryptographic Applications

### 1. Internet & Web Security

**HTTPS/SSL-TLS**
- Secures all website connections
- Uses AES for encryption
- RSA for key exchange
- Certificates verify website identity

**Email Encryption**
- PGP/GPG (Pretty Good Privacy)
- End-to-end encryption
- Digital signatures for authentication

### 2. Financial Systems

**Banking Transactions**
- AES-256 encryption
- Digital signatures verify transactions
- Multi-factor authentication

**Payment Cards**
- PCI-DSS compliance requires encryption
- EMV chip technology
- Tokenization for card data

**Cryptocurrency**
- Bitcoin: SHA-256 hashing
- Blockchain: Cryptographic links
- Private key security critical

### 3. Authentication & Access Control

**Password Systems**
- Passwords hashed (not encrypted)
- Salted hashes prevent rainbow tables
- Bcrypt, Argon2 for strength

**Two-Factor Authentication**
- Time-based codes (TOTP)
- Hardware tokens
- Biometric + cryptography

### 4. Data Protection

**File Encryption**
- BitLocker (Windows)
- FileVault (Mac)
- VeraCrypt (cross-platform)

**Database Encryption**
- Encryption at rest
- Encryption in transit
- Field-level encryption

### 5. Military & Government

**Classified Communications**
- One-Time Pad for ultra-sensitive
- Military-grade encryption
- Air-gapped networks

**Digital Signatures**
- Documents authentication
- Legal validity

### 6. IoT & Smart Devices

**Device Communication**
- Secure pairing protocols
- Message authentication codes
- Certificate-based authentication

**Smart Home**
- Encrypted WiFi (WPA3)
- Secure device registration
- Encrypted remote access

### 7. Messaging Applications

**End-to-End Encryption**
- WhatsApp, Signal, Telegram
- Only sender/receiver can read
- Forward secrecy

**Message Authentication**
- Detect tampering
- Verify sender identity

---

## Classical Cryptography in Modern Context

### Why Study Classical Ciphers?

1. **Educational Foundation**: Understand core principles
2. **Cryptanalysis Skills**: Learn how to break codes
3. **Historical Understanding**: Appreciate evolution
4. **Design Principles**: Know what makes crypto secure
5. **Security Awareness**: Recognize weak implementations

### Classical Cipher Weaknesses Applied to Modern Security

**Caesar Cipher Problem**: Limited key space
**Modern Solution**: Use large key spaces (256-bit keys)

**Vigenère Problem**: Key repetition vulnerable
**Modern Solution**: Generate unique keys per message

**Transposition Problem**: Character frequency preserved
**Modern Solution**: Use multiple encryption layers

**One-Time Pad Challenge**: Key distribution
**Modern Solution**: Public-key cryptography for key exchange

---

## Transition to Modern Cryptography

### Symmetric Encryption Evolution
```
Caesar → Vigenère → DES → AES
(Simple) (Polyalpha) (Complex) (Military-grade)
```

### Public-Key Cryptography (RSA)
- Solves key distribution problem
- Different keys for encryption/decryption
- Enables digital signatures
- Basis for HTTPS

### Hash Functions
- One-way transformation
- Input: Any length
- Output: Fixed size (typically 256-bit)
- Applications: Passwords, signatures, integrity

---

## Cybersecurity in 2026

### Threats & Defenses

| Threat | Defense | Cryptography |
|--------|---------|-------------|
| Eavesdropping | Encryption | AES |
| Man-in-the-Middle | Digital Signatures | RSA |
| Data Tampering | Hash Functions | SHA-256 |
| Brute Force | Strong Keys | 256-bit keys |
| Quantum Attacks | Post-Quantum Crypto | NIST standards |

### Post-Quantum Cryptography

**Why Needed**: Quantum computers will break RSA

**NIST Standardization**: 
- Lattice-based cryptography
- Hash-based signatures
- Code-based cryptography

**Timeline**: Transitioning 2023-2030

---

## Real-World Example: Secure Communication

### Process Overview

```
Alice → Message → Encryption (AES) → Network → Decryption (AES) → Bob
        ↑                                                      ↑
        Key Exchange (RSA)                    Key Management (HTTPS/TLS)
        ↑                                                      ↑
        Digital Signature (RSA)          Message Authentication (HMAC)
```

### Step-by-Step

1. **Key Exchange**: Alice and Bob use RSA to exchange AES key
2. **Encryption**: Alice encrypts message with AES key
3. **Authentication**: Alice signs with her private key (RSA)
4. **Transmission**: Encrypted message sent over network
5. **Decryption**: Bob decrypts with shared AES key
6. **Verification**: Bob verifies signature with Alice's public key

---

## Security Best Practices

### For Users
- Use strong passwords (12+ characters, mixed case, numbers, symbols)
- Enable two-factor authentication
- Keep software updated
- Use VPN on public WiFi
- Never share encryption keys
- Use password managers

### For Developers
- Never implement your own crypto
- Use established libraries (OpenSSL, libsodium, etc.)
- Hash passwords (don't encrypt them)
- Use authenticated encryption (AES-GCM)
- Rotate encryption keys regularly
- Implement rate limiting for brute force protection

### For Organizations
- Encrypt data at rest
- Encrypt data in transit (TLS)
- Manage encryption keys securely
- Regular security audits
- Compliance (GDPR, HIPAA, PCI-DSS)
- Incident response plan

---

## Summary

Cryptography is foundational to modern cybersecurity. Understanding classical ciphers provides the knowledge base for appreciating modern cryptographic solutions. All data security ultimately depends on cryptography working correctly.

### Key Takeaways

✓ Classical ciphers teach fundamental concepts
✓ Modern encryption (AES, RSA) is mathematically complex
✓ Key management is as important as the cipher
✓ Multiple layers of security are necessary
✓ Cryptography alone is not sufficient - requires full security framework
✓ Quantum computing will require new cryptographic methods

---

*Last Updated: July 2026*