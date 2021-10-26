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
        return jsonify(self._interface.get_entry_by_key(key))

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
        size = request.args.get('size', 10, type=int)

        response = self._interface.scan()
        return jsonify(self._paginate(response, page, size))

    def delete_all_entries(self) -> Response:
        """
        TODO: Add documentation
        :return:
        """
        return jsonify(self._interface.delete_all_entries())

    @staticmethod
    def _paginate(response: list, pages: int, size: int) -> list:
        """
        This method will paginate the list from the DB
        by number of pages and number of items in every page.
        :param response: list from storage
        :param pages: number of pages to return
        :param size: number of items in page
        :return: paginated list
        """
        return_list = []
        for list_index in range(pages):
            if not len(response):
                break
            return_list.append([])
            while len(return_list[list_index]) < size and len(response):
                return_list[list_index].append(response.pop())
        return return_list

