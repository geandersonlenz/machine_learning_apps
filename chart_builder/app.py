from flask import Flask
from flask import render_template, request
from datetime import time
 
 
app = Flask(__name__)


@app.route('/index')
def my_form():
    return render_template('forms.html')

@app.route('/charts', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        legend = request.form['legend']
        labels = request.form['labels']
        values = request.form['values']
        chart = request.form['chart']
    return render_template('chart.html', values=values, labels=labels, legend=legend, chart=chart)
        
 
 
if __name__ == "__main__":
    app.run(debug=True)