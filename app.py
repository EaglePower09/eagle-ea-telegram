from flask import Flask, jsonify
import random
import requests

app = Flask(__name__)

# === Telegram Bot Setup ===
BOT_TOKEN = 'YOUR_BOT_TOKEN'  # 🔁 Replace with your Telegram bot token
CHAT_ID = 'YOUR_CHAT_ID'      # 🔁 Replace with your Telegram chat ID

# === Signal Generator Function ===
def generate_signal():
    pairs = ['XAUUSD', 'NAS100', 'US30', 'GER40', 'EURUSD', 'USDJPY',
             'GBPUSD', 'GBPAUD', 'GBPJPY', 'AUDCAD', 'USDCHF', 'NZDUSD']
    directions = ['Buy', 'Sell']
    sessions = ['Asian', 'London', 'New York']
    modes = ['Sniper', 'Normal', 'Aggressive']
    
    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "session": random.choice(sessions),
        "mode": random.choice(modes),
        "confidence": f"{random.randint(70, 95)}%"
    }
    return signal

# === Send Signal to Telegram ===
def send_to_telegram(signal):
    text = (
        f"📡 *Eagle EA Scalper Signal*\n"
        f"Pair: {signal['pair']}"
