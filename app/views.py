from flask import request, jsonify
import requests
from app import create_app
from config import Config

# Import the app instance created by create_app in run.py
app = create_app()  # This line was previously causing the error

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Webhook verification for Meta
        if request.args.get('hub.mode') == 'subscribe' and request.args.get('hub.challenge'):
            if request.args.get('hub.verify_token') == Config.VERIFY_TOKEN:
                return request.args['hub.challenge'], 200
            return 'Verification token mismatch', 403
        return 'Invalid request', 400
    
    if request.method == 'POST':
        # Process the incoming WhatsApp message
        data = request.get_json()

        # Handle incoming message (you can add more logic here)
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if 'message' in messaging_event:
                    phone_number = messaging_event['sender']['id']
                    text = messaging_event['message']['text']
                    send_message(phone_number, text)
        return 'OK', 200


def send_message(phone_number, message):
    url = f'https://graph.facebook.com/v15.0/{Config.PHONE_NUMBER_ID}/messages'
    headers = {
        'Authorization': f'Bearer {Config.WHATSAPP_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        'messaging_product': 'whatsapp',
        'to': phone_number,
        'text': {'body': message}
    }
    response = requests.post(url, json=data, headers=headers)
    print(f"Sent message to {phone_number}: {response.status_code}, {response.text}")
