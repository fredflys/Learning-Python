import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def email(email_list, content, subject="来自抽屉的问候，递上您需要的CODE"):  # email_list邮件列表，content邮件内容，subject：发送标题
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = formataddr(["抽屉测试版", 'xyf220@126.com'])
    server = smtplib.SMTP("smtp.126.com", 25)
    # 邮箱引擎
    server.login("xyf220@126.com", "x9zv4vemj7")  # 邮箱名，密码
    server.sendmail('xyf220@126.com', email_list, msg.as_string())
    server.quit()