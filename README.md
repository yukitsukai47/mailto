# Send mail using python
This program is a python program for sending mail.

In addition,You can also spoof mail headers,not just send mail.

# Requirement
* python3.7.4
* Email account(Gmail,yahoo,outlook, etc...)

However, when using Gmail, it is necessary to disable 2-step verification etc. from Gmail settings.

# How to use
1. Please write your account information.
```
   FROM_ADDRESS = 'Own account'

   MY_PASSWORD = 'Own password'
```
2. Edit the smtplib.SMTP source code in def send ().
Here you decide whether to use Gmail or Outlook.

*Gmail by default

You can also select Outlook by removing 「#」
```
def send(from_addr, to_addrs, msg):
#   if use gmail SMTP
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
#   if use outlook SMTP
#   smtpobj = smtplib.SMTP('smtp.office365.com', 587)
```

3. Email subject and body read external file and compose email.
So please prepare the subject.txt and body.txt of the content you want to write before running the program.

4. Next is program execution.
```
python3 mailto.py
```

5. First, specify who you want to send mail to.
Then answer yes or no to disguise the mail header.
If impersonating, enter the name used for impersonation.

6. You can then choose which files to attach. If you have an attachment, please select it.

7. The email will be sent to you.

![program](https://user-images.githubusercontent.com/52772923/64474926-7cd38200-d1b6-11e9-80c3-e563a77aa0fe.png)

8. Sending... Complete!

![mail](https://user-images.githubusercontent.com/52772923/64474933-970d6000-d1b6-11e9-827d-220ce9605dcc.png)