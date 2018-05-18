import email
import imaplib


EMAIL_ACCOUNT = "Mail_id"
PASSWORD = "password"
sender_email ='sender_domain'
subject_line7="Subject_to_Filter"
mail = imaplib.IMAP4_SSL('imap.secureserver.net')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
mail.select('inbox')
result, data = mail.uid('search', None, "ALL")
i = len(data[0].split())

#for x in range(20,30): # for some range
for x in range(i):
    email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', email_uid, '(RFC822)')
    
    raw_email = email_data[0][1]
    
    raw_email_string = raw_email.decode('ISO-8859-1')
    
    email_message = email.message_from_string(raw_email_string)

    email_from=email_message['FROM']
    subject=email_message['Subject']
    local_message_date=email_message['Date']
    if subject.startswith('CSA Request'):
       if  sender_email in email_from :
           if subject_line7 not in subject:
               subject=subject.replace(' /',';')
               subject=subject.replace('Synon2E; Cool2E','Synon2E/Cool2E')
               subject=subject.replace('\n','')
               subject=subject.replace('\r','')
               subject=subject.replace('CSA Request ','')
               subject=subject.replace(' of type RFQ','')
               subject=subject.replace('of type MOP ','')
               subject=subject.replace('Hive is Must ::','')
               print(subject)
               print(local_message_date)
               file_name = "Subject18.txt"
               output_file = open(file_name, 'a')
               output_file.write(str(x))
               output_file.write(';')
               output_file.write(email_from)
               output_file.write(';')
               output_file.write(subject)
               output_file.write(';')
               output_file.write(local_message_date )
               output_file.write('\n')
               output_file.close()
                                            
    else:
        continue
