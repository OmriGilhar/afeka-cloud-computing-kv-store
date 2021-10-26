from flask import request, jsonify, Response

from src.entities.key_value_pair_boundary import KeyValuePairBoundary
from src.entities.key_value_pair_aws import KeyValuePairAws


class KeyValueController:
    def __init__(self):
        self._interface = KeyValuePairAws()

    def store_entry(self, key: str, value: any) -> Response:
        """
        TODO: Add documentation

        :param key:
        :param value:
        :return:
        """
        kv_boundary = KeyValuePairBoundary(key, value)
        self._interface.store(kv_boundary)
        return jsonify(kv_boundary.__dict__)

    def get_entry_by_key(self, key: str) -> Response:
        """
        TODO: Add documentation

        :param key:
        :return:
        """
        # TODO: Implement getting value by Key from AWS
        return jsonify({})

    def update_entry_by_key(self, key: str, value: any) -> Response:
        """
        TODO: Add documentation

        :param key:
        :param value:
        :return:
        """
        # TODO: Implement updating a value by Key from AWS
        return jsonify({})

    def delete_entry_by_key(self, key: str) -> Response:
        """
        TODO: Add documentation
        :param key:
        :return:
        """
        # TODO: Implement deleting an entry by Key from AWS
        return jsonify({})

    def get_all_entries(self) -> Response:
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 1, type=int)

        # TODO: Call AWS to get all entries
        return jsonify([])

    def delete_all_entries(self) -> Response:
        """
        TODO: Add documentation
        :return:
        """
        return jsonify(self._interface.delete_all_entries())
