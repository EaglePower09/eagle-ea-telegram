from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Telegram bot credentials
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
        response = requests.post(url, data=payload)
        print(f"Telegram response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Error sending Telegram message: {e}")

@app.route('/')
def home():
    return jsonify({"status": "Eagle EA Telegram Bot is live"})

@app.route('/send', methods=['POST'])
def send():
    try:
        data = request.get_json()
        required = ['time', 'symbol', 'mode', 'session', 'confidence', 'entry', 'tp', 'sl']
        if not all(field in data for field in required):
            return jsonify({"error": "Missing fields"}), 400

        # Format signal
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
        return jsonify({"status": "Signal sent"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render uses this port
    app.run(host='0.0.0.0', port=port)
