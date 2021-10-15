def sendMail(orderNo,data):
    ## Compiling a Email
    order_no="OA0011133"
    date="10-2-2020"
    mail="titancart1122@gmail.com"
    passW="Tropic88"
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    sender_email =mail
    receiver_email = "i170014@nu.edu.pk"

    password = passW
    message = MIMEMultipart("alternative")
    message["Subject"] = "Titan Cart Order Confirmation :"+order_no
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    text = """\
    Dear Custome {str1}:
    How are you?
    Your Order : {str2} is Confirmed.
    It will be delivered to your doorstep within 5 working days.
    If you have any querries, please contact us at titancart1122@gmail.com or 03481512600.
    Here is Your Order:
    {str3}
    """.format(str1=reciever_LastName,str2=order_no,str3=data)
    html = """\
    <html>
    <body>
        <p>Dear Customer {str1}:<br>
        How are you?<br>
        Your Order : {str2}  From 
        <a href="http://127.0.0.1:8000/">Titan Cart</a> 
        is Confirmed.
        It will be delivered to your doorstep within 5 working days.
        If you have any querries, please contact us at titancart1122@gmail.com or 03481512600.
        Here is Your Order:
        {str3}
        </p>
    </body>
    </html>
    """.format(str1=reciever_LastName,str2=order_no,str3=data)

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
def sendAttachMain(orderNo,fileanme):
    import smtplib 
    from email.mime.multipart import MIMEMultipart 
    from email.mime.text import MIMEText 
    from email.mime.base import MIMEBase 
    from email import encoders     
    fromaddr = "titancart1122@gmail.com"
    toaddr = "i170014@nu.edu.pk"
    reciever_LastName=" XYZ "
    msg = MIMEMultipart()    
    msg['From'] = fromaddr   
    msg['To'] = toaddr   
    msg['Subject'] = "Titan Cart Order Confirmation :"+orderNo
    body = """\
    Dear Customer {str1}:
    How are you?
    Your Order : {str2} is Confirmed.
    It will be delivered to your doorstep within 5 working days.
    If you have any querries, please contact us at titancart1122@gmail.com or 03481512600.
    *Attached:: is the reciept that you will need to show to the delivery Guy
    """.format(str1=reciever_LastName,str2=orderNo) 
    msg.attach(MIMEText(body, 'plain'))  
    filename = fileanme
    attachment = open("Orders/{str1}".format(str1=filename), "rb") 
    p = MIMEBase('application', 'octet-stream')  
    p.set_payload((attachment).read()) 
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(fromaddr, "Tropic88") 
    text = msg.as_string() 
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()       