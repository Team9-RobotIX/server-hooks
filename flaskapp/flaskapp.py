from flask import Flask, request
import subprocess
app = Flask(__name__)


@app.route('/pull', methods = ['GET', 'POST'])
def run():
    payload = request.values.get('payload')
    if payload is not None:
        res = ""
        cmd = "/var/www/html/server-hooks/updates.sh"

        try:
            res += subprocess.check_output(
                cmd, shell=True, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            return "Command error: " + str(e.output)
        except Exception as e:
            return "Other exception: " + str(e)

        return res

    return "No payload."


@app.errorhandler(Exception)
def exception_handler(error):
    return "Error: "  + repr(error)


if __name__ == '__main__':
    app.run()
