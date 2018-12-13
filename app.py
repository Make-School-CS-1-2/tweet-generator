from flask import Flask
from old import stochastic_sample, dict_histogram
from source.markov_chain import MarkovChain
import os.path

app = Flask(__name__)


@app.route('/')
def hello_world():
    f = open(os.getcwd()+'/text/source.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n'))
    text = text.split(' ')
    chain = MarkovChain(text)
    sentence = stochastic_sample.make_sentence(chain)

    return ' '.join(sentence)
