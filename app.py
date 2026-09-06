from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=['POST'])
def whatsapp_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()

    if 'hi' in incoming_msg or 'hello' in incoming_msg:
        msg.body("Hello! 🤖 Mai 24x7 Online Pro Bot hu. PC band bhi ho to chalunga! 😆")
    else:
        msg.body(f"Tune bheja: {incoming_msg} \nBot online hai ✅")

    return str(resp)

@app.route("/", methods=['GET'])
def home():
    return "Bot is running 24x7!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)