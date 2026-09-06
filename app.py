from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/")
def home():
    return "Bot is Running with AI!"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    msg = resp.message()

    if not incoming_msg:
        msg.body("Bolo kya help chahiye?")
        return str(resp)

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful WhatsApp assistant. Reply in Hinglish, short and friendly."},
                {"role": "user", "content": incoming_msg}
            ]
        )
        ai_reply = completion.choices[0].message.content
        msg.body(ai_reply)
    except Exception as e:
        print(e)
        msg.body("AI thoda busy hai, 1 min baad try karo 🙏")

    return str(resp)

if __name__ == "__main__":
    app.run()
