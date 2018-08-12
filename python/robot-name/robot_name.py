import random
from os import urandom

class Robot(object):
    def __init__(self):
        self.assign_name()
    def name(self):
        return self.name
    def reset(self):
        self.assign_name()
    def assign_name(self):
        random.seed(urandom(5))
        head = random.choices([chr(c) for c in range(ord('A'), ord('Z'))], k=2)
        tail = random.choices([str(i) for i in range(0, 9)], k=3)
        self.name = ''.join(head + tail)
