class InputCell(object):
    def __init__(self, initial_value):
        self._value = initial_value

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    value = property(get_value, set_value)


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.value = compute_function(inputs)

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass

    def expect_callback_values(self, callback):
        pass
