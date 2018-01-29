from flask import Flask, request
import subprocess
app = Flask(__name__)


@app.route('/pull', methods = ['GET', 'POST'])
def run():
    payload = request.values.get('payload')
    if payload is not None:
        subprocess.call("cd ~/production/ && git pull")
        subprocess.call("cd ~/development/ && git pull")
        return "OK."

    return "No payload."


@app.errorhandler(Exception)
def exception_handler(error):
    return "Error: "  + repr(error)


if __name__ == '__main__':
    app.run()
