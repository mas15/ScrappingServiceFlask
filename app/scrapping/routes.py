import rq
import redis
from base64 import b64encode
from app.scrapping import bp
from flask import jsonify, current_app, request
from app.utils import read_scrapped_images, read_scrapped_text


@bp.route("/scrape", methods=['POST'])
def scrape():
    url_to_scrape = request.data.decode("utf-8")

    job = current_app.task_queue.enqueue('app.scrapping.tasks.scrape_async', url_to_scrape)
    job.meta['state'] = 'pending'

    return jsonify({
        "task_id": job.get_id()
    })


@bp.route("/status/<task_id>")
def check_status(task_id):
    return jsonify({
        "state": _get_status(task_id)
    })


@bp.route("/get/<task_id>")
def get_data(task_id):
    status = _get_status(task_id)
    if status == 'pending':
        return jsonify({"error": "Task has not started to be processed yet"})
    if status == 'processing':
        return jsonify({"error": "Url is processed now"})

    text, images = read_scrapped_text(task_id), read_scrapped_images(task_id)
    encoded_images = [b64encode(img).decode('utf-8') for img in images]

    return jsonify({
        'text': text,
        'images': encoded_images
    })


def _get_status(task_id):  # todo raise if not found
    job = get_rq_job(task_id)
    return job.meta.get('state', 'pending') if job else 'done'


def get_rq_job(task_id):
    try:
        rq_job = rq.job.Job.fetch(task_id, connection=current_app.redis)
    except (redis.exceptions.RedisError, rq.exceptions.NoSuchJobError):
        return None
    return rq_job
