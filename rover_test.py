# python
import unittest

# project
from rover import ORIENTATION_MAP
from rover import Plateau
from rover import Rover


class RoverTest(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)
        self.rover = Rover(1, 2, 'N', self.plateau)

    def test_rover_create(self):
        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['N'])
        self.assertEqual(self.rover.plateau, self.plateau)

    def test_rover_create_with_wrong_coordinates_input(self):
        rover_data = ['a', 0, 'N', self.plateau]

        with self.assertRaises(AssertionError):
            Rover(*rover_data)

    def test_rover_create_with_wrong_orientation_input(self):
        rover_data = [0, 0, 'A', self.plateau]

        with self.assertRaises(AssertionError):
            Rover(*rover_data)

    def test_rover_change_orientation_to_right(self):
        self.rover.change_orientation('R')

        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['E'])

    def test_rover_change_orientation_to_left(self):
        self.rover.change_orientation('L')

        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['W'])

    def test_rover_change_orientation_with_wrong_type_input(self):
        with self.assertRaises(AssertionError):
            self.rover.change_orientation(0)

        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['N'])

    def test_rover_change_orientation_with_wrong_turn_input(self):
        with self.assertRaises(AssertionError):
            self.rover.change_orientation('A')

        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['N'])

    def test_rover_move_north(self):
        self.rover.move()

        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 3)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['N'])

    def test_rover_move_east(self):
        self.rover.change_orientation('R')  # turn the orientation to the east
        self.rover.move()

        self.assertEqual(self.rover.x, 2)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['E'])

    def test_rover_move_south(self):
        self.rover.change_orientation('R')  # turn the orientation to the south
        self.rover.change_orientation('R')
        self.rover.move()

        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 1)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['S'])

    def test_rover_move_west(self):
        self.rover.change_orientation('L')  # turn the orientation to the west
        self.rover.move()

        self.assertEqual(self.rover.x, 0)
        self.assertEqual(self.rover.y, 2)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['W'])

    def test_rover_move_when_it_can_not(self):
        rover = Rover(0, 0, 'S', self.plateau)
        rover.move()

        self.assertEqual(rover.x, 0)
        self.assertEqual(rover.y, 0)
        self.assertEqual(rover.orientation, ORIENTATION_MAP['S'])

    def test_rover_run_instructions(self):
        self.rover.run('LMLMLMLMM')

        self.assertEqual(self.rover.x, 1)
        self.assertEqual(self.rover.y, 3)
        self.assertEqual(self.rover.orientation, ORIENTATION_MAP['N'])

    def test_rover_run_wrong_instructions(self):
        with self.assertRaises(AssertionError):
            self.rover.run('LMLMA')
