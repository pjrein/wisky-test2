from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 9090 dit moet ook werken op pi in spijkenisse hoop ik toch '

if __name__ == "__main__":
    app.run()