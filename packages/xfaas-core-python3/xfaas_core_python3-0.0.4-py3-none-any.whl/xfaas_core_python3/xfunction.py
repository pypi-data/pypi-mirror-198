from abc import ABC
from flask import make_response


class XFunction(ABC):

    def call(self, request):
        # Put your custom logic here
        return make_response(("Response from default function handler", 200))


class DefaultFunction(XFunction):

    def call(self, request):
        return make_response(("Response from default function handler", 200))