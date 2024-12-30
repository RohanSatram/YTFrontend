from flask import Flask, request, render_template, jsonify
from main import main, question

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    url = request.form['url'] 
    result = main(url) 
    return render_template('result.html', result=result)

@app.route('/result', methods=['POST'])
def result():
    text = request.form['ytfollowup']
    result = question(text)
    return render_template('result.html', result = result)

if __name__ == '__main__':
    app.run(debug=True)
