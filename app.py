from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'San Francisco, US'
  },
  {
    'id': 2,
    'title': 'Back End Developer',
    'location': 'Brussels, BE'
  },
  {
    'id': 3,
    'title': 'Front End Developer',
    'location': 'Sao Paulo, BR',
    'salary': 'R$ 3000,00'
  },
]

@app.route('/')
def home():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def jobs():
  return jsonify(JOBS)

if(__name__ == '__main__'):
  app.run(host='0.0.0.0', debug=True)