from src.entities.key_value_pair_boundary import KeyValuePairBoundary


class KeyValuePairDummy(KeyValuePairBoundary):
    def __init__(self):
        super().__init__()

    def store(self, entry: KeyValuePairBoundary):
        return {'You Triggered': 'store'}

    def scan(self):
        return [{'You Triggered': 'scan'}, {'Scanning': "......"}]

    def delete_item(self, key: str):
        return [{'You Triggered': 'delete_item'}, {'Smile': "=D"}]

    def delete_all_entries(self) -> list[dict]:
        return [{'You Triggered': 'delete_all_entries'}, {'Smile': "=)"}]

    def get_entry_by_key(self, key: str) -> dict:
        return {'You Triggered': 'get_entry_by_key'}

    def update_entry_by_key(self, key: str, value: any) -> dict:
        return {'You Triggered': 'update_entry_by_key'}
