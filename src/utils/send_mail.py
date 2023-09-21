import smtplib
def send_mail():
    s = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
 
    # start TLS for security
    s.ehlo()
 
    # Authentication
    s.login("hrevit@gmail.com", "Egbdfxk!8595")
 
    # message to be sent
    message = "Message_you_need_to_send"
 
    # sending the mail
    s.sendmail("hrevit@gmail.com", "hrevit@gmail.com", message)
 
    # terminating the session
    s.quit()