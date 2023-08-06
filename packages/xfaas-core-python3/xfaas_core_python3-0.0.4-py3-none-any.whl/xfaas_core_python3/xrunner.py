from flask import Flask, request

from xfaas_core_python3.xfunction import DefaultFunction, XFunction

app = Flask(__name__)
target_function = DefaultFunction()


@app.route("/", methods=['GET', 'POST'])
def function_entry():
    return target_function.call(request)


# Required for OpenFaaS health check
@app.route("/_/health")
def openfaas_health():
    return app.make_response(("Ok", 200))


# Required for OpenFaaS readiness check
@app.route("/_/ready")
def openfaas_ready():
    return app.make_response(("Ok", 200))


# Required for Nuclio health check
@app.route("/__internal/health")
def nuclio_health():
    return app.make_response(("Ok", 200))


def get_app(function: XFunction):
    global target_function
    target_function = function
    return app


def run_app(function):
    global target_function
    target_function = function
    app.run(debug=True, host='0.0.0.0', port=8080)


# Local testing
if __name__ == "__main__":
    run_app(DefaultFunction())
