from flask import Flask, render_template, json
import data
app = Flask(__name__)


@app.route('/')
def index():

    return render_template('home.html')


@app.route('/about')
def about():
    about = 'Albin Sundqvist made this'
    return render_template('about.html', about=about)

@app.route('/features')
def features():
    return render_template('features.html')


if __name__ == '__main__':
    some_data = data.get_some_data()
    app.run(debug=True)
