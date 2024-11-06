import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
    WHATSAPP_ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
    PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
