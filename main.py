import time
from types import NoneType
from bs4 import BeautifulSoup
import requests

# url = input('Enter indeed.com url to scrape => ')
minutes = int(input('Repeat after how many minutes => '))
url = 'https://pk.indeed.com/jobs?q=python&l&vjk=8340b31c7c0f5c09'
def find_jobs():
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('div', class_='job_seen_beacon')
    for index, job in enumerate(jobs):
        posted_date = job.find('span', class_ = 'date').text
        salary = job.find('div',class_='salary-snippet')
        job_title = job.find('h2',class_ = 'jobTitle')
        if(job_title.span.text == 'new'):
            title = job_title.find_all('span')[1].text
        else:
            title = job_title.span.text

        if salary != None:
            with open(f'posts/{index}.txt','w') as f:
                f.write(f'''
                    Job Title: {title}
                    salary: {salary.text}
                    {posted_date}
                ''')
                print(f'File saved in {index}.txt')
        else:
            with open(f'posts/{index}.txt','w') as f:
                f.write(f'''
                    Job Title: {title}
                    salary: Not Defined
                    {posted_date}
                ''')
                print(f'File saved in {index}.txt')

if __name__ == '__main__':
    while True: 
        find_jobs()
        print(f'Waiting {minutes} minutes')
        time.sleep(minutes * 60)