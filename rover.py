from collections import namedtuple

# constants
ORIENTATION = ['N', 'E', 'S', 'W']
ORIENTATION_MAP = {o: i for i, o in enumerate(ORIENTATION)}

Plateau = namedtuple('Plateau', ['x', 'y'])


class Rover(object):

    def __init__(self, x, y, o, plateau):
        error_message = \
            'The coordinates of the rover must be integers, the orientation ' \
            'must be a string with one of these letters "N", "E", "S", "W"'
        assert (isinstance(x, str) and x.isdigit()) or isinstance(x, int), error_message
        assert (isinstance(y, str) and y.isdigit()) or isinstance(y, int), error_message
        assert isinstance(o, str) and o in ORIENTATION, error_message

        self.x = int(x)
        self.y = int(y)
        self.orientation = ORIENTATION_MAP[o]
        self.plateau = plateau

    def change_orientation(self, turn):
        """
        Update rover orientation
        """
        error_message = \
            'The turn must be a string containing one of the letters "L", "R"'
        assert isinstance(turn, str) and turn in ['L', 'R'], error_message

        if turn == 'L':
            self.orientation = (self.orientation - 1 + 4) % 4
        elif turn == 'R':
            self.orientation = (self.orientation + 1) % 4

    def can_move(self, x, y):
        if 0 <= x <= self.plateau.x and 0 <= y <= self.plateau.y:
            return True

        print('Rover does not move due to the plateau limit')
        return False

    def move(self):
        """
        Check the orientation of the rover and update its coordinates

        Means move forward one grid point, and maintain the same heading
        Assume that the square directly North from (x, y) is (x, y+1)
        """

        if self.orientation == 0:  # North
            self.y += 1 if self.can_move(self.x, self.y + 1) else 0
        elif self.orientation == 1:  # East
            self.x += 1 if self.can_move(self.x + 1, self.y) else 0
        elif self.orientation == 2:  # South
            self.y -= 1 if self.can_move(self.x, self.y - 1) else 0
        elif self.orientation == 3:  # West
            self.x -= 1 if self.can_move(self.x - 1, self.y) else 0

    def run(self, inst_list):
        """
        Receives a list of instructions and executes
        """

        for inst in inst_list:
            assert inst in ['L', 'R', 'M'], \
                   'Instructions must be a string containing only the letters'\
                   ' "L", "R" and "M"'

            if inst in ['L', 'R']:
                self.change_orientation(inst)
            elif inst == 'M':
                self.move()

    def position_status(self):
        return f'{self.x} {self.y} {ORIENTATION[self.orientation]}'

    def __str__(self):
        return self.position_status()


def main():
    # upper-right co-ordinates of the plateau
    try:
        plateau = Plateau(*(int(_) for _ in input().split()))
    except TypeError as err:
        print(err)
        print('Plateau coordinates must be integers')

    try:
        while True:
            # rover co-ordinates and orientation
            rover = Rover(*input().split(), plateau)

            # series of instructions
            rover.run(input())

            print(rover)

    except EOFError:
        pass


if __name__ == '__main__':
    main()
