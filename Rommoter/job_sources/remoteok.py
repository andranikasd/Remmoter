# job_sources/remoteok.py
import requests
from config import config

def fetch_remoteok_jobs():
    response = requests.get(config.REMOTEOK_API_URL)
    if response.status_code == 200:
        jobs = response.json()
        return [{
            'title': job.get('position', 'N/A'),
            'company': job.get('company', 'N/A'),
            'location': job.get('location', 'N/A'),
            'url': job.get('url', 'N/A'),
            'tags': [tag.lower() for tag in job.get('tags', [])]
        } for job in jobs]
    return []
