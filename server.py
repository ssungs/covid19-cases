from flask import Flask, render_template
from covid19_cases_data import Covid19_cases_data


app = Flask(__name__)

@app.route('/')
def index():
    cases = 'Covid19 cases in Korea'
    return render_template('index.html', cases=cases)

@app.route('/covid19_korea_cases')
def show_user():
    casesdata=Covid19_cases_data()
    return render_template('covid19_korea_cases.html', cases_data=casesdata)

if __name__=='__main__':
    app.run(host='localhost', port=8119, debug=True)
