import smtplib
import os
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

try:
    import requests
except ImportError:
    os.system('apt-get install python3')
    os.system('pip3 install requests')
#from  dot_env import load_dotenv

# Download the CSV file from the URL
url = "http://agridata.tn/dataset/4bb3d668-6c9b-4072-ad56-1eb9119091af/resource/8d70196c-a95e-4a04-9c61-8144b4b60a18/download/barrages.csv"
response = requests.get(url)
#current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
#envars = current_dir /".env"
#load_dotenv(envars)

sender_email="barometertnbybig4partners@gmail.com"        #os.environ.get("EMAIL")
password="mvnezctznpbwziru"            #os.environ.get("PASSWORD")



# Download the CSV file from the URL
#url = "http://agridata.tn/dataset/4bb3d668-6c9b-4072-ad56-1eb9119091af/resource/8d70196c-a95e-4a04-9c61-8144b4b60a18/download/barrages.csv"
#response = requests.get(url)
url="http://agridata.tn/dataset/4bb3d668-6c9b-4072-ad56-1eb9119091af/resource/8d70196c-a95e-4a04-9c61-8144b4b60a18/download/barrages.csv"
response = requests.get(url)
# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = sender_email
msg["Subject"] = "Donnees Situation des barrages"

# Attach the CSV file to the email
part = MIMEBase("application", "octet-stream")
part.set_payload((response.content))
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename=barrages.csv")
msg.attach(part)

# Send the email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender_email, password)
    smtp.sendmail(sender_email,sender_email, msg.as_string())
    smtp.quit()  