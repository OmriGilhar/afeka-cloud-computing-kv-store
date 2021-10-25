class KeyValueException(RuntimeError):
    KEY_NOT_FOUND = 'Key not found.'
    KEY_ERROR = 'error key'

    def __init__(self, error):
        self.error = error
        super(self.__class__)
