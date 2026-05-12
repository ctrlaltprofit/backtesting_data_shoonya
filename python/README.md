# backtesting_data_shoonya

Automated historical candle data downloader for Shoonya API using Python.

This project:

- Logs into Shoonya automatically using Playwright + TOTP
- Generates access token
- Downloads historical candle data
- Saves candles into structured JSON files
- Supports multi-threaded fetching
- Organizes data symbol-wise and date-wise

---

# Features

✅ Fully automated Shoonya login  
✅ TOTP based authentication  
✅ Auto access token generation  
✅ Historical candle data download  
✅ Threaded data fetching  
✅ Atomic file saving (safe writes)  
✅ Duplicate candle protection  
✅ Date-wise JSON storage  
✅ Easy to extend with more symbols  

---

# Project Structure

```bash
backtesting_data_shoonya/
│
├── login.py
├── data_fetch.py
├── requirements.txt
│
├── data/
│   └── cred.py
│
└── shoonyadata/
    ├── Nifty 50/
    │   ├── 2026-05-12.json
    │   └── ...
    │
    ├── HDFCBANK-EQ/
    └── ...
```

---

# Installation

## 1. Clone Repository

```bash
git clone git@github-ctrlaltprofit:ctrlaltprofit/backtesting_data_shoonya.git

cd backtesting_data_shoonya
```

---

## 2. Create Virtual Environment

### Linux / Ubuntu

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Playwright Browser

```bash
playwright install
```

---

# credentials Setup

Create:

```bash
data/cred.py
```

Add:

```python
credentials = {
    "client_id": "YOUR_CLIENT_ID",
    "userid": "YOUR_USER_ID",
    "password": "YOUR_PASSWORD",
    "totp_secret": "YOUR_TOTP_SECRET",
    "secret_code": "YOUR_SECRET_CODE"
}
```

---

# Generate Access Token

Run:

```bash
python login.py
```

If successful:

```bash
✅ Auth code captured
✅ Auth Code: xxxxx
Checksum: xxxxx
<ACCESS_TOKEN>
```

Copy the generated access token.

---

# Configure Data Script

Inside `data_fetch.py`:

```python
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
UID = "YOUR_USER_ID"
```

---

# Run Data Downloader

```bash
python data_fetch.py
```

Example output:

```bash
✅ Saved 375 candles for Nifty 50
✅ Saved 375 candles for HDFCBANK-EQ
```

---

# Data Storage Format

Data is stored as:

```bash
shoonyadata/<SYMBOL>/<DATE>.json
```

Example:

```bash
shoonyadata/HDFCBANK-EQ/2026-05-12.json
```

Example candle:

```json
{
  "time": "12-05-2026 09:15:00",
  "into": "1900.00",
  "inth": "1905.00",
  "intl": "1898.00",
  "intc": "1902.00",
  "v": "120000"
}
```

---

# Supported Symbols

Currently includes:

- Nifty 50
- Bank Nifty
- HDFCBANK
- ICICIBANK
- RELIANCE
- INFY
- TCS
- SBIN
- AXISBANK
- ITC
- And more...

You can add more symbols inside:

```python
SYMBOLS_CONSTANT
```

---

# Timestamp Configuration

Default:

```python
ST_TIMESTAMP = get_today_midnight_timestamp_ist()
```

Custom timestamp:

```python
ST_TIMESTAMP = "1777919400"
```

---

# Tech Stack

- Python
- Playwright
- Requests
- PyOTP
- ThreadPoolExecutor

---

# requirements.txt

Example:

```txt
playwright
requests
pyotp
```

---

# Important Notes

- Access tokens expire periodically
- Generate a new token when required
- Do NOT commit credentials or tokens
- Add sensitive files to `.gitignore`

Example:

```gitignore
venv/
__pycache__/
data/cred.py
shoonyadata/
```

---

# Disclaimer

This project is for educational and personal use only.

Use Shoonya APIs responsibly and according to their terms of service.

---

# Author

GitHub: @ctrlaltprofit