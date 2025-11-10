# OTP Verification System using Flask and Twilio

This project demonstrates how to build a **secure OTP (One-Time Password) verification system** using **Twilio’s Verify API** and a **Flask backend**.  
It allows users to input their phone number, receive an OTP via SMS, and verify it through a simple and elegant frontend.

---

## Overview

The system performs three key operations:

1. **Send OTP:** The user enters a valid phone number and receives an OTP via SMS.  
2. **Verify OTP:** The user enters the OTP received on their phone to confirm identity.  
3. **Redirect After Verification:** Once verified, the system redirects the user to a “Home” page.

This setup is ideal for integrating into **secure login systems**, **two-factor authentication (2FA)**, or **user registration flows**.

---

## Features

- Built using **Flask (Python)** as the backend server.  
- Integrated with **Twilio Verify API** for OTP generation and verification.  
- **Responsive and modern frontend** built with HTML, CSS, and JavaScript.  
- Simple structure — easy to customize and expand.  
- Automatic redirect after successful verification.

---

## Project Structure

```
OTP-Verification/
│
├── app.py                # Flask backend
├── requirements.txt      # Python dependencies
│
├── index.html
├── home.html
│
└── README.md             # Project documentation
```

---

## Prerequisites

Before running this project, ensure you have:

- **Python 3.8 or higher**  
- A **Twilio Account** (Trial or Paid)  
- **Flask** installed in your environment  
- An **active internet connection** (Twilio requires it)

---

## 1. Twilio Setup

To use Twilio’s OTP service, you need to set up a **Verify Service**.

### Step 1: Create a Twilio Account
- Go to [https://www.twilio.com/try-twilio](https://www.twilio.com/try-twilio)
- Sign up or log in to your Twilio account.

### Step 2: Get Account Credentials
After signing in:
- Navigate to **Twilio Console → Account Info**
- Copy your:
  - **Account SID**
  - **Auth Token**

### Step 3: Create a Verify Service
- In the Twilio Dashboard, go to **“Verify” → “Services”**
- Click **Create New Service**
- Enter a name (e.g., “OTP Verification Service”)
- Copy the generated **Service SID** (it starts with `VA...`)

### Step 4: Verify Phone Numbers (Trial Accounts Only)
If you are using a **Trial Account**, Twilio only allows sending OTPs to verified numbers.
- Navigate to **Verified Caller IDs**
- Add and verify your phone number before testing.

---

## 2. Project Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/OTP-Verification-Flask.git
cd OTP-Verification-Flask
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a file named `.env` in the project root and add:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_VERIFY_SID=your_verify_service_sid_here
```

### Step 4: Run the Flask Server

```bash
python app.py
```

You should see:

```
Twilio OTP Verification API is running 🚀
```

Now, open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 3. Using the Application

1. Enter your phone number (with country code, e.g., +91XXXXXXXXXX)  
2. Click **Send OTP**  
3. Enter the OTP received on your phone  
4. Upon successful verification, you’ll be redirected to the **Home Page**

---

## 4. Common Issues

**Error:** “The phone number is unverified”  
→ This occurs on a Twilio trial account. You must verify your number under **Twilio Console → Phone Numbers → Verified Caller IDs.**

**Error:** “Invalid Parameter”  
→ Ensure your phone number format includes the **country code** (e.g., `+1`, `+91`, etc.)

**Error:** “Server Not Reachable”  
→ Make sure Flask is running and the API endpoint matches the URL in your frontend JavaScript.

---

## 5. Customization Ideas

You can enhance this project by:
- Adding **email-based OTP verification**.  
- Storing verified users in a **database** (SQLite, MongoDB, or Firebase).  
- Adding **login/signup integration**.  
- Building a **React or Vue frontend**.  
- Deploying on **Render**, **Netlify**, or **Vercel** with a Flask backend.

---

## 6. License

This project is open-source and available under the **MIT License**.  
You are free to use, modify, and distribute it for personal or commercial projects.

---

**Author:** Anindya Maity  
**Category:** Flask + Twilio Projects  
**Description:** Secure OTP verification system with Twilio Verify API integration.
