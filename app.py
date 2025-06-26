import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = '7959778482:AAFgqgf01UFX4QCKkYuNBiT4jt557m7LQuE'
TELEGRAM_CHAT_ID = '7959778482'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    return response.json()

@app.route('/signal', methods=['POST'])
def send_signal():
    data = request.get_json()

    signal_text = f"""📡 *Eagle EA Scalper Signal*

🕒 Time: {data.get('time')}
💱 Pair: {data.get('symbol')}
🎯 Mode: {data.get('mode')}
📊 Session: {data.get('session')}
⚡ Confidence: {data.get('confidence')}%

📍 Entry: {data.get('entry')}
🎯 TP: {data.get('tp')}
🛑 SL: {data.get('sl')}"""

    result = send_telegram_message(signal_text)

    return jsonify({'status': 'sent', 'telegram_result': result})

if __name__ == '__main__':
    app.run()
