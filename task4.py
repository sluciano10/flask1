from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello World!</h1>
    <p>Oscar A: LMAO</p>
    <p>Maria S: LOL</p>
    '''

@app.route('/smirth')
def smirth():
    return render_template('template.html', name='Smirth L', acronym='ASAP')

if __name__ == '__main__':
    app.run(debug=True)

