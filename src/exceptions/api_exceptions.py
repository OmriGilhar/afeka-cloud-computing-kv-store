class ApiExceptions(Exception):
    PROTOCOL_NOT_SUPPORTED = ''

    def __init__(self, error):
        self.error = error
        super(self.__class__)
