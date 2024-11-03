from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('static\data\data.csv')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    id = request.form.get('ID')  
    value = request.form.get('id_value')
    
    if id == 'student_id':
        student_data = data[data['Student id'] == int(value)].to_dict('records')

        if len(student_data) == 0:
            return render_template('error.html')
        
        s = sum(int(row[' Marks']) for row in student_data)
        return render_template('student.html', student_data=student_data, sum = s)

    elif id =='course_id':
        course_data = data.loc[data[" Course id"] == 2001, " Marks"].tolist()


        if len(course_data) == 0:
            return render_template('error.html')
        
        avg_marks = sum(course_data)//len(course_data)
        max_marks = max(course_data)
        plt.hist(course_data, bins=10, edgecolor='black')
        plt.title(f"Marks Distribution for Course {value}")
        plt.xlabel("Marks")
        plt.ylabel("Frequency")
        plt.savefig("static/images/histogram.jpg")
        
        return render_template("course.html", avg_marks= avg_marks, max_marks= max_marks)

    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, threaded=True)