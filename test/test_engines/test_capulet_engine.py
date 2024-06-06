from unittest import TestCase
from engine.capulet_engine import CapuletEngine
class TestCapuletEngine(TestCase):
    def setUp(self):
        self.engine1 = CapuletEngine(100000, 70000)
        self.engine2 = CapuletEngine(100000, 90000)
    def test_current_mileage(self):
        self.assertEqual(self.engine1.current_mileage, 100000)
        self.assertEqual(self.engine2.current_mileage, 100000)
    def test_last_mileage(self):
        self.assertEqual(self.engine1.last_service_mileage, 70000)
        self.assertEqual(self.engine2.last_service_mileage, 90000)
    def test_need_service(self):
        self.assertTrue(self.engine1.need_service())
        self.assertTrue(not self.engine2.need_service())