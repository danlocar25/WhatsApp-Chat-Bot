# netlify-functions/whatsapp_chat_bot.py

import json
import requests
from app import create_app
from config import Config

# Initialize the Flask app, but don't run it (Netlify will handle the function execution)
app = create_app()

def handler(event, context):
    """
    The handler function is called when a request is made to the serverless function.
    It processes the incoming request (event), and handles messaging events for WhatsApp.
    """
    try:
        # Parse the incoming JSON body
        data = json.loads(event['body'])

        # Loop through entries and messaging events to process the messages
        for entry in data.get('entry', []):
            for messaging_event in entry.get('messaging', []):
                if 'message' in messaging_event:
                    phone_number = messaging_event['sender']['id']
                    text = messaging_event['message']['text']
                    send_message(phone_number, text)

        # Return a success response after processing
        return {
            'statusCode': 200,
            'body': json.dumps({'status': 'success', 'message': 'Messages processed successfully'})
        }
    except Exception as e:
        # Return an error response if something goes wrong
        return {
            'statusCode': 500,
            'body': json.dumps({'status': 'error', 'message': str(e)})
        }

def send_message(phone_number, message):
    """
    This function sends a WhatsApp message using the Facebook Graph API.
    """
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
