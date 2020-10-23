from flask import Flask, jsonify, request
from flask.json import JSONEncoder
from PostgreSQL_Connecter import Connector
from datetime import datetime


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = CustomJSONEncoder
app.config["DEBUG"] = True
app.config["JSON_AS_ASCII"] = False

conn = Connector()


@app.route("/", methods=['GET'])
def home():
    result = conn.getStationData()
    return jsonify(result)


@app.route("/getStationData", methods=['GET'])
def getStationData():
    result = conn.getStationData()
    return jsonify(result)


if __name__ == '__main__':
    app.run(host="192.168.0.55", port="8180")
