from flask import Flask, render_template, request,jsonify
import os 
import json
import numpy as np
import pandas as pd
from SMDF.pipeline.forecasting import ForecastingPipeline
from SMDF.logging import logger
from flask_cors import CORS


app = Flask(__name__) # initializing a flask app
CORS(app)


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/forecast',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            
            obj = ForecastingPipeline()
            forecast = obj.forecasting()
            
            logger.info(type(forecast))
            #json_str = json.dumps(forecast)

            




            return jsonify(forecast)
        

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)
    


