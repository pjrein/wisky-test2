from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Flask in ubuntu en env '

if __name__ == "__main__":
    app.run()