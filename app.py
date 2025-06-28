from flask import Flask, jsonify
import requests

app = Flask(__name__)

# === Your Telegram Bot Details ===
TELEGRAM_BOT_TOKEN = '7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE'
TELEGRAM_CHAT_ID = '6105818531'

# === Your Live Signal API ===
SIGNAL_API_URL = 'https://eagle-ea-api.onrender.com/'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=payload)
        print(f"✅ Sent to Telegram: {response.status_code}")
    except Exception as e:
        print(f"❌ Telegram Error: {e}")

@app.route('/')
def home():
    return jsonify({"status": "✅ Eagle EA Telegram Bot is running."})

@app.route('/send', methods=['GET'])
def send_signal():
    try:
        response = requests.get(SIGNAL_API_URL)
        signal = response.json()

        if signal['mode'] != 'Sniper':
            return jsonify({"status": "Skipped – Not Sniper Mode"}), 200

        message = f"""📡 *Eagle EA Scalper Signal (Sniper)*

🕒 Time: {signal['time']}
💱 Pair: {signal['pair']}
📈 Direction: {signal['direction']}
🎯 Mode: {signal['mode']}
📊 Session: {signal['session']}
⚡ Confidence: {signal['confidence']}

✅ Result: {signal['result']}"""

        send_telegram_message(message)
        return jsonify({"status": "Sniper Signal Sent"}), 200

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": "Failed to fetch or send signal"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
