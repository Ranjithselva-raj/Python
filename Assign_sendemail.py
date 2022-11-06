#write a function which will be able to send a mail to anyone
def email():
    """This function will send email from your gmail acc to anyone but ensure you give the input when you executing """
    import os
    from email.message import EmailMessage
    import ssl
    import smtplib

    email_sender =input("Enter your email ID: ")
    email_pass = input("Enter your 16 digit generated password: ") #Ensure your 2 step verification on and generate 16-digit password
    email_receiver = input("Enter receiver email ID: ")

    subject = input("Enter Subject: ")

    body = input("Enter Body of Email: ")

    msg=EmailMessage()

    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg.set_content(body)


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(email_sender,email_pass)
        smtp.sendmail(email_sender,email_receiver,msg.as_string())