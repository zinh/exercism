class CustomSet(object):
    def __init__(self, elements=[]):
        self.elements = []
        if elements:
          self.elements.append(elements[0])
          for element in elements[1:]:
              self.add(element)

    def isempty(self) -> bool:
        return self.elements == []

    def __contains__(self, element) -> bool:
        return element in self.elements

    def __sub__(self, other):
        return self.difference(other)

    def __add__(self, other):
        return self.union(other)

    def issubset(self, other) -> bool:
        return self.intersection(other) == self

    def isdisjoint(self, other):
        return self.intersection(other).isempty()

    def __eq__(self, other):
        if len(self.elements) == len(other.elements):
            for element in self.elements:
                if element not in other.elements:
                    return False
            return True
        else:
            return False

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def intersection(self, other):
        return CustomSet([i for i in self.elements for j in other.elements if i == j])

    def difference(self, other):
        return CustomSet([i for i in self.elements if i not in other.elements])

    def union(self, other):
        return CustomSet(self.elements + other.elements)
