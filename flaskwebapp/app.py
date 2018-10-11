from flask import Flask, request
from driver import *
import time
from sklearn.linear_model import LinearRegression
import sys

app = Flask(__name__)


@app.route('/score', methods = ['GET'])
def scoreRRS():
    """ Endpoint for scoring
    """
    start = time.time()
    response = run()
    end = time.time() - start
    return response


@app.route("/")
def healthy():
    return "System is Healthy"


if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0') # Ignore, Development server