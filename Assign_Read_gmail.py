#write a function which will be able to read all the mails
import smtplib
import time
import imaplib
import email
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = 'enteryour@gmail.com'
FROM_PWD = 'enter password'
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993
imaplib._MAXLINE = 400000000

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')
        #key = 'FROM'                               #if you want to read from specific email
        #value = 'enter@gmail.com'
        data = mail.search(None, 'ALL') #key, value  #ALL
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    email_body=msg['body']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')
                    print ("body:")
                    for part in msg.walk():
                        #print(part.get_content_type())
                        if part.get_content_type() == 'text/plain':
                            print (part.get_payload())

    except Exception as e:
        traceback.print_exc()
        print(str(e))

read_email_from_gmail()
