import datetime
import os
import smtplib
from email.message import EmailMessage

def run_file():
    '''
    sends email of scraped fangraphs articles
    '''
    print(f'Running {__name__}')
    email_address = os.environ.get('EMAIL_ADDRESS')
    email_password = os.environ.get('EMAIL_PASSWORD')

    msg = EmailMessage()
    today_datetime = datetime.datetime.now().date()
    msg['Subject'] = f'Fangraphs Articles - {today_datetime}'

    msg['From'] = email_address
    msg['To'] = email_address
    msg.set_content('Articles')
    today_datetime = str(today_datetime).replace('-', '_')
    with open(f'/Users/eric/ds/fangraphs/text_files/articles_{today_datetime}'
        f'.txt', 'rb') as f:
        file_data = f.read()
        file_name = f.name

    file_name = file_name.split('/')[-1].split('.')[0]

    msg.add_attachment(file_data, maintype = 'application',
        subtype = 'octet-stream', filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)

        smtp.send_message(msg)

if __name__=='__main__':
    run_file()
