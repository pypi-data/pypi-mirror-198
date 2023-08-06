from flask import Flask, request, jsonify, make_response
from waitress import serve as serve


class Sculpture(object):
    def __init__(self, inference_function):
        self._inference_function = inference_function

        self._app = Flask(__name__)
        self._app.add_url_rule("/invocations", methods=["POST"], view_func=self.invocations)
        self._app.add_url_rule("/ping", methods=["POST"], view_func=self.ping)

    def invocations(self):
        request_body = request.get_json()
        result = self._inference_function(request_body)
        return jsonify({"result": result})

    def ping(self):
        return make_response(None, 200)

    def serve(self, debug: bool = False):
        if debug:
            self._app.run(port=8080, debug=True)
        else:
            serve(self._app, port=8080)
