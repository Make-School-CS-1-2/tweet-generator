from flask import Flask
import stochastic_sample
import dict_histogram
app = Flask(__name__)


@app.route('/')
def hello_world():
    import sys
    f = open('don-quixote.txt', mode='r', encoding='utf-8-sig')
    text = " ".join(f.read().split('\n')).lower()

    histogram = dict_histogram.histogram(text)

    sentence = stochastic_sample.new_weighted_random_word(histogram)

    for _ in range(10):
       sentence += " " + stochastic_sample.new_weighted_random_word(histogram)
    return sentence


app.run()
