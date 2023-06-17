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

message["Subject"] = "제목입니다."
message["From"] = "jklo0220@gmail.com"
message["To"] = "jy02_20@naver.com"
message.set_content("테스트 메일입니다.")


with open("miami.jpeg", "rb") as image:
	image_file = image.read()

image_type = imghdr.what("miami", image_file)
print(image_type)
message.add_attachment(image_file, maintype='image', subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("jklo0220@gmail.com", "ufcwdfzmksmmahpw")

sendEmail(message["To"])

smtp.quit()

