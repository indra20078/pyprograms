import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('primemember248@gmail.com','123qwe@456rty')
server.sendmail('primember248@gmail.com',
                 'indradhanushhs@gmail.com',
                  'hi how are you')

server.quit()