# login.py

from playwright.sync_api import sync_playwright
from pyotp import TOTP

from urllib.parse import urlparse, parse_qs

import requests
import hashlib
import json
import time

from data.cred import credentials


CLIENT_ID   = credentials["client_id"]
USER_ID     = credentials["userid"]
PASSWORD    = credentials["password"]
TOTP_SECRET = credentials["totp_secret"]
SECRET_CODE = credentials["secret_code"]


LOGIN_URL = (
    f"https://trade.shoonya.com/OAuthlogin/investor-entry-level/login"
    f"?api_key={CLIENT_ID}&route_to=abc"
)

TOKEN_URL = (
    "https://api.shoonya.com/NorenWClientAPI/GenAcsTok"
)


def generate_checksum(client_id, secret_code, auth_code):

    data = client_id + secret_code + auth_code

    return hashlib.sha256(
        data.encode("utf-8")
    ).hexdigest()


def capture_auth_code():

    totp = TOTP(TOTP_SECRET)

    auth_code = None

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
            # slow_mo=100
        )

        page = browser.new_page()

        print("Opening login page...")

        # Capture auth code from requests
        def handle_request(request):

            nonlocal auth_code

            request_url = request.url

            if (
                "code=" in request_url and
                "shoonya" in request_url.lower()
            ):

                parsed = urlparse(request_url)

                params = parse_qs(parsed.query)

                auth_code = params.get("code", [None])[0]

                print("✅ Auth code captured")

        page.on("request", handle_request)

        try:

            page.goto(
                LOGIN_URL,
                wait_until="networkidle"
            )

            # Fill login details
            page.fill("#lgnusrid", USER_ID)

            page.fill("#lgnpwd", PASSWORD)

            otp_value = totp.now()

            page.fill("#lgnotp", otp_value)

            page.click("button:has-text('LOGIN')")

            print("Login submitted...")

            start = time.time()

            while (
                not auth_code and
                time.time() - start < 60
            ):

                page.wait_for_timeout(500)

                # Refresh OTP automatically
                new_otp = totp.now()

                if new_otp != otp_value:

                    otp_value = new_otp

                    print("Refreshing OTP...")

                    page.fill("#lgnotp", otp_value)

                    page.click(
                        "button:has-text('LOGIN')"
                    )

            if not auth_code:

                print("❌ Could not capture auth code")

                return None

            print("✅ Auth Code:", auth_code)

            return auth_code

        except Exception as err:

            print("Error:", str(err))

            return None

        finally:

            browser.close()


def login():

    auth_code = capture_auth_code()

    if not auth_code:

        print("Failed to capture auth code")

        return

    checksum = generate_checksum(
        CLIENT_ID,
        SECRET_CODE,
        auth_code
    )

    print("Checksum:", checksum)

    j_data = {
        "code": auth_code,
        "checksum": checksum
    }

    try:

        response = requests.post(
            TOKEN_URL,
            data=f'jData={json.dumps(j_data)}',
            headers={
                'Content-Type':
                'application/x-www-form-urlencoded'
            }
        )

        response_json = response.json()

        access_token = response_json.get(
            "access_token"
        )

        if not access_token:

            print(
                "Access token not found:",
                response_json
            )

            return

        print(access_token)

        return access_token

    except Exception as err:

        print("Error:", str(err))


login()