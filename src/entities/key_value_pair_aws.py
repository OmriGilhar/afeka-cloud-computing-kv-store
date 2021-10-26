import boto3

from src.entities.key_value_pair_boundary import KeyValuePairBoundary


STORAGE_NAME = 'CloudTestTable'


class KeyValuePairAws(KeyValuePairBoundary):
    def __init__(self, resource: str = 'dynamodb', region: str = 'eu-west-1'):
        super().__init__()
        self._type = resource
        self._region = region
        self._resource = boto3.resource(self._type, region_name=self._region)
        self._storage = self._resource.Table(STORAGE_NAME)

    def store(self, entry: KeyValuePairBoundary):
        self._storage.put_item(
            Item={
                'ID': entry.key,
                'value': entry.value,
            }
        )