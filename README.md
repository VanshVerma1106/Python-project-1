# Python-project-1

# 🔐 File Integrity Checker

A simple desktop-based **File Integrity Checker** built with **Python and Tkinter**.

The application generates cryptographic hashes for selected files using **SHA-256** or **MD5**, allowing users to verify whether a file has been modified or remains unchanged.

---

## ✨ Features

- 📂 **Browse and select any file**
- 🔒 Generate **SHA-256 hash**
- 🔑 Generate **MD5 hash**
- ✅ Compare a generated hash with an entered hash
- 🛡️ Verify file integrity
- 💾 Save generated hash to a `.txt` file
- 🌙 Dark Mode
- ☀️ Light Mode
- 🖥️ Simple graphical user interface
- 📊 Hashes are calculated in chunks, allowing large files to be processed without loading the entire file into memory

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Application development |
| **Tkinter** | Graphical User Interface |
| **hashlib** | SHA-256 and MD5 hash generation |
| **os** | File and path handling |

All libraries used by the application are part of Python's standard library.

---

## 📸 Application Workflow

The application follows a simple workflow:

```text
Select File
    ↓
Generate Hash
    ↓
SHA-256 / MD5
    ↓
Display Hash
    ↓
Enter/Compare Hash
    ↓
Integrity Verified / Integrity Failed
