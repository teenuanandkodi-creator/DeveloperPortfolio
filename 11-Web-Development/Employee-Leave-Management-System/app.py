from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
from src.database import (
     initialize_database,
     initialize_users
)

from src.leave import (
    add_leave_request,
    get_all_leave_requests,
    get_leave_statistics,
    update_leave_status,
    search_leave_requests
)

from src.employee import (

    get_all_employees,
    insert_sample_data,
    add_employee,
    get_employee_by_id,
    update_employee,
    delete_employee,
    get_total_employees,
    search_employees,
    get_employee_by_employee_id
    
)

from src.auth import authenticate_user

app = Flask(__name__)

app.secret_key = "employee-leave-management-secret-key"

def is_logged_in():

    return "user_id" in session


def is_admin():

    return str(session.get("role","")).lower() == "admin"


def is_employee():

    return str(session.get("role","")).lower() == "employee"

initialize_database()

initialize_users()

insert_sample_data()

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = authenticate_user(
            username,
            password
        )

        if user:

            session["user_id"] = user["id"]

            session["username"] = user["username"]

            session["role"] = str(user["role"]).lower()

            return redirect(
                url_for("home")
            )

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template(
        "login.html"
    )
@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("login")
    )

@app.route("/")
def home():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )
    
    total_employees = get_total_employees()

    leave_stats = get_leave_statistics()

    return render_template(
        "index.html",
        total=total_employees,
        leave_stats=leave_stats
    )

@app.route("/employees")
def employees():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )
    
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


@app.route("/add-employee", methods=["GET", "POST"])
def add_employee_page():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if not is_admin():

        return "Access Denied: Admins only", 403
    
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

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if not is_admin():

        return "Access Denied: Admins only", 403
    
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

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if not is_admin():

        return "Access Denied: Admins only", 403
    
    delete_employee(id)

    return redirect(url_for("employees"))

@app.route("/leave", methods=["GET", "POST"])
def leave():

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        employee_id = request.form["employee_id"].strip()

        leave_type = request.form["leave_type"].strip()

        start_date = request.form["start_date"]

        end_date = request.form["end_date"]

        reason = request.form["reason"].strip()

        # Validate required fields

        if not employee_id or not leave_type or not start_date or not end_date or not reason:

            flash(
                "All fields are required.",
                "danger"
            )

            return redirect(
                url_for("leave")
            )

        # Check whether employee exists

        employee = get_employee_by_employee_id(employee_id)

        if not employee:

            flash(
                    f"Employee ID {employee_id} does not exist.","danger")

            return redirect(
                    url_for("leave")
                )

        # Validate date range

        if end_date < start_date:

            flash(
                "End date cannot be before start date.",
                "danger"
            )

            return redirect(
                url_for("leave")
            )

        # Add leave request

        add_leave_request(
            employee_id,
            leave_type,
            start_date,
            end_date,
            reason
        )

        flash(
            "Leave request submitted successfully.",
            "success"
        )

        return redirect(
            url_for("leave")
        )

    search_employee_id = request.args.get(
        "employee_id",
        ""
    )

    search_status = request.args.get(
        "status",
        ""
    )

    search_leave_type = request.args.get(
        "leave_type",
        ""
    )

    if (
        search_employee_id
        or search_status
        or search_leave_type
    ):

        leave_requests = search_leave_requests(
            search_employee_id,
            search_status,
            search_leave_type
        )

    else:

        leave_requests = get_all_leave_requests()

    return render_template(
        "leave.html",
        leave_requests=leave_requests,
        search_employee_id=search_employee_id,
        search_status=search_status,
        search_leave_type=search_leave_type
    )

@app.route("/approve_leave/<int:id>")
def approve_leave(id):

    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if not is_admin():

        return "Access Denied: Admins only", 403
    
    update_leave_status(
        id,
        "Approved"
    )

    flash(
        "Leave request approved successfully.",
        "success"
    )

    return redirect(url_for("leave"))

@app.route("/reject_leave/<int:id>")
def reject_leave(id):
    
    if not is_logged_in():

        return redirect(
            url_for("login")
        )

    if not is_admin():

        return "Access Denied: Admins only", 403

    update_leave_status(
        id,
        "Rejected"
    )

    flash(
        "Leave request rejected.",
        "danger"
    )

    return redirect(url_for("leave"))

@app.route("/about")
def about():

    if "user_id" not in session:

        return redirect(
            url_for("login")
        )

    return render_template(
        "about.html"
    )


if __name__ == "__main__":

    app.run(debug=True)