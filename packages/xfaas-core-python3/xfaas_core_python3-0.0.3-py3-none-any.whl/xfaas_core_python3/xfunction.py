from abc import ABC, abstractmethod
from flask import make_response, Request, Response


class XFunction(ABC):

    @abstractmethod
    def call(self, request: Request) -> Response:
        pass


class DefaultFunction(XFunction):

    def call(self, request):
        return make_response(("Response from default function", 200))
