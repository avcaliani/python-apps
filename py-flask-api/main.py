from flask import Flask
from controllers.task_controller import TaskController
__author__  = 'Anthony Vilarim Caliani'
__contact__ = 'https://github.com/avcaliani'
__license__ = 'MIT'

app = Flask(__name__)

@app.route('/')
def home():
    return "Wellcome to PYService<br>By @avcaliani"

# Registering Controllers
app.register_blueprint(TaskController)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)