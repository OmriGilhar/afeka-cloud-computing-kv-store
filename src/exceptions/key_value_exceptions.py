class KeyValueException(Exception):
    KEY_NOT_FOUND = 'Key not found.'

    def __init__(self, error):
        self.error = error
        super(self.__class__)
