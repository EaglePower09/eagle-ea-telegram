from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# ✅ Your correct bot token and chat ID
TELEGRAM_BOT_TOKEN = '7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE'
TELEGRAM_CHAT_ID = '6105818531'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE}/sendMessage'
    payload = {
        'chat_id': 6105818531,
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

@app.route('/signal', methods=['POST'])
def signal():
    try:
        data = request.get_json()

        # Validate required fields
        required_fields = ['time', 'symbol', 'mode', 'session', 'confidence', 'entry', 'tp', 'sl']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

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
        return jsonify({"status": "Signal sent to Telegram"}), 200

    except Exception as e:
        print(f"Error in /signal: {e}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
