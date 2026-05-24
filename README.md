# PENETRATION-TESTING-TOOLKIT

A lightweight, Python-based modular cybersecurity toolkit designed for network reconnaissance and security auditing.

## 📌 Project Overview
This toolkit is built using a highly scalable modular architecture. The core engine (`toolkit.py`) acts as a central control panel that dynamically interacts with individual, decoupled scanning modules housed within the `modules/` directory.

## 🚀 Features
- **Modular Framework**: Easily expand the toolkit by dropping new scripts into the modules directory.
- **Port Scanner**: Utilizes native network sockets to probe target IP addresses for active communication ports (FTP, SSH, HTTP, HTTPS).
- **Clean CLI Interface**: Simple, interactive command-line interface for seamless navigation.

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x installed on your host machine.

### Running the Toolkit
1. Clone or download this project directory to your local machine.
2. Open your terminal/command prompt inside the project folder.
3. Execute the controller script:
   ```bash
   python toolkit.py
   ```
4. Enter a target IP address (Use `127.0.0.1` for safe local loopback testing).

## 📁 Directory Structure
```text
pentest_toolkit/
│
├── toolkit.py          # Main application controller
├── README.md           # Project documentation
│
└── modules/            # Sub-directory for individual tools
    ├── __init__.py     # Initializer to mark the directory as a Python package
    └── port_scanner.py # Port scanning module logic
```

## ⚖️ Disclaimer
This toolkit is developed strictly for educational purposes and authorized security assessments. Unauthorized scanning of external networks or infrastructure without explicit, prior written consent is strictly illegal. The developer assumes no liability for misuse.




OUTPUT:
<img width="1920" height="1030" alt="Image" src="https://github.com/user-attachments/assets/cd55dee2-f7ee-4e7b-be3a-900ba1c3b46f" />
