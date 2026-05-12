# backtesting_data_shoonya

Shoonya automation and historical market data toolkit built using Python and JavaScript.

This repository contains:

- Python-based historical candle downloader
- JavaScript-based automated Shoonya login system
- TOTP authentication workflow
- Access token generation utilities
- Structured market data storage

---

# Repository Structure

```bash
backtesting_data_shoonya/
│
├── README.md
├── .gitignore
│
├── python/
│   ├── README.md
│   ├── login.py
│   ├── data.py
│   └── ...
│
└── javascript/
    ├── README.md
    ├── login.js
    └── ...
```

---

# Modules

## Python Module

Location:

```bash
python/
```

Features:

- Historical candle data download
- Multi-threaded fetching
- Shoonya API integration
- Structured JSON storage
- Automated login flow

See:

```bash
python/README.md
```

for detailed setup and usage.

---

## JavaScript Login Module

Location:

```bash
javascript/
```

Features:

- Automated Shoonya login
- Playwright browser automation
- TOTP authentication
- OAuth auth code capture
- Access token generation

See:

```bash
javascript/README.md
```

for detailed setup and usage.

---

# Tech Stack

## Python Side

- Python
- Playwright
- Requests
- PyOTP

## JavaScript Side

- Node.js
- Playwright
- Axios
- Otplib

---

# Installation

Clone repository:

```bash
git clone git@github-ctrlaltprofit:ctrlaltprofit/backtesting_data_shoonya.git

cd backtesting_data_shoonya
```

---

# Recommended .gitignore

```gitignore
# Python
venv/
__pycache__/
*.pyc

# Node
node_modules/

# Secrets
data/cred.py
data/cred.js

# Data
shoonyadata/
```

---

# Security Notes

- Never commit credentials
- Never commit access tokens
- Keep secret files inside `.gitignore`
- Shoonya authentication flow may change anytime

---

# Disclaimer

This project is for educational and personal use only.

Use Shoonya APIs responsibly and according to their terms of service.

---

# Author

GitHub: @ctrlaltprofit