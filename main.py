from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello, Welcome!</h1>
    <p>This is Mahmoud's Google Cloud App Engine project.</p>
    <p>Successfully deployed using Google Cloud PaaS.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
