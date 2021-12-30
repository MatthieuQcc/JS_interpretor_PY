class Number:
    def __init__(self, value):
        self.value = value

    def add(self, other_nb):
        if isinstance(other_nb, Number):
            return Number(self.value + other_nb.value)

    def sub(self, other_nb):
        if isinstance(other_nb, Number):
            return Number(self.value - other_nb.value)

    def mul(self, other_nb):
        if isinstance(other_nb, Number):
            return Number(self.value * other_nb.value)

    def div(self, other_nb):
        if isinstance(other_nb, Number):
            return Number(self.value / other_nb.value)

    def __repr__(self):
        return str(self.value)
