HOST, PORT = "0.0.0.0", 514

#
# NO USER SERVICEABLE PARTS BELOW HERE...
#


import os
import sys
import json
import logging
import numpy as np
import pandas as pd
import socketserver as SocketServer
import tensorflow as tf
from keras import backend as K
from keras.models import load_model, save_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from logging.handlers import RotatingFileHandler


config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
K.set_session(sess)


logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='')
logger = logging.getLogger("Rotating Log")
logger.setLevel(logging.INFO)

# Output Path for Write preds data
output_path = '/data/cc.log'

# add a rotating handler
handler = RotatingFileHandler(output_path, maxBytes=20000, backupCount=5)
logger.addHandler(handler)



# Declare traffic data prediction model here.
path = './hcn_traffic_model2.h5'
model = load_model(filepath=path)

# Store prediction data here
preds_list = []

class SyslogTCPHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = json.loads(str(bytes.decode(self.request[0].strip())))
        data_trans = []

        # LabelEncoder()
        encoder = LabelEncoder()

        data_trans.append(data['bps'])
        data_trans.append(data['day'])
        preds_list.append(data_trans)

        if len(preds_list) >= 5:
            data_numpy = np.asarray(preds_list[-5:])

            data_numpy[:, 1] = encoder.fit_transform(data_numpy[:, 1])
            data_numpy = data_numpy.astype('float64')

            # MinMax Normalization
            scaler = MinMaxScaler(feature_range=(0., 1.))
            scaled = scaler.fit_transform(data_numpy)
            scaled = scaled.reshape(-1, 5, 2)

            # Prediction
            with tf.device('/gpu:1'):
                preds = model.predict(scaled)
                preds = np.concatenate((preds, preds), axis=1)
                preds = scaler.inverse_transform(preds)

            output = {
                'bps': float(preds[0][0])
            }

            # Write Predicted Output onto the "cc.log" file
            logger.info(json.dumps(output))


if __name__ == "__main__":

    pid = str(os.getpid())
    pid_file = "/var/run/syslog_server.pid"

    with open(pid_file, 'w') as pw:
        pw.write(pid.strip())

    try:
        server = SocketServer.UDPServer((HOST, PORT), SyslogTCPHandler)
        server.serve_forever(poll_interval=1)
    except:
        pass
    finally:
        os.unlink(pid_file)

