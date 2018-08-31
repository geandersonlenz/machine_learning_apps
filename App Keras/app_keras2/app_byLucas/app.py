#from keras.models import Sequential
#from keras.layers import Dense, Activation

from flask import Flask, render_template, request, jsonify, url_for
import pandas as pd

app = Flask(__name__)

## Lucas
@app.route('/')
def new():
    return render_template('index2.html')

@app.route('/process', methods=['POST'])
def process():
    if request.method == 'POST':

        url = request.files['file']
        df = pd.read_csv(url)

        cat = list(df.columns.values)

        layer_types = list(df['Layer Type'].dropna().unique())
        neurons_number = list(df['Neurons Number'].dropna().unique())
        activations = list(df['Activations'].dropna().unique())
        optimizer = list(df['Optimizer'].dropna().unique())
        min_optimizer = min(optimizer)
        max_optimizer = max(optimizer)

        return render_template('process.html', cat=cat, layer_types=layer_types,
            neurons_number=neurons_number, activations=activations, optimizer=optimizer,
            max_optimizer=max_optimizer, min_optimizer=min_optimizer)
    return redirect(url_for('new'))

@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        layertype = request.form['layertypes']
        neuronsnumber = request.form['neuronsnumber']
        activations = request.form['activations']
        optimizer = request.form['range']
        
        return render_template('resultado.html', 
                                layertype=layertype,
                                neuronsnumber=neuronsnumber,
                                activations=activations,
                                optimizer=optimizer)
    return resultado(url_for('new'))


if __name__ == '__main__':
    app.run(port=9000, debug=True)