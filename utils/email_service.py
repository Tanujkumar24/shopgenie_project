import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email_report(to_email, query, comparison_result):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = os.getenv("SMTP_USER")
    smtp_pass = os.getenv("SMTP_PASSWORD")

    body = f"Product Comparison Results for: {query}\n\n{comparison_result}"
    message = MIMEText(body)
    message["Subject"] = f"ShopGenie Product Comparison - {query}"
    message["From"] = smtp_user
    message["To"] = to_email

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_pass)
    server.sendmail(smtp_user, to_email, message.as_string())
    server.quit()