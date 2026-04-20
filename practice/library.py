from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world!"

@app.route('/sum')
def summa():
    a = 10
    b = 15
    return str(a + b)

if __name__ == "__main__":
    app.run(debug=True)
