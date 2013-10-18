__author__ = 'Burak Tekin'
# Department of Computer Science
# Sending Email Using SMTP Authentication


from smtplib import SMTPException, SMTP


# ***************** E-MAIL CONFIGURATION ****************
HostName = '<YOUR HOST NAME>'
Port = 'SMTP PORT'
UserName = 'Your Username'
Password = 'Your Password'
debuglevel = 0
# ***************** END of CONFIGURATION ****************


# -- SMTP Connection --
smtp = SMTP()
smtp.set_debuglevel(debuglevel)
smtp.connect(HostName, Port)
smtp.login(UserName, Password)
# -- End of Connection


# -- Email Requirements --

# -- Sender and Recipients
From = "<Name to Display> <your@domain>"
To = "Recipients"

# -- Body --
Subject = "Your Subject"
Text = "Your main message into body part"
Message = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (From, To, Subject, Text)

# -- Send Email --
try:
    smtp.sendmail(From, To, Message)
except SMTPException:
    print "An error occured while sending mail"

smtp.quit()
