import os
from Execute import Helper
from EmailUtils import SendEmail

sub = "Strava Run Statistics"

def LambdaHandler(event, context):
    help = Helper()
    data = help.getLatestActivity()
    msg = help.formatMessage(data = data)
    SendEmail(is_html=True).send_email(send_to = os.environ["RecEmail"], subject = sub, email_body = msg)