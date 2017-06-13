"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github)

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

    # get parameters from the form we are creating now,
    # to pass to this function, which will add to database and then return the
    # success message that will be printed at the end of this function

    # the template that will get and format the output from make_new_student
    # function (above)

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
