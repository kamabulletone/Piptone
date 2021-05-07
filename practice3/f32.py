


class C32:
    def __init__(self):
        self.state = 'A'
    def print(self):
        if (self.state == 'A'):
            self.state = 'B'
            return 0
        elif (self.state == 'C'):
            self.state = 'C'
            return 5
        elif (self.state == 'D'):
            self.state = 'E'
            return 6
        elif (self.state == 'E'):
            self.state = 'C'
            return 8
        else:
            RuntimeError
    def trim(self):
        if (self.state == 'B'):
            self.state = 'C'
            return 1
        elif (self.state == 'E'):
            self.state = 'F'
            return 7
        elif (self.state == 'G'):
            self.state = 'H'
            return 10
        else:
            RuntimeError
    def trace(self):
        if (self.state == 'C'):
            self.state = 'D'
            return 3
        elif (self.state == 'F'):
            self.state = 'G'
            return 9
        elif (self.state == 'G'):
            self.state = 'G'
            return 11
        else:
            RuntimeError
    def step(self):
        if (self.state == 'B'):
            self.state = 'G'
            return 2
        elif (self.state == 'C'):
            self.state = 'G'
            return 4
        else:
            RuntimeError


