import pywhatkit as kit
from config import PHONE_NUMBER, MESSAGE, SEND_HOUR, SEND_MINUTE


def send_whatsapp_message():
    try:
        print("Sending WhatsApp message...")
        kit.sendwhatmsg(PHONE_NUMBER, MESSAGE, SEND_HOUR, SEND_MINUTE)
        print("Message scheduled successfully!")
    except Exception as e:
        print("Error sending message:", e)
