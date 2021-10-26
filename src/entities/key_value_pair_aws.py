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
                'content': entry.value,
            }
        )

    def scan(self):
        return self._storage.scan()['Items']

    def delete_item(self, key: str):
        return self._storage.delete_item(
            Key={
                'ID': key
            }
        )

    def delete_all_entries(self) -> list[dict]:
        scan = self._storage.scan()
        with self._storage.batch_writer() as batch:
            for item in scan['Items']:
                batch.delete_item(
                    Key={
                        'ID': item['ID'],
                    }
                )
        return scan['Items']

    def get_entry_by_key(self, key: str) -> dict:
        return self._storage.get_item(
            Key={
                'ID': key
            }
        )['Item']

    def update_entry_by_key(self, key: str, value: any) -> dict:
        return self._storage.update_item(
            Key={
                'ID': key
            },

            UpdateExpression="SET content = :g",
            ExpressionAttributeValues={
                ":g": value
            },
            ReturnValues="ALL_NEW"
        )['Attributes']
