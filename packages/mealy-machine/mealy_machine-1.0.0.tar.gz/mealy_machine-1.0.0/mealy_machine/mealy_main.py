class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def init(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'E':
            self.state = 'B'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'E'
            return 9
        raise MealyError('init')

    def type(self):
        if self.state == 'A':
            self.state = 'C'
            return 1
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'G'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        raise MealyError('type')


def main():
    return StateMachine()
