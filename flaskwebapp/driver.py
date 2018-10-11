import numpy as np
import logging, sys, json
import timeit as t
import base64
import pickle
from io import BytesIO
from sklearn.linear_model import LinearRegression


MODEL_FILE = 'car_prediction_model.pkl'

logger = logging.getLogger("cntk_svc_logger")
ch = logging.StreamHandler(sys.stdout)
logger.addHandler(ch)

loaded_model = None
X_test = None
y_test = None


def init():

    #Load up our test data and Learned Model

    global loaded_model,X_test,y_test

    start = t.default_timer()

    loaded_model = pickle.load(open(MODEL_FILE, 'rb'))
    end = t.default_timer()

    file_xtest = open('X_test.pkl','rb')
    X_test = pickle.load(file_xtest)

    file_ytest = open('y_test.pkl','rb')
    y_test = pickle.load(file_ytest)

    end = t.default_timer()
    loadTimeMsg = "Model loading time: {0} ms".format(round((end - start) * 1000, 2))
    logger.info(loadTimeMsg)


def run():
    """ Classify the input using the loaded model
    """
    start = t.default_timer()

    result = []
    coeff = loaded_model.score(X_test,y_test)
    result = str(coeff)

    end = t.default_timer()

    actualWorkTime = 1;
    return (result, 'Computed in {0} ms'.format(actualWorkTime))