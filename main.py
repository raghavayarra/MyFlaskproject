from flask import Flask, request, render_template,url_for,redirect
import config
import database
import os
import json
import logging


app = Flask(__name__)

#logging creation for this application

logger = logging.getLogger(__name__)
LOGLEVEL = os.environ.get('LOGLEVEL', 'debug').upper()
logging.basicConfig(level=LOGLEVEL)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./main.log', mode='w')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


#index page creation

@app.route('/', methods = ['POST', 'GET'])
def index():
    try:
        if request.method == 'GET':
            logger.info(" use GET method to fetch the values from Database")
            obj=database.dbconnection()
            response = obj.get_values() 
            return render_template('form.html', data=response)

        try:
            if request.method == 'POST':
                logger.info(" Use POST method to enter the values into the Database")
                fname = request.form['name']
                obj=database.dbconnection()
                response=obj.insert_values(fname)
                return redirect(url_for('index'))
        except Exception as e:
            logger.exception("Error while processing post request:{}".format(e))
            logger.error("Error while processing POST request") 
            return "Error while processing POST request"

    except Exception as e:
            logger.exception("Error while processing GET request:{}".format(e))
            logger.error("Error while processing Get request") 
            return "Error while processing GET request"
       

if __name__ == "__main__":
    logger.info('app started to run')
    obj=database.dbconnection()
    s=obj.table_creation() # calling table creation function from database module 
    app.run(debug=True,host='0.0.0.0')


