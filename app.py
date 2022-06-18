from flask import Flask 
from housing.logger import logging

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("testing logging")
    return "Starting the Machine Leraning Project"



if __name__=="__main__":
    app.run(debug=True)

# HERUKU_API_KEY = 0fd3a65b-f4b3-472a-8c34-36c8a481f5e3
# HERUKU_EMAIL_ID = 196shubham@gmail.com
# HERUKU_app = simple-ml-project
