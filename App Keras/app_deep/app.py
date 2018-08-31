#from keras.models import Sequential
#from keras.layers import Dense, Activation


from flask import Flask, render_template, request, jsonify, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/grid')
def hello_world2():
    return render_template('grid.html')


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
    app.run(port=9000) #Run the Server
