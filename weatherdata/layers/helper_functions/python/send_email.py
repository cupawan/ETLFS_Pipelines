import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from boto3_toolkit import Boto3Utils

class EmailWithPython:
    def __init__(self,is_html = False):
        self.is_html = is_html
        self.config = Boto3Utils().get_secret(secret_name="WeatherPipelineSecrets")

    def send_email(self, send_to, subject, email_body):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config["BULLETIN_EMAIL_ADDRESS"]
            msg['To'] = send_to
            today_date = datetime.now().strftime('%A, %d %b %Y')
            msg['Subject'] = f"{today_date} {subject}"
            msg.attach(MIMEText(email_body, 'html'))        
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(self.config['BULLETIN_EMAIL_ADDRESS'],self.config['BULLET_EMAIL_ADDRESS_APP_PASSWORD'] )
            s.sendmail(self.config['BULLETIN_EMAIL_ADDRESS'], send_to, msg.as_string())
            s.quit()
            return {'status': 'success'}
        except Exception as e:
            print(f"Can not send email: {e}")
            return {'status': 'failed', 'reason' : str(e)}