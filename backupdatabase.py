import ftplib
import email
import smtplib
import ssl
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def file_upload():
    session = ftplib.FTP('ftp.test.gr','test@test.gr','test)')
    session.cwd('test') # specific folder on ftp server
    file = open('test.bak','rb')                  
    session.storbinary('STOR test.bak', file)     
    file.close()                                
    session.quit()

def send_email():
    now = datetime.datetime.now()
    d = now.strftime("%d_%m_%Y")
    subject = "Backup Amvrosia" + "-" + d
    body = "Amvrosia Backup test"
    sender_email = "test@test.gr"
    receiver_email = "test@test.gr"
    password = "test"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("test", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

    
    
def main():
    file_upload()
    send_email()

if __name__ == "__main__":
    main()
