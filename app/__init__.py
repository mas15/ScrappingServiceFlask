from flask import Flask
from redis import Redis
import rq
import os


def create_app():
    app = Flask(__name__)

    app.redis = Redis.from_url(os.environ.get('TASKS_REDIS_URI'))
    app.task_queue = rq.Queue('scrapping-tasks', connection=app.redis)

    from app.scrapping import bp as scrapping_bp
    app.register_blueprint(scrapping_bp)

    return app
