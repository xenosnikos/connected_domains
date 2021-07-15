from flask import Flask
from flask_restful import Api

from controllers.connected_domains import ConnectedDomains

app = Flask(__name__)
api = Api(app)

api.add_resource(ConnectedDomains, "/v2/connectedDomains")

if __name__ == "__main__":
    app.run()
