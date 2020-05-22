import a_scrape_articles
import boto3
from bs4 import BeautifulSoup
import datetime
import lxml
import os
import requests
import utils

article_title_lst, article_date_lst, article_text_lst = a_scrape_articles.main()
region = os.environ.get('AWS_REGION')
access_key = os.environ.get('AWS_ACCESS_KEY')
secret_key = os.environ.get('AWS_SECRET_KEY')


def lambda_handler(event, context):

    content = ''
    for title, date, text in zip(article_title_lst, article_date_lst,
        article_text_lst):
        content += title
        content += '\n'
        content += date
        content += text
        article_seperator = '\n' + '-' * 100 + '\n'
        content += article_seperator
        content += article_seperator
        content += article_seperator

	# Export the data to S3
    s3 = boto3.resource(
        's3',
        region_name = region,
        aws_access_key_id = access_key,
        aws_secret_access_key = secret_key
    )

    today_datetime = datetime.datetime.now().date()
    f_name = f'articles_{today_datetime}.txt'.replace('-', '_')

    s3.Object('fangraphs', f_name).put(Body = content)
