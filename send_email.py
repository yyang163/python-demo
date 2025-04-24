import os
import smtplib
from email.mime.text import MIMEText


# from email_config import sectpass
def send_qqemail(sender_email, sender_password, rec_email, subject, message):
    msg = MIMEText(message,'plain','utf-8')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = rec_email
    # send_password='YKg3EgPAW93xw3ra'
    try:
        with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
            smtp.set_debuglevel(1)
            smtp.login(sender_email, sender_password)
            smtp.send_message(msg)
            smtp.quit()
            print("邮件发送完毕")
    except smtplib.SMTPException as e:
        print(f"发送失败{str(e)}")


def main():
    sender_email = '1635087188@qq.com'
    auth_code = os.getenv("MAIL_AUTH_CODE")
    to_email = '1635087188@qq.com'
    sub_msg = 'zhuti'
    txt = 'hello yc'
    send_qqemail(sender_email,auth_code, to_email, sub_msg, txt)


if __name__ == '__main__':

    main()


# import smtplib
# from email.mime.text import MIMEText
#
#
# def send_qqemail(sender_email, sender_password, rec_email, subject, message):
#     """
#     发送QQ邮件
#
#     参数:
#         sender_email: 发件人QQ邮箱
#         sender_password: QQ邮箱授权码(不是密码)
#         rec_email: 收件人邮箱
#         subject: 邮件主题
#         message: 邮件正文
#     """
#     # 创建邮件内容
#     msg = MIMEText(message, 'plain', 'utf-8')
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = rec_email
#
#     try:
#         # 使用SMTP_SSL连接QQ邮箱服务器(正确端口是465)
#         with smtplib.SMTP_SSL('smtp.qq.com', 465) as smtp:
#             smtp.login(sender_email, sender_password)
#             smtp.send_message(msg)
#             print("邮件发送成功")
#     except smtplib.SMTPException as e:
#         print(f"邮件发送失败: {str(e)}")
#
#
# def main():
#     # 注意: 实际使用时应该从安全的地方获取这些信息
#     sender_email = '1635087188@qq.com'  # 发件人QQ邮箱
#     auth_code = 'YKg3EgPAW93xw3ra'  # QQ邮箱授权码(注意保护)
#     to_email = '1041259750@qq.com'  # 收件人邮箱
#     subject = '测试邮件主题'  # 邮件主题
#     content = '你好，这是一封测试邮件!'  # 邮件内容
#
#     send_qqemail(sender_email, auth_code, to_email, subject, content)
#
#
# if __name__ == '__main__':
#     main()

# import telnetlib
# try:
#     telnetlib.Telnet('smtp.qq.com', 465, timeout=10)
#     print("端口可访问")
# except:
#     print("无法连接服务器")
# server = smtplib.SMTP_SSL('smtp.qq.com', 465)
# server.set_debuglevel(1)  # 显示详细调试信息