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
    update_employee,
    delete_employee,
    get_total_employees,
    search_employees
    
)

app = Flask(__name__)

initialize_database()

insert_sample_data()


@app.route("/")
def home():

    total = get_total_employees()

    return render_template(
        "index.html",
        total=total
    )

@app.route("/employees")
def employees():

    keyword = request.args.get("search", "")

    if keyword:

        employee_list = search_employees(keyword)

    else:

        employee_list = get_all_employees()

    return render_template(
        "employees.html",
        employees=employee_list,
        keyword=keyword
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

@app.route("/delete/<int:id>")
def delete(id):

    delete_employee(id)

    return redirect(url_for("employees"))


@app.route("/leave")
def leave():

    return render_template("leave.html")


@app.route("/about")
def about():

    return render_template("about.html")



if __name__ == "__main__":

    app.run(debug=True)