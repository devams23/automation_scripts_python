import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email using Gmail's SMTP server.    

    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email
        
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error: {e}")


