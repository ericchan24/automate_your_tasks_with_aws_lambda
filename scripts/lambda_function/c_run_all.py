import a_scrape_articles
import b_email
import datetime

def run_file():
    '''
    scrapes fangraphs articles and emails them as an attachment
    '''
    start_time = datetime.datetime.now()
    a_scrape_articles.run_file()
    b_email.run_file()

    end_time = datetime.datetime.now()
    print(f'Started: {start_time}\n'
        f'Ended: {end_time}\n'
        f'Run time: {end_time - start_time}')

if __name__=='__main__':
    run_file()
