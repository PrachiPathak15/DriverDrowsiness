from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
    subprocess.run(['python', 'try.py'])
    return 'Webcam started successfully'
if __name__=='__main__':
    app.run(debug=True, port=5001)

# def index():
#     return render_template('index.html')

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     subprocess.run(['python', 'try.py'])
#     return 'Script executed successfully'

# if __name__ == '__main__':
#     app.run(debug=True)
