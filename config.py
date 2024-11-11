import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")  # Token for webhook verification
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")  # Your WhatsApp Access Token
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")  # Your Phone Number ID for WhatsApp API
