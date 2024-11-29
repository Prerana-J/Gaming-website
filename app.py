
from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script')
def run_script():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game3.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result
#New function to call new python script
@app.route('/run-script2')
def run_script2():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game4.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result

@app.route('/run-script3')
def run_script3():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game5.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script8')
def run_script8():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game8.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script9')
def run_script9():
    # Call your Python script here
    process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


@app.route('/run-script7')
def run_script7():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game7.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result
@app.route('/run-script77')
def run_script77():
    # Call your Python script here
    process = subprocess.Popen(['python', 'game7,1.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result

@app.route('/run-script10')
def run_script10():
    # Call your Python script here
    process = subprocess.Popen(['python', 'ggame10.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return_code = process.returncode
    result = ""
    return result


if __name__ == '__main__':
    app.run(debug=True)