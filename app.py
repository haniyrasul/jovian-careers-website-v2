from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,000,000'
    }, 
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Remote',
    },
    {
        'id': 3,
        'title': 'Data Engineer',
        'location': 'Mumbai, India',
        'salary': 'Rs. 13,000,000'
    },
    {
        'id': 4,
        'title': 'Machine Learning Engineer',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 19,000,000'
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__=='__main__':
    app.run(debug=True)