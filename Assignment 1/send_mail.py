 
 
#     Assignment - 1 | Zelthy - Hemant Kumar Lader (hemantlader@gmail.com)
# 
#               Input format:
#                    python -m send_mail 
#                    >Subject? <input text>
#                    >Body? <input text>
#                    >Recipient? <input email>
#                OUTPUT: 
#                    >Email Sent!
# ------------------------------------------------------------------            


import smtplib
from email.mime.text import MIMEText

fromEmail="hemanttest9@gmail.com"
fromEmailPassword="Test@123"

def sendEmail(emailData):
    messageBody = MIMEText(emailData['body'])
    messageBody['Subject'] = emailData['subject']
    toMailId = emailData['recipient']
    messageBody['From'] = fromEmail
    
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(fromEmail, fromEmailPassword)
        smtp.sendmail(fromEmail, toMailId, messageBody.as_string())
        smtp.quit()
        print(">Email sent!")
        
    except:
        print(">Error in connection")

emailData = {}

if __name__ == "__main__":
    
    print(">Subject? ", end="")
    emailData['subject'] = str(input()).capitalize()
    print(">Body? ", end="")
    emailData['body'] = str(input()).capitalize()
    print(">Recipient? ", end="")
    emailData['recipient'] = str(input()).capitalize()
    sendEmail(emailData)
    
    
    # Below code was for using this module as console program 
    
    
    # while(1):
    
    #     if len(emailData.keys()) == 3 :
    #         sendEmail(emailData)
    #         break
            
    #     print(">", end="")
    #     console = str(input())
    #     commandList = console.split('?')
        
    #     # if console == "Exit" :
    #     #     ext()
    #     #     break
        
    #     if commandList[0] == 'Subject' :
    #         if len(commandList) == 2 :
    #             emailData['subject'] = commandList[1].strip()
    #     elif commandList[0] == 'Body' :
        
    #         if len(commandList) == 2 :
    #             emailData['body'] = commandList[1].strip()
    #     elif commandList[0] == 'Recipient' :
    #         if len(commandList) == 2 :
    #             emailData['recipient'] = commandList[1].strip()
    #     else:
    #         print("invalid command")