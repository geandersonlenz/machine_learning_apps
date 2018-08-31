from flask import Flask, request, render_template, jsonify
from textblob import TextBlob
from bs4 import BeautifulSoup
import json, re, string
import spacy, nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
import urllib.request

import nltk

nlp = spacy.load("en")

app = Flask(__name__)

@app.route('/count')
def my_form():
    return render_template('forms.html')

@app.route('/count', methods=['POST'])
def my_form_post():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        count_text = text.count("oi")
        return jsonify ({'count': count_text})

@app.route('/tags')
def my_form2():
    return render_template('forms2.html')


@app.route('/tags', methods=['POST'])
def tags():
    if request.method == 'POST':
        text = request.form['text2']
        blob = TextBlob(text)
        tags = blob.tags
        return jsonify ({'tags': tags})

@app.route('/tokenization')
def my_form3():
    return render_template('forms3.html')


@app.route('/tokenization', methods=['POST'])
def tokens():
    if request.method == 'POST':
        text = request.form['text3']
        doc = nlp(text)
        tokenization = [token.orth_ for token in doc]
        return jsonify({'tokenization': tokenization})


@app.route('/lemmatisation')
def my_form4():
    return render_template('forms4.html')

@app.route('/lemmatisation', methods=['POST'])
def lemma():
    if request.method == 'POST':
        text = request.form['text4']
        doc = nlp(text)
        lemmatisation = [word.lemma_ for word in doc]
        return jsonify({'lemmatisation': lemmatisation})

@app.route('/postagging')
def my_form5():
    return render_template('forms5.html')

@app.route('/postagging', methods=['POST'])
def postag():
    if request.method == 'POST':
        text = request.form['text5']
        #tagging = []
        doc = nlp(text)
        tokenization = json.dumps([token.orth_ for token in doc])
        postagging = json.dumps([i.tag_ for i in doc])
        return jsonify({tokenization, postagging})

@app.route('/sentences')
def my_form6():
    return render_template('forms6.html')

@app.route('/sentences', methods=['POST'])
def sentence():
    if request.method == 'POST':
        text = request.form['text6']
        blob = TextBlob(text)
        sentences = blob.sentences
        return jsonify({'sentences': sentences})

@app.route('/punctuation')
def my_form7():
    return render_template('forms7.html')

@app.route('/punctuation', methods=['POST'])
def punct():
    if request.method == 'POST':
        text = request.form['text7']
        tokenized_docs=[word_tokenize(doc) for doc in text]
        x=re.compile('[%s]' % re.escape(string.punctuation))
        tokenized_docs_no_punctuation = []
        for review in tokenized_docs:
            new_review = []
        for token in review:
            new_token = x.sub(u'', token)
        if not new_token == u'':
            new_review.append(new_token)
        tokenized_docs_no_punctuation.append(new_review)
        return jsonify({'punctuation': tokenized_docs_no_punctuation})

@app.route('/stopwords')
def my_form8():
    return render_template('forms8.html')

@app.route('/stopwords', methods=['POST'])
def stop():
    if request.method == 'POST':
        words = request.form['text8']
        stops=set(stopwords.words('english'))
        stop_words = [word for word in words if word not in stops]
        return jsonify({'stopwords': stop_words})

@app.route('/wordfrequency')
def my_form9():
    return render_template('forms9.html')

@app.route('/wordfrequency', methods=['POST'])
def wordf():
    if request.method == 'POST':
        text = request.form['text9']
        response = urllib.request.urlopen('http://php.net/')
        html = response.read()
        soup = BeautifulSoup(html,"html5lib")
        text = soup.get_text(strip=True)
        tokens = [t for t in text.split()]
        freq = nltk.FreqDist(tokens)
        freq.plot(20, cumulative=False)
    for key,val in freq.items():
        return (str(key) + ':' + str(val))

@app.route('/synonyms')
def my_form10():
    return render_template('forms10.html')

@app.route('/synonyms', methods=['POST'])
def syno():
    if request.method == 'POST':
        text = request.form['text10']
        syn = wordnet.synsets("pain")
        definition = syn[0].definition()
        example = syn[0].examples()
        return jsonify({'definition': definition, 'example': example})

@app.route('/antonyms')
def my_form10():
    return render_template('forms10.html')

@app.route('/antonyms', methods=['POST'])
def anto():
    if request.method == 'POST':
        text = request.form['text10']
        antonyms = []
        for syn in wordnet.synsets("small"):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        return jsonify({'antonyms': antonyms})


@app.route('/stemmer')
def my_form11():
    return render_template('forms11.html')

@app.route('/stemmer', methods=['POST'])
def anto():
    if request.method == 'POST':
        text = request.form['text11']
        from nltk.stem import PorterStemmer
        stemmer = PorterStemmer()
        result = stemmer.stem(text)
        jsonify ({'stemmer': result})






if __name__ == '__main__':
    app.run(debug=True)
