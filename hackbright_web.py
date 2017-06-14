"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    projects = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           projects=projects)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")


@app.route("/student-add-form")
def add_student_form():
    """Renders form to add a student to database. """

    return render_template("student_add.html")


@app.route("/student-add-success", methods=["POST"])
def add_student_to_database():
    """Adds student to database from student-add-form route. """

    first = request.form.get("first")
    last = request.form.get("last")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template("student_add_success.html",
                           first=first,
                           last=last,
                           github=github)


@app.route("/project")
def get_project():
    """Show information about a project."""

    project = request.args.get('title')

    title, description, max_grade = hackbright.get_project_by_title(project)

    students = hackbright.get_grades_by_title(project)

    html = render_template("project_info.html",
                           title=title,
                           description=description,
                           max_grade=max_grade,
                           students=students)

    return html

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
