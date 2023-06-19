import smtplib
from email.message import EmailMessage
import imghdr
import re

def sendEmail(addr):
	reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
	if bool(re.match(reg, addr)):
		smtp.send_message(message)
		print("메일 발송 성공")
	else:
		print("유효한 이메일 주소가 아닙니다.")


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()

message["Subject"] = "현지니"
message["From"] = "jklo0220@gmail.com"
message["To"] = "chlguswls241@naver.com"
message.set_content("이거봐라")


with open("IMG_5092.jpeg", "rb") as image:
	image_file = image.read()

image_type = imghdr.what("miami", image_file)
print(image_type)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("jklo0220@gmail.com", "ufcwdfzmksmmahpw")

sendEmail(message["To"])

smtp.quit()

