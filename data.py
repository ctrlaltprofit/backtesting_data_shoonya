import requests
import json
import os
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone


ACCESS_TOKEN = "f556c5bdc135b09594a482a7438c424009244a5434814d41f6b380733a92f631"
UID = "FAXXXXX"
DATA_DIR = "./shoonyadata"

def get_today_midnight_timestamp_ist():
    # IST = UTC + 5:30
    IST = timezone(timedelta(hours=5, minutes=30))

    now_ist = datetime.now(IST)

    midnight_ist = now_ist.replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    return str(int(midnight_ist.timestamp()))


# ===== CONFIG =====
ST_TIMESTAMP = get_today_midnight_timestamp_ist()
ST_TIMESTAMP= "1777919400"    #uncomment if you want any other timestamp 



SYMBOLS_CONSTANT = {
    "NSE|26000": {
        "exch": "NSE",
        "tysm": "Nifty 50"
    },
    "NSE|26009": {
        "exch": "NSE",
        "tysm": "Nifty Bank"
    },
    "NSE|10576": {
        "exch": "NSE",
        "tysm": "NIFTYBEES-EQ"
    },
    "NSE|11439": {
        "exch": "NSE",
        "tysm": "BANKBEES-EQ"
    },
    "NSE|1333": {
        "exch": "NSE",
        "tysm": "HDFCBANK-EQ"
    },
    "NSE|4963": {
        "exch": "NSE",
        "tysm": "ICICIBANK-EQ"
    },
    "NSE|2885": {
        "exch": "NSE",
        "tysm": "RELIANCE-EQ"
    },
        "NSE|10604": {
        "exch": "NSE",
        "tysm": "BHARTIARTL-EQ"
    },
        "NSE|1594": {
        "exch": "NSE",
        "tysm": "INFY-EQ"
    },
        "NSE|11483": {
        "exch": "NSE",
        "tysm": "LT-EQ"
    },
        "NSE|3045": {
        "exch": "NSE",
        "tysm": "SBIN-EQ"
    },
        "NSE|5900": {
        "exch": "NSE",
        "tysm": "AXISBANK-EQ"
    },
        "NSE|1660": {
        "exch": "NSE",
        "tysm": "ITC-EQ"
    },
        "NSE|2031": {
        "exch": "NSE",
        "tysm": "M&M-EQ"
    },
    "NSE|1922": {
        "exch": "NSE",
        "tysm": "KOTAKBANK-EQ"
    },
    "NSE|11536": {
        "exch": "NSE",
        "tysm": "TCS-EQ"
    },
    "NSE|317": {
        "exch": "NSE",
        "tysm": "BAJFINANCE-EQ"
    },
    "NSE|1394": {
        "exch": "NSE",
        "tysm": "HINDUNILVR-EQ"
    },
    "NSE|3351": {
        "exch": "NSE",
        "tysm": "SUNPHARMA-EQ"
    },
    "NSE|3506": {
        "exch": "NSE",
        "tysm": "TITAN-EQ"
    },
    "NSE|11630": {
        "exch": "NSE",
        "tysm": "NTPC-EQ"
    },
    "NSE|10999": {
        "exch": "NSE",
        "tysm": "MARUTI-EQ"
    },
    "NSE|5097": {
        "exch": "NSE",
        "tysm": "ETERNAL-EQ"
    },
    "NSE|3499": {
        "exch": "NSE",
        "tysm": "TATASTEEL-EQ"
    },
    "NSE|383": {
        "exch": "NSE",
        "tysm": "BEL-EQ"
    },
    "NSE|7229": {
        "exch": "NSE",
        "tysm": "HCLTECH-EQ"
    },
    "NSE|1363": {
        "exch": "NSE",
        "tysm": "HINDALCO-EQ"
    },
    "NSE|14977": {
        "exch": "NSE",
        "tysm": "POWERGRID-EQ"
    },
    "NSE|4306": {
        "exch": "NSE",
        "tysm": "SHRIRAMFIN-EQ"
    },
    "NSE|11532": {
        "exch": "NSE",
        "tysm": "ULTRACEMCO-EQ"
    },
    "NSE|2475": {
        "exch": "NSE",
        "tysm": "ONGC-EQ"
    },
    "NSE|11723": {
        "exch": "NSE",
        "tysm": "JSWSTEEL-EQ"
    },
    "NSE|20374": {
        "exch": "NSE",
        "tysm": "COALINDIA-EQ"
    },
    "NSE|15083": {
        "exch": "NSE",
        "tysm": "ADANIPORTS-EQ"
    },
    "NSE|16669": {
        "exch": "NSE",
        "tysm": "BAJAJ-AUTO-EQ"
    },
    "NSE|1232": {
        "exch": "NSE",
        "tysm": "GRASIM-EQ"
    },
    "NSE|236": {
        "exch": "NSE",
        "tysm": "ASIANPAINT-EQ"
    },
    "NSE|16675": {
        "exch": "NSE",
        "tysm": "BAJAJFINSV-EQ"
    },
    "NSE|11195": {
        "exch": "NSE",
        "tysm": "INDIGO-EQ"
    },
    "NSE|13538": {
        "exch": "NSE",
        "tysm": "TECHM-EQ"
    },
    "NSE|910": {
        "exch": "NSE",
        "tysm": "EICHERMOT-EQ"
    },
    "NSE|17963": {
        "exch": "NSE",
        "tysm": "NESTLEIND-EQ"
    },
    "NSE|1964": {
        "exch": "NSE",
        "tysm": "TRENT-EQ"
    },
    "NSE|21808": {
        "exch": "NSE",
        "tysm": "SBILIFE-EQ"
    },
    "NSE|18143": {
        "exch": "NSE",
        "tysm": "JIOFIN-EQ"
    },
    "NSE|157": {
        "exch": "NSE",
        "tysm": "APOLLOHOSP-EQ"
    },
    "NSE|881": {
        "exch": "NSE",
        "tysm": "DRREDDY-EQ"
    },
    "NSE|22377": {
        "exch": "NSE",
        "tysm": "MAXHEALTH-EQ"
    },
    "NSE|3432": {
        "exch": "NSE",
        "tysm": "TATACONSUM-EQ"
    },
    "NSE|694": {
        "exch": "NSE",
        "tysm": "CIPLA-EQ"
    },
    "NSE|3456": {
        "exch": "NSE",
        "tysm": "TMPV-EQ"
    },
    "NSE|467": {
        "exch": "NSE",
        "tysm": "HDFCLIFE-EQ"
    },
    "NSE|3787": {
        "exch": "NSE",
        "tysm": "WIPRO-EQ"
    },
    "NSE|25": {
        "exch": "NSE",
        "tysm": "ADANIENT-EQ"
    }   
    
}

