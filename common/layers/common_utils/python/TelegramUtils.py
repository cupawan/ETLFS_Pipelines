import os
import requests
from Boto3Toolkit import Boto3Utils

class TelegramMessage:
    def __init__(self):
        self.token = os.environ["TelegramBotToken"].replace("=",":")
        self.audio_url = f"https://api.telegram.org/bot{self.token}/sendAudio"
        self.document_url = f"https://api.telegram.org/bot{self.token}/sendDocument"
        self.image_url = f"https://api.telegram.org/bot{self.token}/sendPhoto"
        self.plain_url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        self.get_updates_url = f"https://api.telegram.org/bot{self.token}/getUpdates"
        self.get_me = f"https://api.telegram.org/bot{self.token}/getMe"

    def send_plain_message(self, text, chat_id):
        url = self.plain_url
        data_payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
        files_payload = None
        return self._send_message(url, data_payload, files_payload)

    def send_audio_message(self, audio_file_path, chat_id, caption=None):
        url = self.audio_url
        data_payload = {'chat_id': chat_id, 'caption': caption}
        files_payload = {'audio': open(audio_file_path, 'rb')}
        return self._send_message(url, data_payload, files_payload)

    def send_document_message(self, document_file_path, chat_id, caption=None):
        url = self.document_url
        data_payload = {'chat_id': chat_id, 'caption': caption}
        files_payload = {'document': open(document_file_path, 'rb')}
        return self._send_message(url, data_payload, files_payload)

    def send_image_message(self, image_file_path, chat_id, caption=None):
        url = self.image_url
        data_payload = {'chat_id': chat_id, 'caption': caption}
        files_payload = {'photo': open(image_file_path, 'rb')}
        return self._send_message(url, data_payload, files_payload)

    def _send_message(self, url, data_payload, files_payload):
        response = requests.post(url, data=data_payload, files=files_payload)
        response.raise_for_status()
        return True
    
    def get_updates(self, timeout = None, limit = None, offset = None, allowed_updates = None):
        params = {'timeout': timeout, 'limit': limit, 'offset' : offset, 'allowed_updates': allowed_updates}
        response = requests.get(url = self.get_updates_url, params=params)
        response.raise_for_status()
