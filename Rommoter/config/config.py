# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
REMOTEOK_API_URL = 'https://remoteok.io/api'
DJINNI_API_URL = 'https://djinni.co/my/inbox/'
INDEED_API_URL = 'https://www.indeed.com'
REMOTE_CO_API_URL = 'https://remote.co/remote-jobs/'
SIMPLYHIRED_API_URL = 'https://www.simplyhired.com/search'
UPWORK_API_URL = 'https://upwork.com'
