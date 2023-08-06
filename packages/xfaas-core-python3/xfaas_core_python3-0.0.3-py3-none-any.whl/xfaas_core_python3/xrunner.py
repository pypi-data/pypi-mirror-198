from xfaas_core_python3.xfunction import XFunction, DefaultFunction
from flask import request
from flask import Flask

app = Flask(__name__)
target_function = DefaultFunction()


# Entrypoint of the function
@app.route("/", methods=['GET', 'POST'])
def xfaas_entry_point():
    # Delegate the call to the implementation of the User
    response = target_function.call(request=request)
    return response


# Required for OpenFaaS health check
@app.route("/_/health")
def health():
    return app.make_response(("Ok", 200))


# Required for OpenFaaS readiness check
@app.route("/_/ready")
def ready():
    return app.make_response(("Ok", 200))


# Required for Nuclio health check
@app.route("/__internal/health")
def internal_health():
    return app.make_response(("Ok", 200))


# Allows to run the server from main function
def run_app(x_function: XFunction):
    global target_function
    target_function = x_function
    app.run(port=8080)


# Needed to get the server object from outside of the package
def get_server(x_function: XFunction):
    global target_function
    target_function = x_function
    return app


if __name__ == '__main__':
    run_app(DefaultFunction())
