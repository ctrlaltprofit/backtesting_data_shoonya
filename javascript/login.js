import { chromium } from 'playwright';
import { OTP } from 'otplib';
import { URL } from 'url';

import axios from 'axios';
import crypto from 'crypto';

import { credentials } from './data/cred.js';

const CLIENT_ID   = credentials.client_id;
const USER_ID     = credentials.userid;
const PASSWORD    = credentials.password;
const TOTP_SECRET = credentials.totp_secret;
const SECRET_CODE = credentials.secret_code;

const LOGIN_URL =
  `https://trade.shoonya.com/OAuthlogin/investor-entry-level/login?api_key=${CLIENT_ID}&route_to=abc`;

const TOKEN_URL =
  'https://api.shoonya.com/NorenWClientAPI/GenAcsTok';



function generateChecksum(clientId, secretCode, authCode) {
  return crypto
    .createHash('sha256')
    .update(clientId + secretCode + authCode, 'utf8')
    .digest('hex');
}


export async function captureAuthCode() {

  const otp = new OTP();

  const browser = await chromium.launch({
    headless: true
    // slowMo: 100
  });

  const page = await browser.newPage();

  let authCode = null;

  try {

    console.log('Opening login page...');

    // Capture auth code
    page.on('request', request => {

      const requestUrl = request.url();

      if (
        requestUrl.includes('code=') &&
        requestUrl.toLowerCase().includes('shoonya')
      ) {

        const parsedUrl = new URL(requestUrl);

        authCode = parsedUrl.searchParams.get('code');

        console.log('✅ Auth code captured');
      }
    });

    await page.goto(LOGIN_URL, {
      waitUntil: 'networkidle'
    });

    // Fill login details
    await page.fill('#lgnusrid', USER_ID);
    await page.fill('#lgnpwd', PASSWORD);

    let otpValue = otp.generateSync({
      secret: TOTP_SECRET
    });

    await page.fill('#lgnotp', otpValue);

    await page.click("button:has-text('LOGIN')");

    console.log('Login submitted...');

    const start = Date.now();

    while (!authCode && Date.now() - start < 60000) {

      await page.waitForTimeout(500);

      // Refresh OTP automatically
      const newOtp = otp.generateSync({
        secret: TOTP_SECRET
      });

      if (newOtp !== otpValue) {

        otpValue = newOtp;

        console.log('Refreshing OTP...');

        await page.fill('#lgnotp', otpValue);

        await page.click("button:has-text('LOGIN')");
      }
    }

    if (!authCode) {
      console.log('❌ Could not capture auth code');
      return null;
    }

    console.log('✅ Auth Code:', authCode);

    return authCode;

  } catch (err) {

    console.error('Error:', err.message);

    return null;

  } finally {

    await browser.close();
  }
}


export async function login() {

  const authCode = await captureAuthCode();

  if (!authCode) {
    console.log('Failed to capture auth code');
    return;
  }

  const checksum = generateChecksum(
    CLIENT_ID,
    SECRET_CODE,
    authCode
  );

  console.log('Checksum:', checksum);

  const jData = {
    code: authCode,
    checksum
  };

  try {

    const response = await axios.post(
      TOKEN_URL,
      `jData=${JSON.stringify(jData)}`,
      {
        headers: {
          'Content-Type':
            'application/x-www-form-urlencoded'
        }
      }
    );

    const accessToken =
      response.data?.access_token;

    if (!accessToken) {

      console.log(
        'Access token not found:',
        response.data
      );

      return;
    }

    console.log(accessToken);

  } catch (err) {

    console.error(
      err.response?.data || err.message
    );
  }
}


login();
