#from keras.models import Sequential
#from keras.layers import Dense, Activation
from flask import Flask, render_template, request, jsonify, url_for, redirect, session
import pandas as pd 
from flask_pymongo import PyMongo



app = Flask(__name__)

def conn_mongo():
    app.config['MONGO_DBNAME'] = 'deeplearning'
    app.config['MONGO_URI'] = 'mongodb://admin:Reload04@ds217452.mlab.com:17452/deeplearning'
    mongo = PyMongo(app)
    return mongo

def create_df(collection):
    app.config['MONGO_DBNAME'] = 'deeplearning'
    app.config['MONGO_URI'] = 'mongodb://admin:Reload04@ds217452.mlab.com:17452/deeplearning'
    mongo = PyMongo(app)

    cursor = mongo.db[collection].find()
    df = pd.DataFrame(list(cursor))
    return df

@app.route('/', methods=['GET','POST'])
def index():

        df = create_df('storage')
        colunas = list(df.columns.values)
        return render_template('index.html', colunas=colunas)

@app.route('/resumo', methods=['POST'])
def resumo():

    df = create_df('storage')
    
    valor_x = request.form.getlist('my-select')
    
    for x in valor_x:
        if x in session['columns']:
            R = df.loc[:6, valor_x]
    
    RDICT = R.to_dict()

    valor_y = request.form['my-select3']

    camadas = request.form['resultado']
    
    losses_function = request.form.getlist('select2')

    custom_radios = request.form['select3']

    radios_toggles = request.form['select4']

    epochs = request.form['epochs']

    batch_size = request.form['batch_size']

    return render_template('resumo.html', valor_x=valor_x,
                                            RDICT=RDICT,
                                            valor_y=valor_y,
                                            camadas=camadas,
                                            losses_function=losses_function,
                                            custom_radios=custom_radios,
                                            radios_toggles=radios_toggles,
                                            epochs=epochs,
                                            batch_size=batch_size,
                                            )


@app.route('/results', methods=['POST'])
def process():
    if request.method == 'POST':
        layer_type = request.form['layer_type']
        neurons_number = request.form['neurons_number']
        activation = request.form['activation']
        optimizer = request.form['optimizer']
        # it's ok in front end
        loss = request.form['loss']
        # it's ok in front end
        metrics = request.form['metrics']
        # keras modelling
        model = Sequential([layer_type])
        model.compile(optimizer=optimizer,
            loss=loss,
            metrics=[metrics])
        summary = model.summary()
        # Train the model, iterating on the data in batches of 32 samples
        model.fit(X_train, y_train, epochs=10, batch_size=32, callbacks=[cb])
        evaluate = model.evaluate(X_test, y_test)
        return jsonify ({'name' : [layer_type, neurons_number, activation]})
    return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.debug = True #Uncomment to enable debugging
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    app.run(port=9000) #Run the Server