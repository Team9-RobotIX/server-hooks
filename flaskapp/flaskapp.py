from flask import Flask, request
import os
app = Flask(__name__)


@app.route('/pull-production', methods = ['GET', 'POST'])
def run():
    payload = request.values.get('payload')
    if payload is not None:
        os.system("cd ~/production/ && git pull")


if __name__ == '__main__':
    app.run()
