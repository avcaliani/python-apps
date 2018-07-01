from flask import Flask # pip3 install flask
from controllers.task_controller import TaskController

app = Flask(__name__)

@app.route('/')
def home():
    return "Wellcome to PYService<br>By @avcaliani"

# Registering Controllers
app.register_blueprint(TaskController)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)