from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.models import Email
from scripts.constants.email_constants import email_obj

app = FastAPI()


def send_email(email: Email):
    # Set up the email details
    sender_email = email_obj.sender_email
    sender_password = email_obj.sender_password
    receiver_email = email.rec_email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = email.subject

    # Add the body to the email
    message.attach(MIMEText(email.body, "plain"))

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
