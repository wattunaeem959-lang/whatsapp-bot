from flask import Flask, request
import os
import google.generativeai as genai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        incoming_msg = request.values.get('Body', '').strip()
        resp = MessagingResponse()
        msg = resp.message()

        if not incoming_msg:
            msg.body("Bolo kya help chahiye?")
            return str(resp)

        try:
            response = model.generate_content(incoming_msg)
            ai_reply = response.text
        except Exception as e:
    print(f"Gemini Error: {e}")
    ai_reply = f"Error: {e}"
        msg.body(ai_reply)
        return str(resp)

@app.route("/whatsapp-reply", methods=["POST"])
def whatsapp_reply():
    return home()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
