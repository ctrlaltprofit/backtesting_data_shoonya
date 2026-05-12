# shoonya_js_login

Automated Shoonya login and access token generator using JavaScript, Playwright, and TOTP authentication.

This project:

- Opens Shoonya login automatically
- Handles TOTP-based authentication
- Captures OAuth auth code
- Generates Shoonya access token
- Uses Playwright for browser automation
- Uses Axios for API requests

---

# Features

✅ Automated Shoonya login  
✅ TOTP authentication  
✅ OAuth auth code capture  
✅ SHA256 checksum generation  
✅ Access token generation  
✅ Headless browser automation  
✅ Easy credential configuration  

---

# Project Structure

```bash
js_login/
│
├── login.js
├── package.json
├── package-lock.json
│
└── data/
    └── cred.js
```

---

# Installation

## 1. Navigate to Folder

```bash
cd js_login
```

---

## 2. Install Dependencies

```bash
npm install
```

---

## 3. Install Playwright Browser

```bash
npx playwright install
```

---

# Credentials Setup

Create:

```bash
data/cred.js
```

Add:

```javascript
export const credentials = {
  client_id: "YOUR_CLIENT_ID",
  userid: "YOUR_USER_ID",
  password: "YOUR_PASSWORD",
  totp_secret: "YOUR_TOTP_SECRET",
  secret_code: "YOUR_SECRET_CODE"
};
```

---

# Run Login Script

```bash
node login.js
```

Example output:

```bash
Opening login page...
Login submitted...
✅ Auth code captured
✅ Auth Code: xxxxx
Checksum: xxxxx
<ACCESS_TOKEN>
```

---

# How It Works

## Step 1 — Browser Automation

Uses Playwright to:

- Open Shoonya login page
- Fill user ID and password
- Generate TOTP automatically
- Submit login form

---

## Step 2 — Auth Code Capture

The script listens for OAuth redirect requests and extracts:

```bash
code=<AUTH_CODE>
```

from the redirect URL.

---

## Step 3 — Checksum Generation

SHA256 checksum is generated using:

```javascript
client_id + secret_code + auth_code
```

---

## Step 4 — Access Token Generation

The auth code and checksum are sent to:

```bash
https://api.shoonya.com/NorenWClientAPI/GenAcsTok
```

to generate the final access token.

---

# Tech Stack

- JavaScript (Node.js)
- Playwright
- Axios
- OTPAuth / otplib
- Crypto

---

# Dependencies

Main packages:

```bash
playwright
axios
otplib
```

---

# .gitignore

Recommended:

```gitignore
node_modules/
data/cred.js
```

---

# Important Notes

- Access tokens expire periodically
- Generate a fresh token when required
- Never commit credentials
- Keep secret files inside `.gitignore`
- Shoonya may change login flow anytime

---

# Run in Headless Mode

Default:

```javascript
headless: true
```

For debugging:

```javascript
headless: false
```

---

# Disclaimer

This project is for educational and personal use only.

Use Shoonya APIs responsibly and according to their terms of service.

---

# Author

GitHub: @ctrlaltprofit