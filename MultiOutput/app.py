import numpy as np
from flask import Flask, abort, jsonify, request, render_template
import _pickle as cPickle
import pickle
from sklearn.externals import joblib

#purchase = cPickle.load(open("top_product.pkl", "rb"))
#purchase = pickle.load(open("multiclassifier2.pkl", "rb"))
purchase = joblib.load("multiclassifier.pkl", "rb")


app = Flask(__name__)

@app.route('/')
def standard():
   return render_template('index.html')


@app.route('/api', methods=['GET', 'POST'])
def make_predict():
    if request.method == 'POST':
        preco = request.form.get('preco')
        quantidade = request.form.get('quantidade')
        promotion = request.form.get('promotion')
        receita = request.form.get('receita')
        clima = request.form.get('clima')
        predict_request = [[preco, quantidade, promotion, receita, clima]]
        y_hat = purchase.predict(predict_request)
        y_hat = y_hat.tolist()
        return jsonify(result=y_hat)

    #return render_template("result.html",result = result)

    # np arrays goes into random forest, prediction comes out
    

      
    # all kinds of error checking should go here
    #data = request.get_json(silent=True)
    # convert our json to a numpy array
    #predict_request = [data['Preco'], data['Quantidade'], data['Promotion'], data['Receita'], data['Clima']]
    # np arrays goes into random forest, prediction comes out
    
    # return our prediction
    #output = [y_hat[0]]

if __name__ == '__main__':
    app.run(port=9000, debug=True)

