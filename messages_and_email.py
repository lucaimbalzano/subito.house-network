import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from time import strftime, gmtime
from email.mime.text import MIMEText
from scraper import *

def sent_working_email():
    df2 = scraping_web_prices_day_by_day()
    name = "Report_"+ str(dt.datetime.today().date().strftime("%d-%m"))+".xlsx"
    df2.to_excel(name, encoding="utf-8")
    msg = MIMEMultipart()
    msg["From"] = "lucaimbalzano@gmail.com"
    while True:
        print("## started cycle - inside loop ##")
        ora = dt.datetime.now().time().hour
        minuti = dt.datetime.now().time().minute
        # if dt.time(ora, minuti) == dt.time(20, 45) or dt.time(ora, minuti) == dt.time(20, 45):
        sent_working_email()
    msg["To"] = "lucaimbalzano@gmail.it"
    msg["Subject"] = "Daily Report Apartments - "+str(dt.datetime.today().date().strftime("%d-%m"))
    row = len(df2)
    body= f"""This email is proudly generated automatically via Python.
    Every day at 6pm you will receive this excel file containing all the apartments that have been uploaded in the last 24 hours.
    Today {row} new apartments have been uploaded\n\nLuca Imbalzano"""
    body = MIMEText(body)  # convert the body to a MIME compatible string
    msg.attach(body)  # attach it to your main message
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(name, "rb").read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", "attachment", filename=name)  # or
    msg.attach(part)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("lucaimbalzano@gmail.com", os.environ.get("GMAIL_LUCA"))
        smtp.send_message(msg)

def send_wrong_email():
    msg = MIMEMultipart()
    msg["From"] = "lucaimbalzano@gmail.com"
    msg["To"] = "lucaimbalzano@gmail.com"
    msg["Subject"] = "Error occured at: " + str(dt.datetime.now())[0:16]
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("lucaimbalzano@gmail.com", os.environ.get("GMAIL_LUCA"))
        smtp.send_message(msg)