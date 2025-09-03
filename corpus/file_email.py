import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Yagmail is another less common import
import yagmail

# Mailer is another less common import
from mailer import Mailer

mailer = Mailer(
    smtp={'host': 'smtp.gmail.com', 'port': 587, 'timeout': 10},
    send_from='your_email@gmail.com',
    send_to=['recipient_email@gmail.com'],
    subject='Test Email',
    body='This is a test email sent from Mailer!'
)
mailer.send()


yag = yagmail.SMTP('your_email@gmail.com', 'your_password')
yag.send(to='recipient_email@gmail.com', subject='Test Email', contents='This is a test email sent from Yagmail!')


def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Use TLS
            server.login(sender_email, sender_password)  # Log in to your email account
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Email details
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"        # Replace with your email password
    recipient_email = "recipient_email@gmail.com"  # Replace with recipient's email
    subject = "Test Email"
    body = "This is a test email sent from Python!"

    send_email(sender_email, sender_password, recipient_email, subject, body)
