
class FileHandlerError(Exception):
    "Parent class of all error raised by this system"

    def __init__(self, message):
        super(FileHandlerError, self).__init__(message)

class FileReaderError(FileHandlerError):
    "Error indicating that the file input for a function was invalid"
    pass