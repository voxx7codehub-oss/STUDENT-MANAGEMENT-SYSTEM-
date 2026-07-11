from flask import Flask, render_template,request

app =Flask(__name__)

students = []


@app.route('/')
def home():
    # Show the registration form (template exists as add.html)
    return render_template("add.html")


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    department = request.form['department']
    course = request.form['course']

    students.append({
        'name': name,
        'department': department,
        'course': course,
    })

    # Show the table of registered students
    return render_template("index.html", students=students)


if __name__ == "__main__":
    app.run(debug=True)
