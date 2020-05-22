import a_scrape_articles
from bs4 import BeautifulSoup
import datetime
import lxml
import os
import requests
import utils

article_title_lst, article_date_lst, article_text_lst = a_scrape_articles.main()
region = os.environ.get('AWS_REGION')
access_key = os.environ.get('AWS_ACCESS_KEY_ID')
secret_key = os.enviorn.get('AWS_SECRET_ACCESS_KEY')


def lambda_handler(event, context):

    content = ''
    for title, date, text in zip(article_title_lst, article_date_lst,
        article_text_lst):
        content += title.encode('utf-8')
        content += '\n'.encode('utf-8')
        content += date.encode('utf-8')
        content += text.encode('utf-8')
        article_seperator = '\n' + '-' * 100 + '\n'
        content += article_seperator.encode('utf-8')
        content += article_seperator.encode('utf-8')
        content += article_seperator.encode('utf-8')

	# Export the data to S3
    s3 = boto3.resource(
        's3',
        region_name = 'us-east-2',
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key
    )

    f_name = f'articles_{today_datetime}.txt'.replace('-', '_')

    content="String content to write to a new S3 file"
    s3.Object('fangraphs', f_name).put(Body = content)
