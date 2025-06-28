from flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your actual bot token and chat ID
TELEGRAM_BOT_TOKEN = '7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE'
TELEGRAM_CHAT_ID = '6105818531'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        requests.post(url, data=payload)
    except Exception:
        pass  # Keep silent for cron job

@app.route('/')
def home():
    return "Eagle EA Telegram Bot is live"

@app.route('/send', methods=['POST'])
def send():
    try:
        data = request.get_json()

        required = ['time', 'symbol', 'mode', 'session', 'confidence', 'entry', 'tp', 'sl']
        if not all(field in data for field in required):
            return "Missing fields", 400

        message = f"""📡 *Eagle EA Scalper Signal*

🕒 Time: {data['time']}
💱 Pair: {data['symbol']}
🎯 Mode: {data['mode']}
📊 Session: {data['session']}
⚡ Confidence: {data['confidence']}%

📍 Entry: {data['entry']}
🎯 TP: {data['tp']}
🛑 SL: {data['sl']}"""

        send_telegram_message(message)
        return "OK", 200  # ⬅ Small response for cron-job.org
    except Exception:
        return "Internal Error", 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Get PORT from environment
    app.run(host='0.0.0.0', port=port)
