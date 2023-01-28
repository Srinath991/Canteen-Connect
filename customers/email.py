import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("991techsri@gmail.com", "zyuqyaghmnneezra")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("991techsri@gmail.com", "srinath2003128991gmail", message)

# terminating the session
s.quit()
