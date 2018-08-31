from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import networkx as nx
import pandas as pd
from pandas_highcharts.core import serialize


app = Flask(__name__)

#########################    ROTAS DE ACESSO   ##################################
import time
import random

s = []
i = time.time()
while i < time.time() + 100:
    i += 1
    s.append([i, random.randint(0, 10), random.random()])
df = pd.DataFrame(s , columns = ["dt", "val1", "val2"])

df.dt = df.dt.astype("datetime64[s]")

df = df.set_index("dt")

@app.route('/')
def index():
    chart = serialize(df, render_to='my-chart',
    output_type='json', legend='None',
    title='Trending Account Value(Daily)')
    return render_template('charts.html', chart=chart)


if __name__ == '__main__':
	app.run(debug=True)
