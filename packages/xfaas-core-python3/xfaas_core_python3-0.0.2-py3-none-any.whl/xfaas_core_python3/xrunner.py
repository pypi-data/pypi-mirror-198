from xfaas_core_python3.xfunction import XFunction
from flask import request
from flask import Flask

app = Flask(__name__)


# Entrypoint of the function
@app.route("/", methods=['GET', 'POST'])
def xfaas_entry_point():
    subclasses = XFunction.__subclasses__()

    # Check if there is exactly one subclass of XFunction
    if len(subclasses) == 0:
        raise Exception('There is no subclass for XFunction. Make sure to implement XFunction to '
                        'provided a valid function endpoint.')
    if len(subclasses) > 1:
        raise Exception('There are more than one implementations for XFunction. This must be '
                        'avoided as FaaS only provides one entry point.')

    function = subclasses[0]
    function = function()
    # Delegate the call to the implementation of the User
    response = function.call(request=request)
    return response


# Allows to run the server from main function
def run_app():
    app.run(port=8080)


# Needed to get the server object from outside of the package
def get_server():
    return app


if __name__ == '__main__':
    run_app()
