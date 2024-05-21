# job_sources/djinni.py
import requests
from bs4 import BeautifulSoup

DJINNI_URL = 'https://djinni.co/jobs/'

def fetch_djinni_jobs():
    jobs = []
    response = requests.get(DJINNI_URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        job_listings = soup.find_all('li', class_='list-jobs__item')

        for job in job_listings:
            title = job.find('div', class_='list-jobs__title').get_text(strip=True).lower()
            company = job.find('div', class_='list-jobs__details__info').get_text(strip=True).lower()
            location = job.find('span', class_='location-text').get_text(strip=True).lower() if job.find('span', class_='location-text') else 'N/A'
            url = f"https://djinni.co{job.find('a', class_='profile')['href']}"
            tags = [tag.get_text(strip=True).lower() for tag in job.find_all('a', class_='job-tag')]
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'url': url,
                'tags': tags
            })
    return jobs
