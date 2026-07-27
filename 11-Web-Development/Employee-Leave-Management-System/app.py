from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🚀 Employee Leave Management System</h1>

    <h2>Developed by Teenu Anand</h2>

    <hr>

    <p><strong>Course:</strong> MSc Artificial Intelligence</p>

    <p><strong>Project:</strong> Employee Leave Management System</p>

    <p><strong>Technology:</strong> Python + Flask</p>

    <p>✅ Flask is running successfully!</p>
    """


if __name__ == "__main__":
    app.run(debug=True)