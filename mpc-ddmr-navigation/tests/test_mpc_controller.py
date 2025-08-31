import unittest
from src.mpc.mpc_controller import MPCController

class TestMPCController(unittest.TestCase):

    def setUp(self):
        self.controller = MPCController()

    def test_initialize(self):
        self.controller.initialize()
        self.assertIsNotNone(self.controller.state)

    def test_update(self):
        initial_state = self.controller.state
        self.controller.update()
        self.assertNotEqual(initial_state, self.controller.state)

    def test_compute_control(self):
        control_output = self.controller.compute_control()
        self.assertIsInstance(control_output, list)
        self.assertEqual(len(control_output), self.controller.control_dim)

if __name__ == '__main__':
    unittest.main()