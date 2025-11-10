# =====================================================
# 📱 Twilio OTP Verification Server using Flask
# Secure Backend API for Sending & Verifying OTP Codes
# =====================================================

from flask import Flask, request, jsonify
from twilio.rest import Client
from dotenv import load_dotenv
from flask_cors import CORS
import os

# -------------------------------
# Load Environment Variables
# -------------------------------
load_dotenv()

# Initialize Flask App
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Allow all origins for testing

# -------------------------------
# Twilio Credentials
# -------------------------------
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
VERIFY_SERVICE_SID = os.getenv("TWILIO_VERIFY_SERVICE_SID")

# Check Twilio credentials
if not all([ACCOUNT_SID, AUTH_TOKEN, VERIFY_SERVICE_SID]):
    raise EnvironmentError("❌ Missing Twilio credentials in .env file.")

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# -------------------------------
# Root Route - Health Check
# -------------------------------
@app.route('/')
def home():
    return jsonify({
        "status": "OK",
        "message": "Twilio OTP Verification API is running 🚀",
        "endpoints": ["/api/send-code", "/api/verify-code"]
    })


# -------------------------------
# 1️⃣ Endpoint - Send OTP
# -------------------------------
@app.route('/api/send-code', methods=['POST'])
def send_code():
    data = request.get_json()
    to_number = data.get('to')

    if not to_number:
        return jsonify({"success": False, "error": "Phone number is required."}), 400

    try:
        verification = client.verify.v2.services(VERIFY_SERVICE_SID).verifications.create(
            to=to_number,
            channel='sms'
        )

        print(f"[✅] OTP sent to {to_number} | Status: {verification.status}")

        return jsonify({
            "success": True,
            "message": f"OTP sent successfully to {to_number}.",
            "status": verification.status
        })

    except Exception as e:
        print(f"[❌] Twilio Send Error: {e}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


# -------------------------------
# 2️⃣ Endpoint - Verify OTP
# -------------------------------
@app.route('/api/verify-code', methods=['POST'])
def verify_code():
    data = request.get_json()
    to_number = data.get('to')
    code = data.get('code')

    if not to_number or not code:
        return jsonify({"success": False, "error": "Phone number and code are required."}), 400

    try:
        verification_check = client.verify.v2.services(VERIFY_SERVICE_SID).verification_checks.create(
            to=to_number,
            code=code
        )

        print(f"[🔍] Verifying {to_number} | Status: {verification_check.status}")

        if verification_check.status == 'approved':
            return jsonify({
                "success": True,
                "message": "✅ Verification successful."
            })
        else:
            return jsonify({
                "success": False,
                "error": "Invalid or expired code."
            }), 401

    except Exception as e:
        print(f"[❌] Twilio Verify Error: {e}")
        return jsonify({
            "success": False,
            "error": "Verification failed. Check server logs."
        }), 500


# -------------------------------
# Run Flask App
# -------------------------------
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"\n🚀 Flask Server running at http://127.0.0.1:{port}")
    print("⚙️  Ensure your .env has TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, and TWILIO_VERIFY_SERVICE_SID.\n")
    app.run(host="0.0.0.0", port=port, debug=True)