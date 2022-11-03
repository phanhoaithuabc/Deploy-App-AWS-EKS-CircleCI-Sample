from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the sample Project DevOps Deploy web on AWS EKS, \
            my name is Phan Hoai Thu</h1>'

app.run(host='localhost', port=80)
