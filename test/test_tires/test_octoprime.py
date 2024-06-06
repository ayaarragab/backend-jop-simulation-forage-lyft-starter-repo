from tires.OctoprimeTires import OctoprimeTire
from unittest import TestCase

class TestOctoprimeTire(TestCase):
    def setUp(self):
        self.tire1 = OctoprimeTire([1, 1, 1])
        self.tire2 = OctoprimeTire([0.1, 0.5, 0.2])
    def tearDown(self):
        pass
    def testArray(self):
        self.assertEqual(self.tire1.array, [1, 1, 1])
        self.assertEqual(self.tire2.array, [0.1, 0.5, 0.2])
    def testNeedService(self):
        self.assertTrue(self.tire1.need_service())
        self.assertTrue(not self.tire2.need_service())