import sys
import uuid
from typing import Any, Union
from flask import Flask, request, jsonify, make_response, Response

try:
    from entities.key_value_pair_boundary import KeyValuePairBoundary
    from exceptions.key_value_exceptions import KeyValueException
except ModuleNotFoundError:
    from src.entities.key_value_pair_boundary import KeyValuePairBoundary
    from src.exceptions.key_value_exceptions import KeyValueException

app = Flask(__name__)


def _get_entry_by_key(key: str) -> Response:
    """
    TODO: Add documentation

    :param key:
    :return:
    """
    # TODO: Implement getting value by Key from AWS
    return jsonify({})


def _update_entry_by_key(key: str, value: Any) -> Response:
    """
    TODO: Add documentation

    :param key:
    :param value:
    :return:
    """
    # TODO: Implement updating a value by Key from AWS
    return jsonify({})


def _delete_entry_by_key(key: str) -> Response:
    """
    TODO: Add documentation
    :param key:
    :return:
    """
    # TODO: Implement deleting an entry by Key from AWS
    return jsonify({})


def _store_entry(key: str, value: Any) -> Response:
    kv_boundary = KeyValuePairBoundary(key, value)

    # TODO: Implement storing on AWS

    return jsonify(kv_boundary.__dict__)


def _get_all_entries() -> Response:
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 1, type=int)

    # TODO: Call AWS to get all entries
    return jsonify([])


def _delete_all_entries() -> Response:
    """
    TODO: Add documentation
    :return:
    """
    # TODO: Call AWS to delete all entries
    return jsonify([])


@app.route(f"/keyValue", methods=['POST', 'GET', 'DELETE'])
def keys() -> Response:
    """
    TODO: Add documentation
    :return:
    """
    try:
        if request.method == 'POST':
            return _store_entry(str(uuid.uuid4()), request.json)
        elif request.method == 'GET':
            return _get_all_entries()
        elif request.method == 'DELETE':
            return _delete_all_entries()
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
            return _get_entry_by_key(key)
        elif request.method == 'PUT':
            return _update_entry_by_key(key, request.get_json())
        elif request.method == 'DELETE':
            return _delete_entry_by_key(key)
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
    app.run(debug=True)
