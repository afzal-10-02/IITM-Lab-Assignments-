import csv
import sys
import matplotlib.pyplot as plt

def generate_student_html(student_id, data):
    # Filter data for the given student
    student_data = [row for row in data if row['Student id'] == student_id]
    
    if not student_data:
        return generate_error_html(f"Invalid Student ID: {student_id}")
    
    # Generate HTML for student details
    total_marks = sum(int(row['Marks']) for row in student_data)
    html_content = f"""<!DOCTYPE html>
    <html>
    <head><title>Student Details</title></head>
    <body>
    <h2>Student Details</h2>
    <table border="1">
        <tr><th>Student ID</th><th>Course ID</th><th>Marks</th></tr>"""
    
    for row in student_data:
        html_content += f"<tr><td>{row['Student id']}</td><td>{row['Course id']}</td><td>{row['Marks']}</td></tr>"
    
    html_content += f"<tr><td colspan='2'>Total</td><td>{total_marks}</td></tr>"
    html_content += "</table></body></html>"
    
    with open("output.html", "w") as file:
        file.write(html_content)

def generate_course_html(course_id, data):
    # Filter data for the given course
    course_data = [int(row['Marks']) for row in data if row['Course id'] == course_id]
    
    if not course_data:
        return generate_error_html(f"Invalid Course ID: {course_id}")
    
    average_marks = sum(course_data) / len(course_data)
    max_marks = max(course_data)
    
    # Create the HTML for course details
    html_content = f"""<!DOCTYPE html>
    <html>
    <head><title>Course Details</title></head>
    <body>
    <h2>Course Details</h2>
    <table border="1">
        <tr><th>Average Marks</th><th>Maximum Marks</th></tr>
        <tr><td>{average_marks:.2f}</td><td>{max_marks}</td></tr>
    </table>
    <img src="course_histogram.png" alt="Marks Histogram" width="500" height="300">
    </body>
    </html>"""
    
    with open("output.html", "w") as file:
        file.write(html_content)

    # Create histogram for course marks
    plt.hist(course_data, bins=10, edgecolor='black')
    plt.title(f"Marks Distribution for Course {course_id}")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.savefig("course_histogram.png")

def generate_error_html(message):
    html_content = f"""<!DOCTYPE html>
    <html>
    <head><title>Error</title></head>
    <body>
    <h2>Error</h2>
    <p>{message}</p>
    </body></html>"""
    
    with open("output.html", "w") as file:
        file.write(html_content)

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments. Expected 2.")
        return
    
    option, identifier = sys.argv[1], sys.argv[2]
    
    # Read data.csv
    data = [
    {"Student id": "1001", "Course id": "2001", "Marks": "56"},
    {"Student id": "1002", "Course id": "2001", "Marks": "67"},
    {"Student id": "1003", "Course id": "2001", "Marks": "78"},
    {"Student id": "1004", "Course id": "2001", "Marks": "90"},
    {"Student id": "1005", "Course id": "2001", "Marks": "45"},
    {"Student id": "1001", "Course id": "2002", "Marks": "58"},
    {"Student id": "1002", "Course id": "2002", "Marks": "98"},
    {"Student id": "1009", "Course id": "2002", "Marks": "12"},
    {"Student id": "1007", "Course id": "2002", "Marks": "99"},
    {"Student id": "1008", "Course id": "2002", "Marks": "39"},
    {"Student id": "1003", "Course id": "2003", "Marks": "34"},
    {"Student id": "1004", "Course id": "2003", "Marks": "43"},
    {"Student id": "1000", "Course id": "2003", "Marks": "25"},
    {"Student id": "1060", "Course id": "2003", "Marks": "60"},
    {"Student id": "1090", "Course id": "2003", "Marks": "88"},
    {"Student id": "1005", "Course id": "2004", "Marks": "81"},
    {"Student id": "1080", "Course id": "2004", "Marks": "59"},
    {"Student id": "1030", "Course id": "2004", "Marks": "87"},
    {"Student id": "1001", "Course id": "2004", "Marks": "35"},
    {"Student id": "1090", "Course id": "2004", "Marks": "33"}
]

    
    if option == '-s':
        generate_student_html(identifier, data)
    elif option == '-c':
        generate_course_html(identifier, data)
    else:
        generate_error_html("Invalid option. Use '-s' for student ID or '-c' for course ID.")

if __name__ == "__main__":
    main()
