import datetime
import email
import imaplib
import mailbox


EMAIL_ACCOUNT = "mail_Id"
PASSWORD = "password"
sender_email ='sender_Mail_id'
subject_text='subject_to_Filter'
mail = imaplib.IMAP4_SSL('imap.secureserver.net')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
mail.select('inbox')
result, data = mail.uid('search', None, "ALL") # (ALL/UNSEEN)
i = len(data[0].split())
list=[]
for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # result, email_data = conn.store(num,'-FLAGS','\\Seen') 
    # this might work to set flag to seen, if it doesn't already
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('ISO-8859-1')
    email_message = email.message_from_string(raw_email_string)

    # Header Details
    date_tuple = email.utils.parsedate_tz(email_message['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y ")))
    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
    #email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
   
    if  subject_text in subject :
    # Body details
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                body_new=(body.decode('ISO-8859-1')).replace('IBM India is not accepting any proposals for this requisition.','').replace('Reason: [Other] CSA Cancelled','').replace(',','').replace('Dear LYNCIS TECHNOLOGIES INDIA PVT LTD','' ).replace('    ','').replace('     ','').replace('A new requisition has been posted by IBM India','').replace('IBM India has cancelled this requisition','').replace('Requisition ID','').replace('Requisition Name','').replace('Requisition Reference','').replace('Project Name','').replace('<p>','').replace('</p>','').replace('<br>','').replace('&nbsp;','').replace('<P>','').replace('<BR>','').replace('</P>','').replace('\n','')
                body_new=body_new.replace('Location:','')
                body_new=body_new.replace('  ','')
                body_new=body_new.replace('\t','')
                body_new=body_new.replace('\r','')
                print(body_new)
                print(local_message_date)
                file_name = "email8.txt"
                output_file = open(file_name, 'a')
                #list.append((body.decode('windows-1252')))
                #print(list)
                output_file.write(local_message_date)
            
                output_file.write(body_new)
                output_file.write('\n')
                #output_file.write("Date: %s\nBody: \n\n%s" %(local_message_date, body.decode('ISO-8859-1')))
                output_file.close()
            else:
                continue
