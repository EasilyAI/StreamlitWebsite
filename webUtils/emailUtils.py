from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from google.cloud import secretmanager
import json
import smtplib
import os   
import re

import project_path

def validate_email(email):
    # Simple regex for email validation
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def load_config(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def get_recipient_email_contacts():
    load_dotenv()
    return os.getenv('RECIPIENT_EMAIL_CONTACTS')

def load_smtp_email_credentials():
    load_dotenv()
    return {
        'smtp_user' : os.getenv('SMTP_USER'),
        'smtp_password' : os.getenv('SMTP_PASS')
        }

def load_smtp_email_credentials_from_google_secret():
    load_dotenv()
    client = secretmanager.SecretManagerServiceClient()
    
    project_id = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
    secret_id = os.getenv('GOOGLE_CLOUD_SECRET_ID')
    version_id = "latest"

    name = f"projects/{project_id}/secrets/{secret_id}/versions/{version_id}"
    response = client.access_secret_version(request={"name": name})

    secret_payload = response.payload.data.decode("UTF-8")
    return json.loads(secret_payload)


def send_email_smtp(subject, body_dict, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Use 465 for SSL

    smtp_config = load_smtp_email_credentials()
    smtp_user = smtp_config['smtp_user']
    smtp_password = smtp_config['smtp_password']

    # Create the email message
    message = MIMEMultipart()
    message['From'] = smtp_user
    message['To'] = to_email
    message['Subject'] = subject
    
    body = json.dumps(body_dict, indent=4)
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_user, smtp_password)
            server.send_message(message)
        return True
    except Exception as e:
        return False