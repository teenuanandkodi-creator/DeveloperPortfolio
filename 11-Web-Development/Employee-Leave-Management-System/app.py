from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for
)
from src.database import initialize_database

from src.employee import (

    get_all_employees,
    insert_sample_data,
    add_employee,
    get_employee_by_id,
    update_employee

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

@app.route("/add_employee", methods=["GET", "POST"])
def add_employee_page():

    if request.method == "POST":

        employee_id = request.form["employee_id"]

        name = request.form["name"]

        department = request.form["department"]

        add_employee(
            employee_id,
            name,
            department
        )

        return redirect(url_for("employees"))

    return render_template("add_employee.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    employee = get_employee_by_id(id)

    if request.method == "POST":

        employee_id = request.form["employee_id"]

        name = request.form["name"]

        department = request.form["department"]

        update_employee(
            id,
            employee_id,
            name,
            department
        )

        return redirect(url_for("employees"))

    return render_template(
        "edit_employee.html",
        employee=employee
    )


@app.route("/leave")
def leave():

    return render_template("leave.html")


@app.route("/about")
def about():

    return render_template("about.html")



if __name__ == "__main__":

    app.run(debug=True)