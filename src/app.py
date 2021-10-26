import sys
import uuid
from flask import Flask, request, jsonify, make_response, Response

try:
    from entities.key_value_pair_boundary import KeyValuePairBoundary
    from exceptions.key_value_exceptions import KeyValueException
    from controllers.key_value_controller import KeyValueController
except ModuleNotFoundError:
    from src.entities.key_value_pair_boundary import KeyValuePairBoundary
    from src.exceptions.key_value_exceptions import KeyValueException
    from src.controllers.key_value_controller import KeyValueController

app = Flask(__name__)
kv_controller = KeyValueController()


@app.route(f"/keyValue", methods=['POST', 'GET', 'DELETE'])
def keys() -> Response:
    """
    TODO: Add documentation
    :return:
    """
    try:
        if request.method == 'POST':
            return kv_controller.store_entry(str(uuid.uuid4()), request.json)
        elif request.method == 'GET':
            return kv_controller.get_all_entries()
        elif request.method == 'DELETE':
            return kv_controller.delete_all_entries()
    except KeyValueException as kve:
        if kve.error == KeyValueException.KEY_NOT_FOUND:
            return make_response(jsonify(KeyValueException.KEY_NOT_FOUND), 404)


@app.route(f"/keyValue/<key>", methods=['GET', 'PUT', 'DELETE'])
def keys_manipulation(key: str) -> Response:
    """
    TODO: Add documentation
    :param key:
    :return:
    """
    try:
        if request.method == 'GET':
            return kv_controller.get_entry_by_key(key)
        elif request.method == 'PUT':
            return kv_controller.update_entry_by_key(key, request.get_json())
        elif request.method == 'DELETE':
            return kv_controller.delete_entry_by_key(key)
    except KeyValueException as kve:
        if kve.error == KeyValueException.KEY_NOT_FOUND:
            return make_response(jsonify(KeyValueException.KEY_NOT_FOUND), 404)


def _usage():
    """
    Show the user a usage message.
    """
    print('[ERROR] - No data json has been entered')
    print('Usage:')
    # TODO: Write Usage Message
    print('\t')
    exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        _usage()
    app.run(debug=True, threaded=True, port=5000)
