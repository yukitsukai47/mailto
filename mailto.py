import smtplib
import email.utils
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

print("Who do you want to send email to?")
TO_ADDRESS = input()

# Enter your account information to use (For example gmail,outlook,etc...)
#FROM_ADDRESS = 'xxxxxxxx@gmail.com'
#MY_PASSWORD = 'xxxxxxxxxxxx'
FROM_ADDRESS = ''
MY_PASSWORD = ''

# Write the subject in subject.txt
# and read subject.txt
f = open('subject.txt', 'r')
SUBJECT = f.read()
f.close()

# Write the body in body.txt
# and read body.txt
f = open('body.txt', 'r')
BODY = f.read()
f.close()

print("Do you want to impersonate the sender?")
IMPERSONATE = FROM_ADDRESS
# CHOICE represents the choice of whether to impersonate the mail header.
CHOICE = ''
# Create dictionary for CHOICE
dic={'y':True, 'ye':True, 'yes':True, 'n':False, 'no':False}
# Repeat input until something in dic comes out.
while True:
    try:
        CHOICE = dic[input("[Y]es/[N]o? >>").lower()]
        break
    except:
        pass
    print("Error! Input again.")
# impersonate
if CHOICE == True:
    print("Please input impersonate name")
    IMPERSONATE = input()
elif CHOICE == False:
    IMPERSONATE = FROM_ADDRESS


print("Do you want to attach a file?")
CHOICE2 = ''
while True:
    try:
        CHOICE2 = dic[input("[Y]es/[N]o? >>").lower()]
        break
    except:
        pass
    print("Error! Input again.")
# Attach file
if CHOICE2 == True:
    print("Please input file name")
    PATH = "./" + input()
elif CHOICE2 == False:
    PATH = ''


# Create message
def create_message(from_addr, to_addr, subject, body, path):
    msg = MIMEMultipart()
    msg['Subject'] = subject

    if CHOICE  == True:
        msg['From'] = email.utils.formataddr((IMPERSONATE, from_addr))
    elif CHOICE == False:
        msg['From'] = from_addr
    
    msg['To'] = to_addr
    msg['Date'] = email.utils.formatdate()

    msg.attach(MIMEText(BODY))
    
    if CHOICE2 == True:
        path = PATH
        with open(path, "rb") as f:
            attach_file = MIMEApplication(
                f.read(),
                Name=basename(path)
        )
        attach_file['Content-Disposition'] = 'attachment; filename="%s"' % basename(path)
        msg.attach(attach_file)
    elif CHOICE2 == False:
        path = PATH

    return msg

# Connect to Google's SMTP Server
def send(from_addr, to_addrs, msg):
# if use gmail SMTP
#    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
# if use outlook SMTP
    smtpobj = smtplib.SMTP('smtp.office365.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS,MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    msg = create_message(FROM_ADDRESS, TO_ADDRESS, SUBJECT, BODY, PATH)
    print("Sending now...")
    send(FROM_ADDRESS, TO_ADDRESS, msg)
    print("The email has been successfully sent.")
