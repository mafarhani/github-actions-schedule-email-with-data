
import smtplib
import requests
import os
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from  dotenv import load_dotenv

# Download the CSV file from the URL
url = "http://agridata.tn/dataset/4bb3d668-6c9b-4072-ad56-1eb9119091af/resource/8d70196c-a95e-4a04-9c61-8144b4b60a18/download/barrages.csv"
response = requests.get(url)
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir /".env"
load_dotenv(envars)

sender_email=os.getenv("EMAIL")
password=os.getenv("PASSWORD")



# Download the CSV file from the URL
#url = "http://agridata.tn/dataset/4bb3d668-6c9b-4072-ad56-1eb9119091af/resource/8d70196c-a95e-4a04-9c61-8144b4b60a18/download/barrages.csv"
#response = requests.get(url)
url="https://data.unhcr.org/population/get/timeseries?export=csv&widget_id=369680&geo_id=656&sv_id=11&population_group=4908&frequency=day&fromDate=1900-01-01"
response = requests.get(url)
# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = sender_email
msg["Subject"] = "UNHCR DATA ya FANNEN"

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
    smtp.sendmail(sender_email,sender_email, msg.as_string())
    smtp.quit()  