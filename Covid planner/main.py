import flask
import cases
import smm
import vaccination
from flask import render_template


app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/covid-sg')
def covid():
    newCases = cases.gov()
    updates = smm.govupdate()
    workplace = smm.workplace()
    vacSignup = vaccination.vaccineRegistration()

    return render_template('final.html', newCases = newCases, updates = updates, workplace = workplace, vacSignup = vacSignup)


@app.route('/mental-health/')
def mentalHealth():
    return render_template('final2.html')


if __name__ == '__main__':
    app.run()



