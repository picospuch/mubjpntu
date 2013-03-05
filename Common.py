class LengthError(Exception):
    def __init__(self, length):
        self._length = length

    def __str__(self):
        return "Invalid Length, here must be %d" % self._length

