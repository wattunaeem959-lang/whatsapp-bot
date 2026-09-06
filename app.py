from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request
import os
import google.generativeai as genai
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/")
def home():
    return "Bot is Running with FREE AI!"

@app.route("/whatsapp-reply", methods=["POST"])
def whatsapp_reply():
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
        ai_reply = "AI thoda busy hai, 1 min baad try karo 🙏"

    msg.body(ai_reply)
    return str(resp)