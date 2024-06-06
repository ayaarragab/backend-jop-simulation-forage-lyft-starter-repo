from tires.CarriganTires import CarriganTire
from unittest import TestCase

class TestCarrigantires(TestCase):
    def setUp(self):
        self.tire1 = CarriganTire([1, 0.5, 0.9])
        self.tire2 = CarriganTire([0.1, 0.5, 0.2])
    def tearDown(self):
        pass
    def testArray(self):
        self.assertEqual(self.tire1.array, [1, 0.5, 0.9])
        self.assertEqual(self.tire2.array, [0.1, 0.5, 0.2])
    def testNeedService(self):
        self.assertTrue(self.tire1.need_service())
        self.assertTrue(not self.tire2.need_service())