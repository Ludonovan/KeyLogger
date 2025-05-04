"""
Runs the server for communication with the GUI
"""


from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    try:
        subprocess.Popen(["python3", "/home/cmpe499/key-logger/capture.py"])  
        return "Script started", 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
