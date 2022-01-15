from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello dit moet ook werken op pi in spijkenisse hoop ik '

if __name__ == "__main__":
    app.run()