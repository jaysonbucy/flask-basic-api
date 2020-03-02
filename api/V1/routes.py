from flask import Blueprint


v1 = Blueprint('v1', __name__)


@v1.route('/', methods=['GET'])
def hello():
    return "Hello World!"
