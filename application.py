from flask import Blueprint
from flaskapp import create_app
from api import PocketAPI, RestAPI
from flask import jsonify

app = create_app()
pocket = Blueprint("pocket", __name__)


# Create rest API
rest_api = RestAPI(app)

# Create Pocket API
p = PocketAPI(
    consumer_key=app.config['POCKET_CONSUMER_KEY'],
    access_token=app.config['POCKET_ACCESS_TOKEN'])
p.connect()
rest_api.set_pocket(p)


# Routes
@pocket.route("/get/<string:tag>", methods=['GET'], defaults={'count': 100})
@pocket.route("/get/<string:tag>/<int:count>", methods=['GET'])
def get(tag, count):
    # Fetch articles
    data = rest_api.pocket.get(
        tag=tag,
        count=count,
        sort='oldest',
        state='all'
    )
    return jsonify(data)


# Register blueprints
app.register_blueprint(pocket, url_prefix='/pocket')

if __name__ == "__main__":
    app.run()
