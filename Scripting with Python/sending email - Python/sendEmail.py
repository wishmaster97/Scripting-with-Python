import smtplib
from email.message import EmailMessage
from getpass import getpass

email = EmailMessage()
email['from'] = 'Abhijeet Tedle'
email['to'] = 't.anurag002@gmail.com'
email['subject'] = "Checking wither this works or not"

email.set_content("I am Python Master")

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    user_id= input("Enter Email ID : ")
    password = getpass("Enter Password : ")
    smtp.login(user_id, password)
    smtp.send_message(email)
    print("All good, Email sent succedssfully")