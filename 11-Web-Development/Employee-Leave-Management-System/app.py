from flask import Flask, render_template

from src.database import initialize_database

from src.employee import (

    get_all_employees,

    insert_sample_data

)

app = Flask(__name__)

initialize_database()

insert_sample_data()


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/employees")
def employees():

    employee_list = get_all_employees()

    return render_template(

        "employees.html",

        employees=employee_list

    )


@app.route("/leave")
def leave():

    return render_template("leave.html")


@app.route("/about")
def about():

    return render_template("about.html")


if __name__ == "__main__":

    app.run(debug=True)