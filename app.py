from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd
from tabulate import tabulate

app = Flask(__name__)

# Import rule-based logic
from rules import generate_schedule


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    subjects = request.form.getlist('subject')
    difficulties = request.form.getlist('difficulty')
    hours_per_day = float(request.form['hours'])
    exam_date = datetime.strptime(request.form['exam_date'], '%Y-%m-%d')

    data = list(zip(subjects, difficulties))
    schedule = generate_schedule(data, hours_per_day, exam_date)

    return render_template(
        'result.html',
        schedule=schedule,
        exam_date=exam_date.strftime("%d %b %Y")
    )


if __name__ == '__main__':
    app.run(debug=True)
