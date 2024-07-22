class ResponseWrapper:

    def __init__(self, ok, status_code, data):
        self._ok = ok
        self._status_code = status_code
        self._data = data

        # Getter for _ok

    @property
    def ok(self):
        return self._ok

    # Setter for _ok
    @ok.setter
    def ok(self, value):
        self._ok = value

    # Getter for _status_code
    @property
    def status_code(self):
        return self._status_code

    # Setter for _status_code
    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    # Getter for _data
    @property
    def data(self):
        return self._data

    # Setter for _data
    @data.setter
    def data(self, value):
        self._data = value
