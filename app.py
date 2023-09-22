from flask import Flask, request, render_template

import subprocess


app = Flask(__name__, template_folder='./app/views/templates/')

@app.route('/')
def index():
    
    return render_template('index.html')

@app.post('/greet')
def greet():
    name = request.form['name']
    result = subprocess.run(['python3', 'app/cli.py', '--name', name], capture_output=True, text=True)
    output = result.stdout.strip()
    return render_template('layaout.html', output=output)

if __name__ == '__main__':
    app.run(port=7280, debug=True)
