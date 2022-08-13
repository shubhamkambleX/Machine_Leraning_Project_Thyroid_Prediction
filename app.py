import sys,os
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException
from flask import Flask, request
from housing.entity.retension_predict import RetensionPredictor, RetensionData
from flask import send_file, abort, render_template
from flask import Response



ROOT_DIR = os.getcwd()
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)


HOUSING_DATA_KEY = "retension_data"
LEFT_KEY = "Class"




app=Flask(__name__)



# @app.route("/",methods=["GET","POST"])
# def index():
#     try:
#         raise Exception("we are testing exception")
#     except Exception as e:
#         housing = HousingException(e,sys)
#         logging.info(housing.error_message)
#         logging.info("we are logging")
#     return "CI-CD Pipeline"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    context = {
        HOUSING_DATA_KEY: None,
        LEFT_KEY: None
    }

    if request.method == 'POST':
        age = int(request.form['age'])
        sex = request.form['sex']
        on_thyroxine = request.form['on_thyroxine']
        query_on_thyroxine = request.form['query_on_thyroxine']
        on_antithyroid_medication = request.form['on_antithyroid_medication']
        sick = request.form['sick']
        pregnant = request.form['pregnant']
        thyroid_surgery = request.form['thyroid_surgery']
        I131_treatment = request.form['I131_treatment']
        query_hypothyroid = request.form['query_hypothyroid']
        query_hyperthyroid = request.form['query_hyperthyroid']
        lithium = request.form['lithium']
        goitre = request.form['goitre']
        tumor = request.form['tumor']
        hypopituitary = request.form['hypopituitary']
        psych = request.form['psych']
        TSH = float(request.form['TSH'])
        T3 = float(request.form['T3'])
        TT4 = float(request.form['TT4'])
        T4U = float(request.form['T4U'])
        FTI = float(request.form['FTI'])
        referral_source = request.form['referral_source']
        

        retension_data = RetensionData(age=age,
                                   sex=sex,
                                   on_thyroxine=on_thyroxine,
                                   query_on_thyroxine=query_on_thyroxine,
                                   on_antithyroid_medication=on_antithyroid_medication,
                                   sick=sick,
                                   pregnant=pregnant,
                                   thyroid_surgery=thyroid_surgery,
                                   I131_treatment=I131_treatment,
                                   query_hypothyroid=query_hypothyroid,
                                   query_hyperthyroid=query_hyperthyroid,
                                   lithium=lithium,
                                   goitre=goitre,
                                   tumor=tumor,
                                   hypopituitary=hypopituitary,
                                   psych=psych,
                                   TSH=TSH,
                                   T3=T3,
                                   TT4=TT4,
                                   T4U=T4U,
                                   FTI=FTI,
                                   referral_source=referral_source
                                   )
        housing_df = retension_data.get_housing_input_data_frame()
        housing_predictor = RetensionPredictor(model_dir=MODEL_DIR)
        Class = housing_predictor.predict(X=housing_df)
        print('output : '+str(Class))
        context = {
            HOUSING_DATA_KEY: retension_data.get_housing_data_as_dict(),
            LEFT_KEY: Class,
        }
        return render_template('index.html', context=context)
    
    return render_template("index.html", context=context)





if __name__=="__main__":
    app.run(debug=True)