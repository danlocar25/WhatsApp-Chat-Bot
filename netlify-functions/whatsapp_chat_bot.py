import json
import requests
from app import create_app
from config import Config

app = create_app()

def handler(event, context):
    data = json.loads(event['body'])
    
    for entry in data['entry']:
        for messaging_event in entry['messaging']:
            if 'message' in messaging_event:
                phone_number = messaging_event['sender']['id']
                text = messaging_event['message']['text']
                send_message(phone_number, text)
    
    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }

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
