from flask import Flask
from routes import index

app = Flask(__name__)
app.add_url_rule("/", "index", index)

if __name__ == "__main__":
    app.run(debug=True)