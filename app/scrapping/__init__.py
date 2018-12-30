from flask import Blueprint

bp = Blueprint('scrapping', __name__)

from app.scrapping import routes