TP_URL = "https://api.shoonya.com/NorenWClientAPI/TPSeries"



# ===== FUNCTIONS =====
def fetch_and_save(symbol):
    exch = SYMBOLS_CONSTANT[symbol]["exch"]
    tysm = SYMBOLS_CONSTANT[symbol]["tysm"]

    values = {
        "ordersource": "API",
        "uid": UID,
        "exch": exch,
        "token": symbol.split("|")[1],
        "st": ST_TIMESTAMP
    }

    payload = "jData=" + json.dumps(values)
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        resp = requests.post(TP_URL, data=payload, headers=headers, timeout=15)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"❌ Error fetching {symbol}: {e}")
        return

    if isinstance(data, dict) and data.get("stat") != "Ok":
        print(f"❌ API Error for {symbol}: {data.get('emsg')}")
        return

    if not isinstance(data, list) or len(data) == 0:
        print(f"⚠️ No candle data for {symbol}")
        return

    folder_path = os.path.join(DATA_DIR, tysm)
    os.makedirs(folder_path, exist_ok=True)

    # ===== GROUP BY DATE =====
    date_map = {}

    for candle in data:
        dt_obj = datetime.strptime(candle["time"], "%d-%m-%Y %H:%M:%S")
        date_key = dt_obj.strftime("%Y-%m-%d")

        date_map.setdefault(date_key, []).append(candle)

    # ===== WRITE PER FILE (SAFE) =====
    for date_key, candles in date_map.items():
        file_path = os.path.join(folder_path, f"{date_key}.json")

        existing = []
        if os.path.exists(file_path):
            try:
                with open(file_path, "r") as f:
                    existing = json.load(f)
            except json.JSONDecodeError:
                print(f"❌ Fixing corrupted file: {file_path}")
                existing = []

        # merge
        existing_times = {c["time"] for c in existing}

        for c in candles:
            if c["time"] not in existing_times:
                existing.append(c)

        existing.sort(key=lambda x: x["time"])

        # ===== ATOMIC WRITE =====
        temp_path = file_path + ".tmp"
        with open(temp_path, "w") as f:
            json.dump(existing, f, indent=2)

        os.replace(temp_path, file_path)

    print(f"✅ Saved {len(data)} candles for {tysm}")


# ===== MAIN =====
def main():
    max_workers = min(5, len(SYMBOLS_CONSTANT))  # safer

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(fetch_and_save, sym) for sym in SYMBOLS_CONSTANT]

        for future in as_completed(futures):
            future.result()


if __name__ == "__main__":
    main()