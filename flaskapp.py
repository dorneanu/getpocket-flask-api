from flask import Flask, Blueprint
from flask import jsonify

pocket = Blueprint("pocket", __name__)


def create_app():
    """ Flask app factory """
    app = Flask(__name__)
    app.config.from_envvar('FLASK_CONFIG_FILE')
    return app


class RestAPI:

    """ REST API for the Pocket API """

    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port

    def set_pocket(self, pocket):
        self.pocket = pocket

    def get_pocket(self):
        return self.pocket

    def run(self):
        app.run(host=app.config['HOST'], port=app.config['PORT'])

# Create rest API
rest_api = RestAPI()

# Routes
@pocket.route("/get/<string:tag>", methods=['GET'], defaults={'count': 20})
@pocket.route("/get/<string:tag>/<int:count>", methods=['GET'])
def get(tag, count):
    # Fetch articles
    data = rest_api.pocket.get(
        tag=tag,
        count=count,
        sort='newest',
        state='all'
    )
    return jsonify(data)


# Create flask app
app = create_app()

# Register blueprints
app.register_blueprint(pocket, url_prefix='/pocket')
