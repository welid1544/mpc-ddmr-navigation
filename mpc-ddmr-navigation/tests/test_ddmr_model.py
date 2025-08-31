import unittest
from src.ddmr.ddmr_model import DDMRModel

class TestDDMRModel(unittest.TestCase):

    def setUp(self):
        self.model = DDMRModel()

    def test_set_reference(self):
        reference = [1.0, 2.0, 3.0]
        self.model.set_reference(reference)
        self.assertEqual(self.model.reference, reference)

    def test_update_state(self):
        initial_state = [0.0, 0.0]
        self.model.update_state(initial_state)
        self.assertEqual(self.model.state, initial_state)

    def test_get_state(self):
        state = [1.0, 1.0]
        self.model.update_state(state)
        self.assertEqual(self.model.get_state(), state)

if __name__ == '__main__':
    unittest.main()