from rq import get_current_job
from app import create_app
from .scrapping import scrape_from_site

app = create_app()
app.app_context().push()


def scrape_async(url):
    job = get_current_job()
    task_id = job.get_id()

    job.meta['state'] = 'processing'
    job.save_meta()

    scrape_from_site(url, task_id)

    job.meta['state'] = 'done'
    job.save_meta()
