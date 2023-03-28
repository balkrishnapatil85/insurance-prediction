from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
app = Flask('__name__')
model=pickle.load(open('insurance_pred.pkl','rb'))

@app.route('/')
def home():
    return render_template('insurance_home.html')

@app.route('/predict',methods=['POST'])
def predict():
    a=float(request.form.get(  'age'  ))
    b=float(request.form.get(  'sex'  ))
    c=float(request.form.get(  'bmi'  ))
    d=float(request.form.get(  'children'  ))
    e=float(request.form.get(  'smoker'  ))
    f=float(request.form.get(  'region'  ))
    

    result=model.predict(np.array([[a,b,c,d,e,f]]))
    #if result==1:
        # return "<h1 style='color:green'>Wine Quality is GOOD</h1>"
    return render_template('insurance_report.html',data=int(result))
    
    #else:
        #return "<h1 style='color:red'>Wine Quality is BAD</h1>"
         #return render_template('churn_no.html',prediction_text='Costomer churn prediction : No churn')

#app.run(debug=True,port=5000)
