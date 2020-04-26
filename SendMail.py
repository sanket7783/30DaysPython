import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os
import sys

# Use environment variables for email and password for more security
# To Store Email and password as environment variables use following command
# 'export Email="YourEmailId"'
# 'export Password="YourPassword"'
username=os.environ['Email']
password=os.environ['Password']

def send_mail(text='Email Body', subject='Subject',from_email='hambirsanket7783@gmail.com',to_emails=None):
    # Check if the to_emails is list or not
    assert isinstance(to_emails,list)
    
    msg=MIMEMultipart('alternative')
    msg['From']=from_email
    msg['To']=",".join(to_emails)
    msg['Subject']=subject

    txt_part=MIMEText(text,'plain')
    msg.attach(txt_part)

    html_part=MIMEText('<h1>This is working</h1>','html')
    msg.attach(html_part)

    msg_str=msg.as_string()

    # login
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)


    server.quit()


    # with smtplib.SMTP() as server:
    #     server.login()
    #     pass



if __name__=='__main__':
    print(sys.argv)
    name="Unknown"
    if len(sys.argv)>1:
        name=sys.argv[1]
    email=None
    if len(sys.argv)>2:
        email=sys.argv[2]
    response=send_mail(to_emails=[email])
    print(response)
