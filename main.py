from flask import Flask, escape, request, send_file, Response, make_response
import os
import subprocess


app = Flask(__name__)
TMP_FILE_NAME='temp.md'

# @app.route('/')
# def hello():

def run(args):
    cmd = ['pandoc']
    args = args.get('args', '--help')
    cmd.append(TMP_FILE_NAME)
    # cmd.extend(['--template', 'template.html'])
    cmd.extend(args.split(' '))

    process = subprocess.run(cmd, stdout=subprocess.PIPE)

    return process.stdout


@app.route('/', methods=['POST'])
def conv():
    with open(TMP_FILE_NAME, 'wb') as fd:
        fd.write(request.get_data())
    result = run(request.args)
    with open('test.html', 'w') as out_f:
        out_f.write(str(result))

    return result

port = int(os.getenv('FLASK_PORT', 3000))
app.run(host='0.0.0.0', port=port)
