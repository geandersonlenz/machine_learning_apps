from flask import Flask, request, render_template, redirect, url_for, jsonify, session
import networkx as nx
import pandas as pd

app = Flask(__name__)

#########################    ROTAS DE ACESSO   ##################################

@app.route('/')
def index():
	multiselect = ''
	return render_template('index.html', multiselect=multiselect)

@app.route('/select', methods=['POST'])
def select():
	multiselect = request.form.getlist('mymultiselect')
	df = pd.read_csv('products.csv')
	sample = df.sample(n=50)
	source = multiselect[0]
	target = multiselect[1]
	grafo = nx.from_pandas_edgelist(sample, source=source, target=target, edge_attr=True,)
	#nodes = grafo.nodes()
	edges = grafo.edges()
	return render_template('index.html', multiselect=multiselect, edges=edges)

if __name__ == '__main__':
	app.run(debug=True)

