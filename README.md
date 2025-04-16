# 🐧 Remote Linux FS Audit & Data Pipeline

### 🔧 Description
This project automates the process of gathering filesystem (FS) usage data from remote Linux machines, formats the data into a structured CSV report, and stores it securely in a remote MySQL database. The tool uses modular scripting with Bash and Python, applies secure credential handling via encryption, and includes OS detection logic to ensure command compatibility.

---

### 🧰 Features

- 🔍 Remote OS detection before execution
- 📁 Collect filesystem usage data (excluding temp mounts)
- 📄 Save report as CSV with additional fields (IP, hostname, date)
- 🔒 Encrypt credentials securely using Fernet
- 📡 Insert CSV data into remote MySQL DB
- 🧠 Modular JSON-based command structure
- 👨‍💻 Optional view of DB entries through command-line prompt

---

### 📁 File Structure

| File | Description |
|------|-------------|
| `my_commands.json` | Stores Linux shell commands to execute remotely |
| `script_for_csv.py` | Executes remote commands, generates CSV report |
| `the_great_python_project.py` | Inserts CSV data into remote DB, decrypts credentials |
| `credentials.enc` | Encrypted file containing database login credentials |

---

### 🔒 Security Practices

- Credentials are **not hardcoded** — stored in a separate, encrypted file.
- Only **non-temporary mount points** are included in FS report.
- Modularized and **reusable scripts** for real-world environments.

---

### 📦 Requirements

- Python 3.x  
- MySQL Connector: `pip install mysql-connector-python`  
- Paramiko: `pip install paramiko`  
- Cryptography: `pip install cryptography`

---

### ▶️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/syed-913/linux-automation-scripts.git
   ```
2. Place your encrypted credentials file as credentials.enc
3. Run the CSV generator:
   ```bash
   python3 script_for_csv.py
   ```
4. Push data to DB:
   ```bash
   python3 the_great_python_project.py
   ```
--- 

📌 Future Enhancements

- Add email alerting for disk usage thresholds
- Expand to support Windows servers (PowerShell-based)
- Use SQLite as local fallback if DB connection fails
- Dockerize the setup

--- 

🙏 Credits

Made with ❤️ by Syed Ammar Hussain
Part of my journey into Linux automation & cybersecurity.

>  ⚠️ For educational use only. Do not deploy on production environments without adaptation.

