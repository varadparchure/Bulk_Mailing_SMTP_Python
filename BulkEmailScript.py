import csv, smtplib
import settings

# email message consists of headers and a payload (which is also referred to as the content)
from email.message import EmailMessage 

# MIMEMultipart is for saying "I have more than one part", and then listing the parts - For attachments
from email.mime.multipart import MIMEMultipart

# MIMEText extends the format of email messages to support text in character sets other than ASCI
from email.mime.text import MIMEText

# MIMEBase is provided primarily as a convenient base class for more specific MIME-aware subclasses
from email.mime.base import MIMEBase  

#encoders usually extract the payload, encode it, and reset the payload to a newly encoded value.
from email import encoders


# ---------- Function To Send An Email ----------

def SendMail(subject,message):

    # ***
    # you can put email draft here too if its multiline:
    # message=''' Text Goes Here '''
       

    # Attachment Condition
    att=int(input("Do you want to send an attachment?\n Press 1 and Enter for Yes \n Press 0 and Enter for No: "))
    if(att==1):
        
        # MIMEMultipart is intermediate base class for MIME messages that are multipart
        msg2=MIMEMultipart()

        # MIMEText class is used to create MIME objects of major type text.
        msg2.attach(MIMEText(message,'plain'))

        # File which we want to send as an attachment
        filename='attachment.txt'
        attachment = open(filename,'rb') 

        # MIMEBase is base class for all the MIME-specific subclasses of Message.
        part=MIMEBase('application','octet-stream')

        # Set the entire message object’s payload to payload
        part.set_payload((attachment).read())

        # Encodes the payload into base64 form and sets the Content-Transfer-Encoding header to base64
        encoders.encode_base64(part)

        # Additional header parameters can be provided as keyword arguments i.e file name in this case. 
        part.add_header('Content-Disposition',"attachment;filename="+ filename)

        # Finally attach part to the email msg
        msg2.attach(part)

    #-----------------------------------------------------------------------------------------------------

    # For establishing the server with smtp gmail port number
    server =smtplib.SMTP('smtp.gmail.com',587)

    # Sent by an email server to identify itself when connecting to another email server
    server.ehlo()

    # Turn an existing insecure connection into a secure one.
    server.starttls()

    #Senders Username and Password
    server.login(settings.sender,settings.pwd)

    #Here is the CSV file Import----------------------------
    #Opening the CSV file which contains Names and Email id's
    with open("emaillist.csv") as file:

        # reader will contain the file data
        reader=csv.reader(file)

        # To skip the CSV header (name and email title) 
        next(reader)

        # For traversing the rows
        for name,addr in reader:

            # An email message consists of headers and a payload
            email=EmailMessage()
            email['From']=settings.sender
            email['To']=addr
            email['Subject']=subject

            # Attachment condition
            if(att==1):
                email.set_content(msg2)
            else:
                email.set_content(message)
                
            # Request the server to send the message (email object) 
            server.send_message(email)

            # Acknowledge 
            print(f'Sent to {name}' )

    server.close()


# ----------   Getting User and Email Draft Info   ----------

print("Enter your Email subject :")
subject=input()
print("Enter your Email Message :")
message=input()


# ----------   Calling sendmail function   ---------

SendMail(subject,message)

 


