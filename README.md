# 🔐 Python Credential Management System
> A learning-driven security project evolved from a basic encryption script into a credential vault — built to demonstrate applied cryptography and secure software development principles.

---

## 🧠 What This Project Is

A Python-based credential storage and encryption system — think a lightweight version of a personal password manager — built from the ground up with security as the core design principle.

The goal is not just to build a working tool, but to demonstrate **how a developer thinks about security** at every layer of an application.

---

## ✅ What Has Been Built

### Phase 1 — Foundation
> *Core logic and basic security concepts*

- [x] Luhn algorithm for credit card validation (same checksum logic used by Visa and Mastercard in real payment systems)
- [x] Vigenère cipher for basic credential encryption (since replaced)
- [x] JSON-based persistent storage
- [x] Input validation — card length, digit-only checks, PIN length enforcement
- [x] Basic error handling and user menu (CLI)

**What I learned:** How data validation works at the input layer, how symmetric cipher logic works, and how to persist structured data with JSON.

---

### Phase 2 — Real Cryptography
> *Replacing toy encryption with industry-standard security*

- [x] Replaced Vigenère cipher with **AES-128 encryption** via Python's `cryptography` library (`Fernet`)
- [x] Replaced plain-text PIN storage with **bcrypt hashing**
- [x] Implemented **salted hashing** to protect against rainbow table attacks
- [x] Secure key management — encryption keys stored separately from card data using `base64` encoding
- [x] BIN/network detection — identifies card network (Visa, Mastercard, Amex, Discover) from card prefix

**Why this matters:** AES encryption is the standard used by banks, governments, and enterprise security systems. bcrypt is the industry standard for password storage. The unique salt generated per PIN means even two identical PINs produce completely different hashes — making bulk attacks impossible.

---

## 🖥️ Features

| Feature | Description |
|---|---|
| **Add Card** | Validates card via Luhn algorithm, encrypts with Fernet, hashes PIN with bcrypt |
| **View Card** | PIN-authenticated decryption — card number only revealed after bcrypt verification |
| **Remove Card** | PIN-authenticated deletion — removes card and matching encryption key in sync |
| **List Cards** | Displays all stored cards masked (`**** **** **** 1234`) — no PIN required |
| **Change PIN** | Verifies current PIN via bcrypt before allowing update — new PIN re-hashed on save |

---

## 🔒 Security Design Decisions

**Why bcrypt over SHA256?**
SHA256 is fast — which is a weakness for password storage. bcrypt is intentionally slow and includes a configurable cost factor, making brute force attacks significantly harder. Every PIN also gets a unique salt, so identical PINs never produce the same hash.

**Why Fernet over a custom cipher?**
The Vigenère cipher used in Phase 1 is trivially breakable. Fernet uses AES-128-CBC with HMAC-SHA256 for authentication — meaning it detects if encrypted data has been tampered with, not just scrambled.

**Why separate encryption keys per card?**
Each card gets its own unique Fernet key. If one key is compromised, only that card is exposed — not the entire vault. This mirrors the principle of **key isolation** used in enterprise key management systems like AWS KMS.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|---|---|
| Python | Core language |
| `cryptography` (Fernet/AES-128) | Card number encryption |
| `bcrypt` | PIN hashing with salt |
| `json` | Persistent storage |
| `base64` | Key encoding for JSON compatibility |
| `os` | File existence checks and path management |

---

## 📁 Project Structure

```
Python-Security-Focused-CLI-Tool/
│
├── Cipher.py          # Main application
├── cards.json         # Encrypted card storage (auto-generated)
├── key.json           # Encryption keys (auto-generated)
└── README.md
```

---

## 🧪 Test Cards (Valid Luhn Numbers)

```
Card Number: 1234123412361236 — Pin: 4566
Card Number: 4829173648291736 — Pin: 3201
Card Number: 6738492017463824 — Pin: 3532
```

---

## 🔗 How This Connects to My Cybersecurity Work

This project is intentionally built alongside my SOC and defensive security work:

- Understanding **how credentials are stored and attacked** makes me a better SOC analyst — I know what brute-force and credential stuffing look like because I've built the defenses from scratch
- The **bcrypt lockout and PIN verification logic** reflects the same MITRE ATT&CK techniques (T1110 — Brute Force) I've written detection rules for in Microsoft Sentinel
- The **key isolation pattern** used here mirrors concepts from the secrets management pipelines in my [Cloud SOC Lab](https://github.com/jmulumbi/Cloud-SOC-Detection-Lab)

---

## 📬 Connect

- 💼 [linkedin.com/in/jeremiah-mulumbi-642501251](https://linkedin.com/in/jeremiah-mulumbi-642501251)
- 📧 [mulumbijeremiah@gmail.com](mailto:mulumbijeremiah@gmail.com)