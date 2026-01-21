from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def index():
    message = os.getenv("APP_MESSAGE", "Hello from Dockerized Flask!")
    return f"<h1>{message}</h1>\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
