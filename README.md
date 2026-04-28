# 🔐 Python Credential Management System
> A learning-driven security project evolving from a basic encryption script into a production-grade credential vault — built to demonstrate applied cryptography and secure software development principles.

---

## 🧠 What This Project Is

A Python-based credential storage and encryption system — think a lightweight version of HashiCorp Vault or a personal password manager — built from the ground up with security as the core design principle.

The goal is not just to build a working tool, but to demonstrate **how a developer thinks about security** at every layer of an application.

---

## 🗺️ Progression Roadmap

### ✅ Phase 1 — Foundation (Complete)
> *Core logic and basic security concepts*

- [x] Luhn algorithm for credit card validation (same logic used in real payment systems)
- [x] Vigenère cipher for basic credential encryption
- [x] JSON-based persistent storage
- [x] Input validation (card length, digit-only checks, PIN length)
- [x] Basic error handling and user menu (CLI)

**What I learned:** How data validation works at the input layer, how symmetric cipher logic works, and how to persist structured data with JSON.

---

### 🔄 Phase 2 — Real Cryptography (In Progress)
> *Replacing toy encryption with industry-standard security*

- [x] Replace Vigenère cipher with **AES-256 encryption** using Python's `cryptography` library (`Fernet`)
- [ ] Replace plain-text PIN storage with **bcrypt hashing**
- [ ] Implement **salted hashing** to protect against rainbow table attacks
- [ ] Secure key management — separating the encryption key from stored data

**Why this matters:** AES-256 is the encryption standard used by banks, governments, and enterprise security systems. bcrypt is the industry standard for password storage. Adding these two things alone takes this from a learning exercise to something genuinely defensible in a technical interview.

---

### 📋 Phase 3 — Security Controls (Planned)
> *Mirroring real-world authentication security*

- [ ] **Login attempt lockout** — lock account after N failed attempts (mirrors enterprise auth controls)
- [ ] **Audit logging** — every access attempt logged with timestamp, username, and outcome
- [ ] **Session management** — time-out inactive sessions
- [ ] Structured log output compatible with SIEM ingestion (JSON format)

**Why this matters:** These are the exact controls I've worked with in Microsoft Sentinel and Wazuh. Building them from scratch deepens my understanding of *why* they exist and *how* they work at the code level.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core language |
| `cryptography` (Fernet/AES-256) | Encryption — Phase 2 |
| `bcrypt` | Password hashing — Phase 2 |
| `json` | Persistent storage |
| `logging` | Audit trail — Phase 3 |
| Flask *(planned)* | Web interface — Phase 4 |

---

## 🔗 How This Connects to My Cybersecurity Work

This project is intentionally built alongside my SOC and defensive security work:

- The **audit logging** in Phase 3 mirrors the log ingestion pipelines I built in my [Cloud SOC Lab](https://github.com/jmulumbi/Cloud-SOC-Detection-Lab)
- Understanding **how credentials are stored and attacked** makes me a better SOC analyst — I know what brute-force and credential stuffing look like because I've built the defenses from scratch
- The **lockout and session controls** in Phase 3 reflect the same MITRE ATT&CK techniques (T1110 — Brute Force) I've written detection rules for in Microsoft Sentinel


## 📬 Connect

- 💼 [linkedin.com/in/jeremiah-mulumbi-642501251](https://linkedin.com/in/jeremiah-mulumbi-642501251)
- 📧 mulumbijeremiah@gmail.com
