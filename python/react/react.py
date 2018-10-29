class InputCell(object):
    def __init__(self, initial_value, subscribers=[]):
        self._value = initial_value
        self.subscribers = subscribers

    def set_value(self, value):
        if self._value != value:
            self._value = value
            for subscriber in self.subscribers:
                subscriber.callback()

    def get_value(self):
        return self._value

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    value = property(get_value, set_value)


class ComputeCell(object):
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self._value = compute_function(list(map(lambda cell: cell.value, inputs)))
        self.subscribers = []
        self.callbacks = set()
        for input_cell in inputs:
            input_cell.add_subscriber(self)

    def add_callback(self, callback):
        self.callbacks.add(callback)

    def remove_callback(self, callback):
        self.callbacks.discard(callback)

    def callback(self):
        new_value = self.compute_function(list(map(lambda cell: cell.value, self.inputs)))
        self.value = new_value

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def get_value(self):
        return self._value

    def set_value(self, new_value):
        if new_value != self._value:
            self._value = new_value
            for callback in self.callbacks:
                callback(new_value)
            for subscriber in self.subscribers:
                subscriber.callback()

    value = property(get_value, set_value)

input_ = InputCell(1)
plus_one = ComputeCell([input_], lambda inputs: inputs[0] + 1)
minus_one = ComputeCell([input_], lambda inputs: inputs[0] - 1)
always_two = ComputeCell( [plus_one, minus_one], lambda inputs: inputs[0] - inputs[1])
observer = []
callback1 = lambda value: observer.append(value)
always_two.add_callback(callback1)
input_.value = 2
print(always_two.value)
print(observer)
#input_.value = 3
#print(always_two.value)
#input_.value = 4
#print(always_two.value)
#input_.value = 5
#print(always_two.value)
