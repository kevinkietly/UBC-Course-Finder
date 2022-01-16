from flask import Flask, request, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        course_code = request.form.getlist("course_code")
        subject_code = request.form.get("subject_code")
        average = request.form.get("average")
        offered = request.form.getlist("offered")
        print(course_code)
        print(subject_code + " " + average)
        print(offered)
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)