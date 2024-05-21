# job_sources/__init__.py
from job_sources.remoteok import fetch_remoteok_jobs
from job_sources.djinni import fetch_djinni_jobs
from job_sources.indeed import fetch_indeed_jobs
from job_sources.remote_co import fetch_remote_co_jobs
from job_sources.simplyhired import fetch_simplyhired_jobs
from job_sources.upwork import fetch_upwork_jobs

def fetch_all_jobs():
    jobs = []
    jobs.extend(fetch_remoteok_jobs())
    jobs.extend(fetch_djinni_jobs())
    jobs.extend(fetch_indeed_jobs())
    jobs.extend(fetch_remote_co_jobs())
    jobs.extend(fetch_simplyhired_jobs())
    jobs.extend(fetch_upwork_jobs())
    return jobs
