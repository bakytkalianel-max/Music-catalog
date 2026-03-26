from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

def my_task():
    result=sum(range(1,100000))
    return result
@app.route('/run_task')
def run_task():
    return jsonify({'result':my_task()})

@app.route('/task')
def task():
    a=16
    b=2
    return str(a+b)
@app.route('/')
def home():
    return "сервер работает"
if __name__ == '__main__':
    app.run(port=5000)
