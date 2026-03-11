import schedule
import time
from message_sender import send_whatsapp_message


def start_scheduler():
    schedule.every().day.at("18:30").do(send_whatsapp_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
